from flask import Flask, render_template, redirect, request, url_for
import data_handler
import util

app = Flask(__name__)


@app.route('/')
def home():
    questions = data_handler.get_questions()
    return render_template('home.html', questions=questions)


@app.route('/question/<question_id>', methods=['POST', 'GET'])
def question(question_id):
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
    question = data_handler.get_selected_question(question_id)
    answers = data_handler.get_answers_for_question(question_id)
    return render_template('question.html', question=question, answers=answers)


if __name__ == '__main__':
    app.run()
