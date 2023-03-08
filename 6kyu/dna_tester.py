def check_DNA(seq1, seq2):
    print(seq1)
    print(seq2)
    d = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    if len(seq1) <= len(seq2):
        print('seq2 >= seq1')
        seq1_reb = ''.join([d.get(i) for i in seq1])
        return True if seq2[::-1].find(seq1_reb) != -1 else False
    else:
        print('seq1 > seq2')
        seq2_reb = ''.join([d.get(i) for i in seq2[::-1]])
        return True if seq1.find(seq2_reb) != -1 else False
