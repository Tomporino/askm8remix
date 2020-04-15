import data_handler


def check_tag(tag, tags):
    if tag in tags:
        return False
    return True


def check_password(password, confirm_password):
    if password == confirm_password:
        return True
    return False


def check_registration(user_data):
    in_use = data_handler.get_users()
    if user_data['username'] in [user['username'] for user in in_use]:
        return False
    elif user_data['email'] in [user['email'] for user in in_use]:
        return False
    return True
