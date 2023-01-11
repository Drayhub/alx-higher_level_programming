import sys

# Create a dictionary to store the number of lines for each status code
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

# Create a variable to store the total file size
total_size = 0

# Create a counter to keep track of the number of lines read
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

        # Split the line into its components
        ip, date, request, status, size = line.strip().split(" ")

        # Increment the count for this status code
        status_codes[int(status)] += 1

        # Add the size to the total size
        total_size += int(size)

        # If we have read 10 lines, print the metrics and reset the counter
        if line_count % 10 == 0:
            print("Total file size:", total_size)
            for status_code in sorted(status_codes.keys()):
                if status_codes[status_code] > 0:
                    print("{}: {}".format(status_code, status_codes[status_code]))
            line_count = 0
except KeyboardInterrupt:
    print("\nTotal file size:", total_size)
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))
