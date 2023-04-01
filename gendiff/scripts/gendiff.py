#!/usr/bin/python3
import argparse
# import diff

# print(diff.a)

# file_path1 = '/home/larriva/python-project-50/file1.json'
# file_path2 = '/home/larriva/python-project-50/file2.json'
# compare_diff = diff.generate_diff(file_path1, file_path2)
# print(diff)

def main():
    parser = argparse.ArgumentParser(prog = 'gendiff',
                        description = 'Compares two configuration files and shows a difference.',
                        epilog = '')

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format',
                            default='stylish',
                            choices=['stylish', 'plain', 'json'],
                            help='set format of output')
    return parser.parse_args()
    # print(args)


if __name__ == '__main__':
    main()



