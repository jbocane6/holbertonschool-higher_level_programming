#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    params = len(argv)

    if params != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    op = argv[2]

    def other():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    def add1():
        result = add(num1, num2)
        print("{:d} + {:d} = {:d}".format(num1, num2, result))
        return result

    def sub1():
        result = sub(num1, num2)
        print("{:d} - {:d} = {:d}".format(num1, num2, result))
        return result

    def mul1():
        result = mul(num1, num2)
        print("{:d} * {:d} = {:d}".format(num1, num2, result))
        return result

    def div1():
        result = div(num1, num2)
        print("{:d} / {:d} = {:d}".format(num1, num2, result))
        return result

    options = {
        "+": add1,
        "-": sub1,
        "*": mul1,
        "/": div1
    }
    options.get(op, other)()
