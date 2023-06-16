from datetime import datetime


def change_month(line, number_months):
    date_input = datetime.strptime(line, '%d.%m.%y')
    month, year = date_input.month, date_input.year
    increased_number_months = month + number_months
    number_year = increased_number_months // 12
    number_month = increased_number_months % 12
    if number_month == 0:
        desired_date = date_input.replace(month=12, year=(year + number_year - 1))
    else:
        desired_date = date_input.replace(month=number_month, year=(year + number_year))
    return desired_date.strftime('%d.%m.%y')


def main():
    line = '01.11.10'
    number_months = -5
    print(change_month(line, number_months))


if __name__ == '__main__':
    main()
