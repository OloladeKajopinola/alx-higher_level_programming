#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Exclude the script name itself and convert arguments to integers
    args = sys.argv[1:]
    args = [int(arg) for arg in args]

    # Calculate the sum of all integer arguments
    result = sum(args)

    # Print the result
    print(result)

