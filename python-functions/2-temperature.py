def convert_to_celsius(fahrenheit):
    if fahrenheit == -459.67:
        return round(5/9 * (fahrenheit - 32), 2)
    else:
        return 5/9 * (fahrenheit - 32)
