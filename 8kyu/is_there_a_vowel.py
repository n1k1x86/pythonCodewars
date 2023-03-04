def is_vow(inp):
    for i in range(len(inp)):
        if chr(inp[i]) in 'aeiou':
            inp[i] = chr(inp[i])
    return inp