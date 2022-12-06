def only_odd_digits(n):
    
    x = list(map(int, str(x)))
    result = all(y%2 == 1 for y in x)
    return(result)