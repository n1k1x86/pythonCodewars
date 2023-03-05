from collections import Counter

def stray(arr):
    return min(Counter(arr), key=Counter(arr).get)