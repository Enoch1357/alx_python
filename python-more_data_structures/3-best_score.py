#! /usr/bin/python3
def best_score(a_dictionary):
    try:
        max_value_key = max(a_dictionary, key=a_dictionary.get)
    except (AttributeError, ValueError):
        max_value_key = None
    return max_value_key