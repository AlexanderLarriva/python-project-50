#!/usr/bin/python3
import gendiff


def main():
    # print(gendiff.diff_files.a) Проверка импорта 
    # gendiff.generate_diff()
    # print(gendiff.a)
    args = gendiff.parse() #вызов параметров файла
    first_file = args.first_file
    # print('Path1=', first_file)
    second_file = args.second_file
    # print('Path2=', second_file)
    #format = args.format формат 
    # print('format=', format)
    compare_diff = gendiff.generate_diff(first_file, second_file)
    print(compare_diff)
    # print(gendiff.generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
