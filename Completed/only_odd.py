def only_odd_digits(n):
    index = str(n)
    count=0
    for x in range (len(index)):
        num=int(index[x])
        if num%2!=0:
            count+=1

    return count==len(index)