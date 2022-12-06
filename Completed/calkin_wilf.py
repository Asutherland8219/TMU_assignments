# Calkin Wilf Sequence
from fractions import Fraction as f
from collections import deque as d

def calkin_wilf(n):
    a = 1
    first = f(1, 1)
    seq = d()
    seq.append(first)

    while a<n:
        for i in range(len(seq)):
            fraction = seq.popleft()
            num = fraction.numerator
            den = fraction.denominator

            frac_answer = f(num, num + den)
            seq.append(frac_answer)
            a += 1
            if a == n:
                return seq[-1]

            frac_answer = f(num + den, den)
            seq.append(frac_answer)
            a += 1
            if a == n:
                return seq[-1]
                
    return -1