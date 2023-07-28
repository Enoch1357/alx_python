#! /usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if sentence == "":
        first = "None"
    return length, first