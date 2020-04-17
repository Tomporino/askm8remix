from psycopg2 import sql
import connection
import os

UPLOAD_FOLDER = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'static/images/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


@connection.connection_handler
def get_questions(cursor):
    query = """
            SELECT * FROM question
            ORDER BY submission_time DESC;
            """
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def get_top_questions(cursor, n):
    query = """
            SELECT * FROM question
            ORDER BY submission_time DESC
            LIMIT %(n)s;
            """
    cursor.execute(query, {'n': n})
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
            WHERE question_id=%(question_id)s
            ORDER BY submission_time DESC;
            """
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()


@connection.connection_handler
def add_answer(cursor, details):
    query = """
            INSERT INTO answer (submission_time, vote_number, question_id, message, image, user_id)
            VALUES (%(submission_time)s, %(vote_number)s, %(question_id)s, %(message)s, %(image)s, %(user_id)s);
            """
    cursor.execute(query, details)


@connection.connection_handler
def add_question(cursor, details):
    query = """
            INSERT INTO question (submission_time, view_number, vote_number, title, message, image, user_id)
            VALUES (%(submission_time)s, %(view_number)s, %(vote_number)s, %(title)s, %(message)s, %(image)s, %(user_id)s)
            RETURNING id;
            """
    cursor.execute(query, details)
    return cursor.fetchone()


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
            WHERE question.id = %(question_id)s
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


@connection.connection_handler
def delete_question(cursor, question_id):
    query = """
            DELETE FROM comment
            WHERE question_id=%(id)s;
            DELETE FROM answer
            WHERE question_id=%(id)s;
            DELETE FROM question_tag
            WHERE question_id=%(id)s;
            DELETE FROM question
            WHERE id = %(id)s;
            """
    cursor.execute(query, {'id': question_id})


@connection.connection_handler
def get_ordered_data(cursor, column, direction):
    cursor.execute(sql.SQL("""
             SELECT * FROM question
             ORDER BY {column} {direction}""").format(column=sql.SQL(column), direction=sql.SQL(direction)))
    return cursor.fetchall()


@connection.connection_handler
def add_comment(cursor, comment):
    query = """
        INSERT INTO comment (question_id, answer_id, message, submission_time, edited_count, user_id)
        VALUES (%(question_id)s, %(answer_id)s, %(message)s, %(submission_time)s, %(edited_count)s, %(user_id)s)"""
    cursor.execute(query, comment)


@connection.connection_handler
def get_selected_answer(cursor, answer_id):
    query = """
        SELECT * FROM answer
        WHERE id = %(answer_id)s"""
    cursor.execute(query, {'answer_id': answer_id})
    return cursor.fetchone()


@connection.connection_handler
def get_comments(cursor):
    query = """
        SELECT * FROM comment"""
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def update_answer(cursor, answer):
    query = """
        UPDATE answer
        SET submission_time = %(submission_time)s, message = %(message)s, image = %(image)s
        WHERE id = %(id)s"""
    cursor.execute(query, answer)


@connection.connection_handler
def update_comment(cursor, comment):
    query = """
        UPDATE comment
        SET message = %(message)s, submission_time=%(submission_time)s
        WHERE id = %(id)s"""
    cursor.execute(query, comment)


@connection.connection_handler
def get_comment_by_id(cursor, comment_id):
    query = """
        SELECT * FROM comment
        WHERE id = %(comment_id)s"""
    cursor.execute(query, {'comment_id': comment_id})
    return cursor.fetchone()


@connection.connection_handler
def delete_comment(cursor, comment_id):
    query = """
        DELETE FROM comment
        WHERE id = %(comment_id)s"""
    cursor.execute(query, {'comment_id': comment_id})


@connection.connection_handler
def add_tag(cursor, new_tag):
    query = """
            INSERT INTO tag (name)
            VALUES (%(new_tag)s);
            """
    cursor.execute(query, {'new_tag': new_tag})


@connection.connection_handler
def get_tags(cursor):
    query = """
            SELECT * FROM tag;
            """
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def get_question_tags(cursor):
    query = """
            SELECT * FROM question_tag;
            """
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def set_question_tag(cursor, question_id, tag_id):
    query = """
            INSERT INTO question_tag (question_id, tag_id)
            VALUES (%(question_id)s, %(tag_id)s);
            """
    cursor.execute(query, {'question_id': question_id, 'tag_id': tag_id})


@connection.connection_handler
def update_question_tag(cursor, question_id, tag_id):
    query = """
            UPDATE question_tag
            SET tag_id=%(tag_id)s
            WHERE question_id = %(question_id)s;
            """
    cursor.execute(query, {'question_id': question_id, 'tag_id': tag_id})


@connection.connection_handler
def get_search_questions(cursor, search_phrase):
    query = """
            SELECT *
            FROM question
            WHERE title ILIKE %(search)s OR message ILIKE %(search)s;
    """
    cursor.execute(query, {'search': '%' + search_phrase + '%'})
    return cursor.fetchall()


@connection.connection_handler
def delete_answer(cursor, answer_id):
    query = """
        DELETE FROM comment
        WHERE answer_id = %(answer_id)s;
        DELETE FROM answer
        WHERE id = %(answer_id)s
        """
    cursor.execute(query, {'answer_id': answer_id})


@connection.connection_handler
def save_user(cursor, user_data):
    cursor.execute('''
        INSERT INTO users (username, password, email, registration_date)
        VALUES (%(username)s, %(password)s, %(email)s, %(registration_date)s)
    ''', user_data)


@connection.connection_handler
def get_users(cursor):
    cursor.execute('''
            SELECT *
            FROM users
            ''')
    return cursor.fetchall()


@connection.connection_handler
def get_user_by_name(cursor, username):
    cursor.execute('''
            SELECT *
            FROM users
            WHERE username=%(username)s;
            ''', {'username': username})
    return cursor.fetchone()


@connection.connection_handler
def get_right_user(cursor, userdata):
    cursor.execute('''
        SELECT id,username,password,email
        FROM users
        WHERE username=%(userdata)s
        ''', {'userdata': userdata})
    return cursor.fetchall()


@connection.connection_handler
def upvote_answer(cursor, answer_id):
    cursor.execute('''
            UPDATE answer
            SET vote_number = vote_number + 1
            WHERE answer.id = %(answer_id)s
            ''', {'answer_id': answer_id})


@connection.connection_handler
def upvote_reputation_answer(cursor, answer_id):
    cursor.execute('''
            UPDATE users
            SET reputation = reputation + 10
            FROM answer
            WHERE answer.id = %(answer_id)s AND answer.user_id = users.id
            ''', {'answer_id': answer_id})


@connection.connection_handler
def upvote_reputation_question(cursor, question_id):
    cursor.execute(''' 
        UPDATE users
        SET reputation = reputation + 5
        FROM question
        WHERE question.id = %(question_id)s AND question.user_id = users.id
        ''', {'question_id': question_id})


@connection.connection_handler
def search_friends(cursor, search_user):
    cursor.execute('''
        SELECT id, username, email
        FROM users
        WHERE username LIKE %(search_user)s OR email like %(search_user)s        
        ''', {'search_user': f'%{search_user}%'})
    return cursor.fetchall()


@connection.connection_handler
def accept_answer(cursor, answer_id):
    cursor.execute('''
            UPDATE answer
            SET accepted = TRUE 
            WHERE id = %(answer_id)s
            ''', {'answer_id': answer_id})


@connection.connection_handler
def accepted_answer_reputation(cursor, answer_id):
    cursor.execute('''
            UPDATE users
            SET reputation = reputation + 15
            FROM answer
            WHERE answer.id = %(answer_id)s AND answer.user_id = users.id

            ''', {'answer_id': answer_id})


@connection.connection_handler
def set_friends(cursor, user_id, friend_id):
    cursor.execute('''
            INSERT INTO friends (user_id, friend_id)
            VALUES (%(user_id)s, %(friend_id)s)
            ''', {'user_id': user_id, 'friend_id': friend_id})


@connection.connection_handler
def search_user_friends(cursor, user_id):
    cursor.execute('''
            SELECT friends.friend_id, users.username, users.email, users.reputation
            FROM friends
            INNER JOIN users ON friends.friend_id = users.id
            WHERE user_id = %(user_id)s
            ''', {'user_id': user_id})
    return cursor.fetchall()


@connection.connection_handler
def unaccept_answer(cursor, answer_id):
    cursor.execute('''
            UPDATE answer
            SET accepted = FALSE 
            WHERE id = %(answer_id)s
            ''', {'answer_id':answer_id})


@connection.connection_handler
def unaccept_reputation(cursor, answer_id):
    cursor.execute('''
            UPDATE users
            SET reputation = reputation - 15
            FROM answer
            WHERE answer.id = %(answer_id)s AND answer.user_id = users.id
            ''', {'answer_id': answer_id})


@connection.connection_handler
def get_question_user(cursor, question_id):
    cursor.execute('''
            SELECT users.username
            FROM users
            INNER JOIN question ON question.user_id = users.id
            WHERE question.id = %(question_id)s AND question.user_id = users.id
            ''', {'question_id':question_id})
    return cursor.fetchone()

