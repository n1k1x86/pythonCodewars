def multiplication_table(size: int):
    res = []
    count = 1
    while count <= size:
        res.append([i for i in range(count,size*count+1,count)])
        count+=1
    return res

