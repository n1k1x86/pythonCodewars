def multiple_of_index(arr):
    res = []
    for ind, el in enumerate(arr,0):
        try:
            if el % ind == 0:
                res.append(el)
        except:
            continue
    return res