def balanced_centrifuge(n, k): 
    if n < 2:
        return False
    factors, div = [], 2
    num = n
    while num > 1:
        if num / div % 1:
            div += 1
        else:
            if not div in factors:
                factors.append(div)
            num /= div
    def validity_check(n, acc, factors, i):
        if acc == n:
            return True
        elif acc > n:
            return False
        else:
            for j in range(i, len(factors)):
                if validity_check(n, acc + factors[j], factors, j):
                    return True
            return False
    return validity_check(k, 0, factors, 0) and validity_check(n - k, 0, factors, 0)