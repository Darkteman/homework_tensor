from datetime import datetime, timedelta


def add_ten_days(line):
    date_time_obj = datetime.strptime(line, '%d.%m.%y')
    date_in_ten_days = date_time_obj + timedelta(days=10)
    return date_in_ten_days.strftime('%d.%m.%Y')


def main():
    line = '03.05.13'
    print(add_ten_days(line))


if __name__ == '__main__':
    main()
