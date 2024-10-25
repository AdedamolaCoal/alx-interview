#!/usr/bin/python3
"""log parsing script into another file"""

import sys
import signal


STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]
LINE_COUNT_THRESHOLD = 10

total_file_size = 0
status_code_counts = {code: 0 for code in STATUS_CODES}
line_count = 0


def print_statistics():
    """Prints the total file size and the number of
    occurrences of each status code.
    """
    try:
        print(f"File size: {total_file_size}")
        for code in sorted(status_code_counts.keys()):
            if status_code_counts[code] > 0:
                print(f"{code}: {status_code_counts[code]}")
    except Exception as e:
        print(f"Error printing statistics: {e}")


def handle_interrupt(signal, frame):
    """Handles the keyboard interrupt (CTRL + C)
    to print the stats before exiting.
    """
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue
            ip_address = parts[0]
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_file_size += file_size
            if status_code in STATUS_CODES:
                status_code_counts[status_code] += 1
            line_count += 1
            if line_count % LINE_COUNT_THRESHOLD == 0:
                print_statistics()
        except (ValueError, IndexError) as e:
            print(f"Error parsing log line: {e}")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
