from datetime import datetime


def get_date_today():
    today = datetime.today().date()
    return today.strftime('%d.%m.%Y')


def main():
    print(get_date_today())


if __name__ == '__main__':
    main()
