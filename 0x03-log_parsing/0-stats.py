#!/usr/bin/python3

"""A script for parsing HTTP request logs"""

import re


def extract_input(input_line):
    """Extracts sections of a line of an HTTP request log"""
    pattern = r'\S+ - \[(\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]' + \
        r' "GET /projects/260 HTTP/1.1" (\d+) (\d+)\s*'
    match = re.fullmatch(pattern, input_line)
    if match:
        return {'status_code': match.group(2),
                'file_size': int(match.group(3))}
    return None


def print_statistics(total_file_size, status_codes_stats):
    """Prints the accumulated statistics of the HTTP request log"""
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code, num in sorted(status_codes_stats.items()):
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    """Updates the metrics from a given HTTP request log"""
    line_info = extract_input(line)
    if line_info:
        status_codes_stats[line_info['status_code']] += 1
        total_file_size += line_info['file_size']
    return total_file_size


def run():
    """Starts the log parser"""
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line, total_file_size, status_codes_stats)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
