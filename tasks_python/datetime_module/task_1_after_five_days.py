from datetime import datetime, timedelta


def get_date_in_five_day():
    today = datetime.today().date()
    after_five_day = today + timedelta(days=5)
    return after_five_day.strftime('%d.%m.%y')


def main():
    print(get_date_in_five_day())


if __name__ == '__main__':
    main()
