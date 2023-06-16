import os


def create_folder(new_dir):
    base_dir = os.getcwd()
    path = os.path.join(base_dir, new_dir)
    os.mkdir(path)


def main():
    new_dir = 'new_folder'
    create_folder(new_dir)


if __name__ == '__main__':
    main()
