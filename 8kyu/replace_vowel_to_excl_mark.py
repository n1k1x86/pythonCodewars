def replace_exclamation(s):
    for i in s:
        if i.lower() in 'aeiou':
            s = s.replace(i,'!')
    return s