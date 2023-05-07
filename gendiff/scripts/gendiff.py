#!/usr/bin/python3
import gendiff


def main():
    args = gendiff.parse()
    first_file = args.first_file
    second_file = args.second_file
    format = args.format
    diff = gendiff.generate_diff(first_file, second_file, format)
    print(diff)


if __name__ == '__main__':
    main()
