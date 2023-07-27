#! /usr/bin/python3
def safe_print_division(a, b):
    try:
        quotient = int(a) / int(b)
        result = quotient
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
    except ZeroDivisionError:
        result = "None"
        print("Inside result: {}".format(result))
        print("{:d} / {:d} = {}".format(a, b, result))
    finally:
        return ("\n")