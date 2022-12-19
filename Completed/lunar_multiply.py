def lunar_multiply(a, b):  # min function
    first, second = str(a)[::-1], str(b)[::-1]
    big_digit = []
    res= 0
    for x in range(len(second)):
        d = ''
        for y in range(len(first)):
            d += min(first[y], second[x])
        big_digit.append('0'*x+d)  
    for x in big_digit: 
        res = lunar_max(res, x[::-1])
    return res

def lunar_max(x, y):  
        first, second = str(x)[::-1], str(y)[::-1]
        sum = ''
        for i in range(max(len(first), len(second))):
            sum += max(first[i:i+1], second[i:i+1])
