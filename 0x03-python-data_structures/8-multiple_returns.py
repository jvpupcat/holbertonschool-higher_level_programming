#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        No = "None"
        return (No)
    else:
        return length, sentence[0]
