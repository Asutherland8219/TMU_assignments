def arithmetic_progression(elems):
    len_ele = len(elems)
    if len_ele == 1:
        return (elems[0], 0, 1)
    if len_ele == 2:
        return (elems[0], elems[1] - elems[0], 2)
    then = [[0 for x in range(len_ele)] for y in range(len_ele)]
    for a in range(len_ele - 1):
        then[a][len_ele - 1] = 2
    for b in range(len_ele - 2, 0, -1):
        a = b - 1
        c = b + 1
        while (a >= 0 and c <= len_ele - 1):
            if (elems[a] + elems[c] < 2 * elems[b]):
                c += 1
            elif (elems[a] + elems[c] > 2 * elems[b]):
                then[a][b] = 2
                a -= 1
            else:
                then[a][b] = then[b][c] + 1
                a -= 1
                c += 1
        while (a >= 0):
            then[a][b] = 2
            a -= 1
    lap = 0
    max_1 = 0
    max_2 = 0
    for a in range(len_ele):
        for b in range(len_ele):
            if then[a][b] > lap:
                lap = then[a][b]
                max_1 = a
                max_2 = b

    return (elems[max_1], elems[max_2] - elems[max_1], lap)