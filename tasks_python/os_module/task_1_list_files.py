import os


def get_list_files_in_folder(path):
    list_files = []
    for root, dirs, files in os.walk(path):
        list_files.extend(files)
    print(f'Количество найденных файлов: {len(list_files)}')
    return list_files


def main():
    path = r'C:\Saby\ProjectTest\tasks_python'
    print(get_list_files_in_folder(path))


if __name__ == '__main__':
    main()
