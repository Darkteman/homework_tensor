def count_lucky_tickets():
    count_lucky = 0
    for i in range(1000000):
        line = str(i).zfill(6)
        first_half = [int(i) for i in line[:3]]
        second_half = [int(i) for i in line[3:]]
        if sum(first_half) == sum(second_half):
            count_lucky += 1
    return count_lucky


def main():
    print(count_lucky_tickets())


if __name__ == '__main__':
    main()
