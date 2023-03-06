def Xbonacci(signature,n):
    for i in range(n):
        signature.append(sum(signature[i:]))
    return signature[:n]
