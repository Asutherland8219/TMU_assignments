def group_and_skip(n,out,ins):
    index=[]
    while n!=0:
        index.append(n%out)
        n=n//out
        n=n*ins
    return index
