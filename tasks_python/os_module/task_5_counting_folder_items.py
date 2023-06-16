import os


def get_counting_folder_items(path):
    count_folders = count_files = count_py = count_exe = 0
    for root, dirs, files in os.walk(path):
        count_folders += len(dirs)
        count_files += len(files)
        for file in files:
            if file.endswith('.py'):
                count_py += 1
            elif file.endswith('.exe'):
                count_exe += 1
    return count_folders, count_files, count_py, count_exe


def create_file_with_result(count_folders, count_files, count_py, count_exe):
    with open('result.txt', 'w+') as file:
        file.write(
            f'Количество папок: {count_folders}\n'
            f'Количество файлов с расширением .py: {count_py}\n'
            f'Количество файлов с расширением .exe: {count_exe}\n'
            f'Общее количество файлов: {count_files}'
        )


def main():
    path = r'C:\Python311'
    create_file_with_result(*get_counting_folder_items(path))


if __name__ == '__main__':
    main()
