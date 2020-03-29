import connection


@connection.connection_handler
def get_questions(cursor):
    query = """
            SELECT * FROM question;"""
    cursor.execute(query)
    return cursor.fetchall()
