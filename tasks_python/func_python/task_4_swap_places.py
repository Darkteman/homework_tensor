def swap_places(array):
    max_item, index_max_item = array[0], 0
    min_item, index_min_item = array[0], 0
    for i in range(len(array)):
        if array[i] > max_item:
            max_item, index_max_item = array[i], i
        if array[i] < min_item:
            min_item, index_min_item = array[i], i
    array[index_max_item], array[index_min_item] = array[index_min_item],  array[index_max_item]
    return array


def main():
    array = [99, 2, 78, 4, 85, 1, 56, 7]
    print(swap_places(array))


if __name__ == '__main__':
    main()
