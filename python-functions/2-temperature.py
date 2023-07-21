def convert_to_celsius(fahrenheit):
    if fahrenheit == -459.67:
        return round(5/9 * (fahrenheit - 32), 2)
    else:
        return 5/9 * (fahrenheit - 32)
print(convert_to_celsius(100))
