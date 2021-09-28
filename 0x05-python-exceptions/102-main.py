#!/usr/bin/python3
import dis
safe_function = __import__('102-magic_calculation').magic_calculation

print("{}".format(dis.dis(safe_function)))