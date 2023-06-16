from datetime import datetime


def get_first_day_month():
    first_day = datetime.today().replace(day=1)
    return first_day.strftime('%d.%m.%y')


def main():
    print(get_first_day_month())


if __name__ == '__main__':
    main()
