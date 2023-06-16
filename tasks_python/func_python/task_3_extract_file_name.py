from os import path

def extract_file_name(line):
    full_name = path.basename(line)
    name = path.splitext(full_name)[0]
    return name


def main():
    line = r'C:\development\inside\test-project_management\inside\myfile.txt'
    print(extract_file_name(line))


if __name__ == '__main__':
    main()
