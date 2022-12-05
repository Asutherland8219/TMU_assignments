def duplicate_digit_bonus(n):
    digit = str(n)
    index = 0
    result = 1
    d = digit[0]
    for i in range(1,len(digit)):
        if d == digit[i]:
            result += 1
            if i+1 == len(digit):
                index += 2 * 10**(result-2)
        else:
            if result >=2:
                index += 10**(result-2)
            result = 1
        d = digit[i]
    return index