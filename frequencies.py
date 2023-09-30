"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for x in items:
        s = str(x)
        if s in frequencies:
            frequencies[s] += 1
        else:
            frequencies[s] = 1
    return frequencies
