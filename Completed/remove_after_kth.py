def remove_after_kth(items, k = 1):
    di = {}
    li = []
    for i in items:
        di[i] = di.get(i, 0) + 1
        if(di[i] <= k):
            li.append(i)
    return li