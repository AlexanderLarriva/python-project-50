#!/usr/bin/python3
from gendiff.cli import parse_args
from gendiff.build_diff import generate_diff


def main():
    args = parse_args()
    first_file = args.first_file
    second_file = args.second_file
    format = args.format
    diff = generate_diff(first_file, second_file, format)
    print(diff)


if __name__ == '__main__':
    main()
