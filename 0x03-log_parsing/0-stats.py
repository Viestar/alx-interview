#!/usr/bin/python3
"""
Module documentation for a script that reads stdin line by line
and computes metrics:
"""
import sys


file_size = 0

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_metrics():
    """prints THE STATUS CODE logs """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    counter = 0
    try:
        for line in sys.stdin:
            try:
                elements = line.split()
                file_size += int(elements[-1])
                if elements[-2] in status_codes:
                    status_codes[elements[-2]] += 1
            except Exception:
                pass
            if counter == 9:
                print_metrics()
                counter = -1
            counter += 1
    except KeyboardInterrupt:
        print_metrics()
        raise
    print_metrics()
