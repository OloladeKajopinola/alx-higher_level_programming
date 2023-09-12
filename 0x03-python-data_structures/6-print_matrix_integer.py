#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    for row in matrix:
        for num in row:
            # Use str.format() to print integers without casting them to strings
            print("{:d}".format(num), end=" ")
        print()  # Print a newline after each row
