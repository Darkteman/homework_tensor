from datetime import datetime
from calendar import monthrange


def get_first_day_month():
    today = datetime.today()
    number_last_day = monthrange(today.year, today.month)[1]
    last_day = today.replace(day=number_last_day)
    return last_day.strftime('%d.%m.%y')


def main():
    print(get_first_day_month())


if __name__ == '__main__':
    main()
