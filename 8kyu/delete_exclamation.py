def remove(s):
    if s == '':
        return ''
    return s[:-1] if s[-1] == '!' else s