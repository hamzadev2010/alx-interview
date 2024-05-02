#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics"""

import sys
import re

def is_log_format_valid(log_string):
    regex_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "GET \/projects\/260 HTTP\/1\.1" \d{3} \d+'
    return re.match(regex_pattern, log_string)

def print_statistics(sorted_keys_dict, total_size):
    """
    function to print
    the values to standard output
    """
    print("Total File Size:", total_size)
    for status_code, count in sorted_keys_dict.items():
        if count:
            print("{}: {}".format(status_code, count))

def read_and_analyze_logs():
    while True:
        try:
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
            total_size = 0
            for line_count in range(11):
                log_info = sys.stdin.readline().strip()
                if is_log_format_valid(log_info):
                    log_info_list = log_info.split(" ")
                    file_size = log_info_list[-1]
                    status_code = log_info_list[-2]
                    status_codes[status_code] = status_codes.get(status_code, 0) + 1
                    total_size += int(file_size)
                    sorted_keys_dict = {code: status_codes[code] for code in sorted(status_codes) if status_codes[code] != 0}
                if line_count % 10 == 0:
                    print_statistics(sorted_keys_dict, total_size)
            print_statistics(sorted_keys_dict, total_size)
        except KeyboardInterrupt:
            print_statistics(sorted_keys_dict, total_size)
            raise

if __name__ == '__main__':
    read_and_analyze_logs()
