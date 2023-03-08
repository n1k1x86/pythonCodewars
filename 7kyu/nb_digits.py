def nb_digit(n: int, d: int):
    return ''.join([str(i**2) for i in range(0,n+1)]).count(str(d))
