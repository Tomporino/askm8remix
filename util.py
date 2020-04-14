from datetime import datetime
import bcrypt


def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_valid_questions(questions, search_phrase, key):
    for question in questions:
        if search_phrase.lower() in question[key].lower():
            for word in question[key].split(" "):
                if word.lower() == search_phrase.lower():
                    question[key] = question[key].replace(word,
                                                          '<span id="search_phrase">' + word + '</span>')


def hash_pass(password):
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_pass.decode('utf-8')


def verify_password(password, hashed_pass):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_pass.encode('utf-8'))

