def top_two(array):
    prices_array = []
    for i in range(len(array)):
        prices_array.append((array[i]["цена"], i))
    prices_array = sorted(prices_array, reverse=True)
    return array[prices_array[0][1]], array[prices_array[1][1]]


def main():
    array = [
        {"наименование": "Спички", "цена": 1},
        {"наименование": "Молоко", "цена": 60},
        {"наименование": "Лук", "цена": 37},
        {"наименование": "Мороженоне", "цена": 150},
        {"наименование": "Жевательная резинка", "цена": 21}
    ]
    print(top_two(array))


if __name__ == '__main__':
    main()
