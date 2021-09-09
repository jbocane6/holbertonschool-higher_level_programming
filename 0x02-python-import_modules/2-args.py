#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    countArgs = len(sys.argv[1:])
    argument = "arguments:"
    if countArgs == 0:
        argument = argument[:-1] + "."
    elif countArgs == 1:
        argument = argument[:-2] + ":"
    print("{:d} {}".format(countArgs, argument))

    increment = 1
    for arg in sys.argv[1:]:
        print("{:d}: {}".format(increment, arg))
        increment += 1
