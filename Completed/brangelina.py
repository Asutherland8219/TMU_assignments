def brangelina(first, second):
    firstv, temp = [],[]
    for ind, letter in enumerate(first):
        if letter in ('a', 'e', 'i', 'o', 'u'):
            temp.append(ind)
        else:
            if len(temp) > 0:
                firstv.append(temp)
                temp = []
    if len(temp) > 0:
                firstv.append(temp)
                temp = []
    if len(firstv) > 2:
        firstv = firstv[:-1]
        first = first[:int(firstv[-1][0])]
    else:
        first = first[:int(firstv[0][0])]
    
    while second[0] not in ('a', 'e', 'i', 'o', 'u'):
        second = second[1:]
            
    return first + second