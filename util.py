from datetime import datetime
import data_handler


def get_current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
