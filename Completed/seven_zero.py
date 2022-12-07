def seven_zero(n):
    d = 1
    ans = 0
    while True:
        if n%2 == 0 or n%5 == 0:
            k = 1
            while k <= d:
                val = int(k * '7' + (d-k) * '0')
                if val%n == 0:
                    ans = val
                    break
                k += 1
        else:
            val = int(d * '7')
            ans = val if val%n == 0 else 0 
        d += 1
        if ans > 0:
            return ans
            
