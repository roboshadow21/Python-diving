from datetime import datetime


def check_date(date_to_check: str) -> bool:
    date_format = "%d.%m.%Y"
    try:
        bool(datetime.strptime(date_to_check, date_format))
        return True
    except ValueError:

        return False


if __name__ == '__main__':
    date = input("Enter date to check for, format DD.MM.YYYY: ")
    print(check_date(date))