#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = len(sys.argv)
    s = "s" if n == 1 or n > 2 else ""
    p = ":" if n > 1 else "."

    print("{:d} argument{}{}".format(n - 1, s, p))
