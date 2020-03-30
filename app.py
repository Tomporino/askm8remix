from flask import Flask, render_template, redirect, request, url_for
import data_handler
import util

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        column = request.form['selector']
        direction = request.form['direction']
        questions = data_handler.get_ordered_data(column, direction)
    else:
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
            'image': None
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
            'image': None
        }
        data_handler.add_question(user_question)
        return redirect('/')
    return render_template('add_question.html')


@app.route('/question/<question_id>/upvote')
def upvote_question(question_id):
    data_handler.upvote_question(question_id)
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
        return redirect(url_for('question', question_id=question_id))
    return render_template('edit_question.html', question=data_handler.get_selected_question(question_id))


@app.route('/delete-question/<question_id>')
def delete_question(question_id):
    data_handler.delete_question(question_id)
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
            'edited_count': 0
        }
        data_handler.add_comment(answer_comment)
        return redirect(url_for('question', question_id=answer['question_id']))

    return render_template('comment.html', answer=answer, question=question)


@app.route('/answer/<answer_id>/edit', methods=['GET', 'POST'])
def edit_answer(answer_id):
    answer = data_handler.get_selected_answer(answer_id)

    if request.method == 'POST':
        edited_answer = {
            'id':answer_id,
            'submission_time':util.get_current_time(),
            'message':request.form['edit_answer'],
            'image':None
        }
        data_handler.update_answer(edited_answer)
        return redirect(url_for('question', question_id=answer['question_id']))

    return render_template('answer.html', answer=answer)



if __name__ == '__main__':
    app.run()
