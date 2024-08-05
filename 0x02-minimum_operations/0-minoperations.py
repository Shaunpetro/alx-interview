#!/usr/bin/python3
'''min operations challenge for python3'''


def minOperations(n):
    """calculates the fewest no of
    operations need to result with
    exact n H chars in file

    returns:
        Integer : if n is impossible to achieve, return 0
    """
    pasted_chars = 1 # how many chars in the file
    clipboard = 0 # how many H's copied
    counter = 0 # operations counter
    
    while pasted_chars < n:
        # if did not copy anything yet
        if clipboard == 0:
            # copyall
            clipboard = pasted_chars
            # increment operations counter
            counter += 1
            
        # if haven't pasted anything yet
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            # increment operation counter
            counter += 1
            # continue to next loop
            continue
        
        remaining = n - pasted_chars # remaining chars to paste
        # check if impossible by checking if clipboard
        # has more than needed to reach the desired no
        # which also means no of chars in file =
        # or more than in clipboard.
        # in both situations its impossible to achieve n chars
        if remaining < clipboard:
            return 0
        
        # if can't be divided
        if remaining % pasted_chars != 0:
            # pasre current clipboard
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
        else:
            # copyall
            clipboard = pasted_chars
            # paste
            pasted_chars += clipboard
            # increment operations counter
            counter += 2
            
    # if got the desired result
    if pasted_chars == n:
        return counter
    else:
        return 0
