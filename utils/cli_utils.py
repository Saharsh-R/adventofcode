from datetime import datetime


def get_current_day_if_advent_else_1() -> int:
    today = datetime.today()
    if today.month != 12:
        return 1
    return today.day if 1 <= today.day <= 25 else 1


def get_current_year() -> int:
    return datetime.today().year
