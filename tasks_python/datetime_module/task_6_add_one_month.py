from calendar import monthrange
from datetime import datetime, timedelta


def add_one_month(line):
    date_input = datetime.strptime(line, '%d.%m.%y')
    days_in_month = monthrange(date_input.year, date_input.month)[1]
    date_in_one_month = date_input + timedelta(days=days_in_month)
    return date_in_one_month.strftime('%d.%m.%Y')


def main():
    line = '03.12.23'
    print(add_one_month(line))


if __name__ == '__main__':
    main()
