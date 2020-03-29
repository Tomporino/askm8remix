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
            WHERE question_id=%(question_id)s"""
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()