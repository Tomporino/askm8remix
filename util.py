from datetime import datetime


def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_valid_questions(questions, search_phrase, key):
    for question in questions:
        if search_phrase in question[key]:
            question[key] = question[key].replace(search_phrase,
                                                  '<span id="search_phrase">' + search_phrase + '</span>')
