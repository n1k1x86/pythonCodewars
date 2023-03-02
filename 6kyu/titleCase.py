def title_case(title, minor_words=''):
    if title == '':
        return ''
    minor_words = minor_words.lower().split()
    title_words = title.lower().split()
    title_words[0] = title_words[0].capitalize()

    for i in range(1,len(title_words)):
        title_words[i] = title_words[i].lower() if title_words[i] in minor_words else title_words[i].capitalize()
        
    return ' '.join(title_words)