def count_red_beads(n: int):
    count = 0
    while n > 0:
        if n == 1:
            return count
        else:
            count += 2
            n -= 1
    return count
