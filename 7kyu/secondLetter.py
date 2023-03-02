def second_symbol(s, symbol):
    count = 0
    for i, elem in enumerate(s):
        if elem == symbol:
            count += 1
        if count == 2:
            return i
    return -1
