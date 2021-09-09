#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total_args = len(argv)
    result = 0
    for i in range(1, total_args):
        result += int(argv[i])
    print("{:d}".format(result))
