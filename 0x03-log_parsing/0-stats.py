#!/usr/bin/python3
"""
Module documentation for a script that reads stdin line by line
and computes metrics:
"""
import sys


def print_statistics(total_size, status_codes):
    """ Prints status codes """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """ Returns parse lines """
    parts = line.split()
    if len(parts) >= 7 and parts[5].isdigit():
        return int(parts[5]), int(parts[6])
    return None


def main():
    """ Program entry point """
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            data = parse_line(line)
            if data:
                file_size, status_code = data
                total_size += file_size
                status_codes[status_code] = \
                    status_codes.get(status_code, 0) + 1

            if i % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        pass  # Handle keyboard interruption

    print_statistics(total_size, status_codes)


if __name__ == "__main__":
    main()
