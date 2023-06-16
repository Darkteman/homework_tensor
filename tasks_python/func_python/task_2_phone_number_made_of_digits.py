def is_phone_number(line):
    base_line = line
    if line[0] == '+':
        line = line[1:]
    skip_simbols = '- '
    for item in line:
        if item in skip_simbols or item.isdigit():
            continue
        return f'error: Номер телефона {base_line} сформирован неверно!'
    return f'success: Номер телефона {base_line} состоит из цифр.'


def main():
    numbers_tuple = (
        '+7 999-555-11-11',
        '8-999-777-1111',
        '+7 999 333 2222'
    )
    [print(is_phone_number(number)) for number in numbers_tuple]


if __name__ == '__main__':
    main()
