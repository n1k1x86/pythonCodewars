import re

def get_number_from_string(string):
    pattern = '[0-9]+'
    res = re.findall(pattern, string)
    return int(''.join(res))