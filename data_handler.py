import connection


@connection.connection_handler
def get_questions(cursor):
    query = """
            SELECT * FROM question;"""
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def get_selected_question(cursor, question_id):
    query = """
            SELECT * FROM question
            WHERE id=%(question_id)s;"""
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchone()


@connection.connection_handler
def get_answers_for_question(cursor, question_id):
    query = """
            SELECT * FROM answer
            WHERE question_id=%(question_id)s;"""
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()


@connection.connection_handler
def add_answer(cursor, details):
    query = """
            INSERT INTO answer (submission_time, vote_number, question_id, message, image)
            VALUES (%(submission_time)s, %(vote_number)s, %(question_id)s, %(message)s, %(image)s)"""
    cursor.execute(query, details)