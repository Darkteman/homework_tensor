def remote_a(line):
    return line.replace('a', ''), line.count('a')


def main():
    line = 'afkfearo ao doek aaeoa feo'
    print(remote_a(line))


if __name__ == '__main__':
    main()
