
def josephus(n, k):
    ls = list(range(1,n+1))
    k -= 1 
    idx = k
    kll =[]
    while len(ls) >= 1:
        kll.append(ls.pop(idx)) 
        idx = (idx + k) % len(ls)
    return(kll+ls)