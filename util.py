from datetime import datetime
import bcrypt
import data_handler
import os


def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_valid_questions(questions, search_phrase, key):
    for question in questions:
        if search_phrase.lower() in question[key].lower():
            for word in question[key].split(" "):
                if word.lower() == search_phrase.lower():
                    question[key] = question[key].replace(word,
                                                          '<span id="search_phrase">' + word + '</span>')


def valid_filename(filename):
    return os.path.splitext(filename)[1] in data_handler.ALLOWED_EXTENSIONS


def hash_pass(password):
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_pass.decode('utf-8')


def verify_password(password, hashed_pass):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_pass.encode('utf-8'))


def check_login(username, password):
    right_user = data_handler.get_right_user(username)
    if right_user == []:
        return False
    else:
        for i in right_user:
            if verify_password(password, i['password']) is True:
                return True
            else:
                return False


def get_user_detail(username, user_detail):
    user_details = data_handler.get_right_user(username)
    for i in user_details:
        return i[user_detail]




