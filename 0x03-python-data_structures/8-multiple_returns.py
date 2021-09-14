#!/usr/bin/python3
def multiple_returns(sentence):
    return tuple([len(sentence), sentence[0]]) if (len(sentence) > 0) else tuple([0,None])
"""remember: you have to use a list and convert to tupple before returning
   Is only used 1 return(at the beggining of the ternary operator"""
