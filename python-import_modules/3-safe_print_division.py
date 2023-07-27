#! /usr/bin/python3
__name__ = "__main__"
def safe_print_division(a, b):
    try:
        quotient = int(a) / int(b)
        print("Inside result: {}".format(quotient))
        
    except ZeroDivisionError: 
        quotient = "None"
        print("Inside result: {}".format(quotient))
    
    finally:
        return (quotient)