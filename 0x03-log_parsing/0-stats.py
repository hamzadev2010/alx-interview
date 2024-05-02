#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics:"""

import sys

def display_statistics(status_stats: dict, total_size: int) -> None:
    print("Total File Size: {:d}".format(total_size))
    for status_code, count in sorted(status_stats.items()):
        if count:
            print("{}: {}".format(status_code, count))

def parse_input_lines(input_lines: iter) -> None:
    total_size, line_count = 0, 0
    status_stats = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        line = input_lines.readline()
        while line:
            line_count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in status_stats:
                    status_stats[status_code] += 1
            except IndexError:
                pass
            try:
                total_size += int(data[-1])
            except ValueError:
                pass
            if line_count % 10 == 0:
                display_statistics(status_stats, total_size)
            line = input_lines.readline()
        display_statistics(status_stats, total_size)
    except KeyboardInterrupt:
        display_statistics(status_stats, total_size)
        raise

if __name__ == '__main__':
    parse_input_lines(sys.stdin)
