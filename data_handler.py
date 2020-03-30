import connection


@connection.connection_handler
def get_questions(cursor):
    query = """
            SELECT * FROM question
            ORDER BY submission_time;
            """
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def get_selected_question(cursor, question_id):
    query = """
            SELECT * FROM question
            WHERE id=%(question_id)s;
            """
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchone()


@connection.connection_handler
def get_answers_for_question(cursor, question_id):
    query = """
            SELECT * FROM answer
            WHERE question_id=%(question_id)s;
            """
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()


@connection.connection_handler
def add_answer(cursor, details):
    query = """
            INSERT INTO answer (submission_time, vote_number, question_id, message, image)
            VALUES (%(submission_time)s, %(vote_number)s, %(question_id)s, %(message)s, %(image)s);
            """
    cursor.execute(query, details)


@connection.connection_handler
def add_question(cursor, details):
    query = """
            INSERT into question (submission_time, view_number, vote_number, title, message, image)
            VALUES (%(submission_time)s, %(view_number)s, %(vote_number)s, %(title)s, %(message)s, %(image)s);
            """
    cursor.execute(query, details)


@connection.connection_handler
def view_counter(cursor, question_id):
    query = """
           UPDATE question
           SET view_number = view_number + 1
           WHERE id = %(question_id)s;
           """
    cursor.execute(query, {'question_id': question_id})


@connection.connection_handler
def upvote_question(cursor, question_id):
    query = """
            UPDATE question
            SET vote_number = vote_number + 1
            WHERE id = %(question_id)s;
            """
    cursor.execute(query, {'question_id': question_id})


@connection.connection_handler
def edit_question(cursor, details):
    query = """
            UPDATE question
            SET title = %(title)s, message = %(message)s, image = %(image)s
            WHERE id = %(id)s
            """
    cursor.execute(query, details)
