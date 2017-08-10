#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        return None
    else:
        return length, sentence[0]
