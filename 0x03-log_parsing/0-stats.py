#!/usr/bin/python3
"""log parsing script into another file"""

import sys
import signal


total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    """Prints the total file size and the number of
    occurrences of each status code.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


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

            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_statistics()

        except (ValueError, IndexError):
            continue

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
