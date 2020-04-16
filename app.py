from flask import Flask, render_template, redirect, request, url_for, session
import data_handler
import util
import error_handling
from datetime import date

app = Flask(__name__)
app.secret_key = b'|\xbc\x93\xc0:&EXh5\xd1\xf5)|\x10N'

@app.route('/')
def index():
    questions = data_handler.get_top_questions(5)
    return render_template('home.html', questions=questions, limit=True)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        column = request.form['selector']
        direction = request.form['direction']
        questions = data_handler.get_ordered_data(column, direction)
        return render_template('home.html', questions=questions)
    questions = data_handler.get_questions()
    return render_template('home.html', questions=questions)


@app.route('/question/<question_id>', methods=['POST', 'GET'])
def question(question_id):
    comments = data_handler.get_comments()

    if request.method == 'POST':
        user_answer = {
            'submission_time': util.get_current_time(),
            'vote_number': 0,
            'question_id': question_id,
            'message': request.form['answer_message'],
            'image': None,
            'user_id':session.get('id')
        }
        data_handler.add_answer(user_answer)
        return redirect(request.url)
    data_handler.view_counter(question_id)
    question = data_handler.get_selected_question(question_id)
    answers = data_handler.get_answers_for_question(question_id)
    return render_template('question.html', question=question, answers=answers, comments=comments)


@app.route('/add-question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        user_question = {
            'submission_time': util.get_current_time(),
            'view_number': 0,
            'vote_number': 0,
            'title': request.form['title'],
            'message': request.form['message'],
            'image': None,
            'user_id': session.get('id')
        }
        question_id = data_handler.add_question(user_question)
        if request.form['tag-selector'] != 'None':
            data_handler.set_question_tag(question_id['id'], int(request.form['tag-selector']))
        return redirect('/')
    return render_template('add_question.html', tags=data_handler.get_tags())


@app.route('/question/<question_id>/upvote')
def upvote_question(question_id):
    data_handler.upvote_question(question_id)
    data_handler.upvote_reputation_question(question_id)
    return redirect(url_for('question', question_id=question_id))


@app.route('/edit-question/<question_id>', methods=['GET', 'POST'])
def edit_question(question_id):
    if request.method == 'POST':
        user_question = {
            'id': question_id,
            'title': request.form['title'],
            'message': request.form['message'],
            'image': None
        }
        data_handler.edit_question(user_question)
        if request.form['tag_selector'] and int(question_id) not in [tag['question_id'] for tag in data_handler.get_question_tags()]:
            data_handler.set_question_tag(question_id, int(request.form['tag_selector']))
        else:
            data_handler.update_question_tag(question_id, int(request.form['tag_selector']))
        return redirect(url_for('question', question_id=question_id))
    return render_template('edit_question.html', question=data_handler.get_selected_question(question_id), tags=data_handler.get_tags())


@app.route('/delete-question/<question_id>')
def delete_question(question_id):
    data_handler.delete_question(question_id)
    return redirect('/')


@app.route('/add-tag/<new_tag>')
def add_tag(new_tag):
    if error_handling.check_tag(new_tag, [tag['name'] for tag in data_handler.get_tags()]):
        data_handler.add_tag(new_tag)
    return redirect('/')


@app.route('/comment/<answer_id>/new_comment', methods=['GET', 'POST'])
def add_comment_to_answer(answer_id):
    answer = data_handler.get_selected_answer(answer_id)

    if request.method == 'POST':
        answer_comment = {
            'question_id': answer['question_id'],
            'answer_id': answer_id,
            'message': request.form['answer_comment'],
            'submission_time': util.get_current_time(),
            'edited_count': 0,
            'user_id': session.get('id')
        }
        data_handler.add_comment(answer_comment)
        return redirect(url_for('question', question_id=answer['question_id']))

    return render_template('comment.html', answer=answer, question=question)


@app.route('/answer/<answer_id>/edit', methods=['GET', 'POST'])
def edit_answer(answer_id):
    answer = data_handler.get_selected_answer(answer_id)

    if request.method == 'POST':
        edited_answer = {
            'id': answer_id,
            'submission_time': util.get_current_time(),
            'message': request.form['edit_answer'],
            'image': None
        }
        data_handler.update_answer(edited_answer)
        return redirect(url_for('question', question_id=answer['question_id']))

    return render_template('answer.html', answer=answer)


@app.route('/comment/<comment_id>/edit', methods=['GET', 'POST'])
def edit_comment(comment_id):
    edit = True
    comment = data_handler.get_comment_by_id(comment_id)

    if request.method == 'POST':
        edited_comment = {
            'id': comment_id,
            'message': request.form['edit_comment'],
            'submission_time': util.get_current_time()
        }
        data_handler.update_comment(edited_comment)
        return redirect(url_for('question', question_id=comment['question_id']))
    return render_template('comment.html', edit=edit, comment=comment)


@app.route('/comment/<comment_id>/delete')
def delete_comment(comment_id):

    comment = data_handler.get_comment_by_id(comment_id)
    data_handler.delete_comment(comment_id)

    return redirect(url_for('question', question_id=comment['question_id']))


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_phrase = request.form['search']
        questions = data_handler.get_search_questions(search_phrase=search_phrase)
        util.get_valid_questions(questions, search_phrase, 'title')
    else:
        return redirect('/')

    return render_template('home.html', questions=questions)


@app.route('/questions/<answer_id>/delete_answer')
def delete_answer(answer_id):
    answer = data_handler.get_selected_answer(answer_id)
    data_handler.delete_answer(answer_id)

    return redirect(url_for('question', question_id=answer['question_id']))


@app.route('/registration', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user_data = {
            'username': request.form['username'],
            'password': util.hash_pass(request.form['password']),
            'password_confirm': util.hash_pass(request.form['password_confirm']),
            'email': request.form['email'],
            'registration_date':date.today()

        }
        if error_handling.check_registration(user_data):
            data_handler.save_user(user_data)
            return redirect(url_for('index'))
    return render_template('registration.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    wrong_login = None
    if request.method == 'POST':

        username = request.form['login-username']
        password = request.form['login-password']

        if util.check_login(username, password) == True:
            session['username'] = util.get_user_detail(username, 'username')
            session['id'] = util.get_user_detail(username, 'id')
            session['email'] = util.get_user_detail(username, 'email')

            return redirect('/')

        else:
            wrong_login = True

    return render_template('login.html', wrong_login=wrong_login)


@app.route('/logut')
def logout():
    session.pop('username', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect('/')


@app.route('/questions/<answer_id>/answer_vote_up')
def voteup_answer(answer_id):
    answer = data_handler.get_selected_answer(answer_id)
    data_handler.upvote_answer(answer_id)
    data_handler.upvote_reputation_answer(answer_id)
    return redirect(url_for('question', question_id=answer['question_id']))


@app.route('/user-page/<username>')
def user_page(username):
    user_info = data_handler.get_user_by_name(username)
    return render_template('user_page.html', user_info=user_info)


@app.route('/questions/<answer_id>/accepted')
def accepted(answer_id):
    answer = data_handler.get_selected_answer(answer_id)
    data_handler.accept_answer(answer_id)
    data_handler.accepted_answer_reputation(answer_id)

    return redirect(url_for('question', question_id=answer['question_id']))

if __name__ == '__main__':
    app.run(
        debug=True
    )
