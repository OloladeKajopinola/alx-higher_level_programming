#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if not sentence:
        return (0, None)  # Return a tuple with length 0 and None for the first character
    
    # Get the length of the sentence and the first character
    length = len(sentence)
    first_char = sentence[0]
    
    return (length, first_char)
