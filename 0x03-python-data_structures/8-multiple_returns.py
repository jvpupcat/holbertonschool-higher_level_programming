#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == '':
        return None
    else:
        for i in sentence:
            return length, sentence[0]