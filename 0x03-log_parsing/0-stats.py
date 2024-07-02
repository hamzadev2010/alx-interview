#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys

def print_metrics(total_size, code_counts):
    """Display matrix"""
    print("File size: {}".format(total_size))
    for code in sorted(code_counts):
        print("{}: {}".format(code, code_counts[code]))

if __name__ == "__main__":
    total_size = 0
    code_counts = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break

            if line_count == 10:
                print_metrics(total_size, code_counts)
                line_count = 1
            else:
                line_count += 1

            parts = line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in valid_codes:
                    if parts[-2] not in code_counts:
                        code_counts[parts[-2]] = 1
                    else:
                        code_counts[parts[-2]] += 1
            except IndexError:
                pass

        print_metrics(total_size, code_counts)

    except KeyboardInterrupt:
        print_metrics(total_size, code_counts)
        raise

