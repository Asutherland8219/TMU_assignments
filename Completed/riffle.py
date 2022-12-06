
def riffle(lst, out=True):
    temp = []
    if len(lst) == 0:
        return lst
    if len(lst) % 2 == 0:
        mid = len(lst) // 2
        a, b = lst[0:mid], lst[mid:]
        if out == True:
            for i in range(0, len(a)):
                temp.append(a[i])
                temp.append(b[i])
        if out == False:
            for i in range(0, len(a)):
                temp.append(b[i])
                temp.append(a[i])
        return temp