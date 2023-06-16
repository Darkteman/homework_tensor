import os


def connect_path_folder_file(path_folder, path_file):
    return os.path.join(path_folder, path_file)


def main():
    path_folder = r'C:\Saby\ProjectTest\tasks_python\os_module'
    path_file = 'simple_file.py'
    print(connect_path_folder_file(path_folder, path_file))


if __name__ == '__main__':
    main()
