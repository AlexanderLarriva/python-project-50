#!/usr/bin/python3
import gendiff
# так тоже можно
# from gendiff import parse
# from gendiff import generate_diff


def main():
    # Проверка импорта
    # print(gendiff.diff_files.a)
    # вызов параметров файла
    args = gendiff.parse()
    first_file = args.first_file
    second_file = args.second_file
    #format = args.format
    compare_diff = gendiff.generate_diff(first_file, second_file)
    print(compare_diff)


if __name__ == '__main__':
    main()
