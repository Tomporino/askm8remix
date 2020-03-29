from flask import Flask, render_template, redirect, request, url_for
import data_handler

app = Flask(__name__)


@app.route('/')
def home():
    questions = data_handler.get_questions()
    return render_template('home.html', questions=questions)


if __name__ == '__main__':
    app.run()
