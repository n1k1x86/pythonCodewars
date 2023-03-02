alphabet = {
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5'
}

rev_alphabet = {
    '1': 'a',
    '2': 'e',
    '3': 'i',
    '4': 'o',
    '5': 'u'
}

def encode(st):
    for i in st:
        if i in alphabet:
            st = st.replace(i, alphabet.get(i))
    return st
    
def decode(st):
    for i in st:
        if i in rev_alphabet:
            st = st.replace(i, rev_alphabet.get(i))
    return st
