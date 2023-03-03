def stock_list(listOfArt, listOfCat):
    books_sum = []
    for i in listOfCat:
        temp = 0
        for j in listOfArt:
            if j[0] == i:
                temp += int(j[j.index(' '):])
        books_sum.append(f"({i} : {temp})")
    res = ' - '.join(books_sum)
    return res if res.count(': 0') != len(listOfCat) else ''