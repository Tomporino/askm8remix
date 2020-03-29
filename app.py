from flask import Flask, render_template, redirect, request, url_for
import data_handler

app = Flask(__name__)


@app.route('/')
def home():
    questions = data_handler.get_questions()
    return render_template('home.html', questions=questions)


@app.route('/question/<question_id>')
def question(question_id):
    question = data_handler.get_selected_question(question_id)
    answers = data_handler.get_answers_for_question(question_id)
    return render_template('question.html', question=question, answers=answers)


if __name__ == '__main__':
    app.run()
