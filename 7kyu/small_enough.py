def small_enough(array, limit):
    res = all(map(lambda x: x <= limit, array))
    return res