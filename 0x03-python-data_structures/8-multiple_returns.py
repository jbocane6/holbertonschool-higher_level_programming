#!/usr/bin/python3
def multiple_returns(sentence):
    return tuple([0,None]) if (sentence is None) else tuple([len(sentence), sentence[0]])
