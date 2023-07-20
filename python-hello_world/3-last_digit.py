#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
length = len(number_str)
last_digit_str = str(number_str[length - 1])
last_digit = int(last_digit_str)
if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit))
if last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
if last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0\n".format(number, last_digit))