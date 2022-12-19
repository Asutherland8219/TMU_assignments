
def count_carries(a, b):
    a = str(a)
    b = str(b)
    carry = 0;
    count = 0;
    len_a = len(a);
    len_b = len(b);
 
    while (len_a != 0 or len_b != 0):
        x = 0;
        y = 0;
        if (len_a > 0):
            x = int(a[len_a - 1]) + int('0');
            len_a -= 1;
         
        if (len_b > 0):
            y = int(b[len_b - 1]) + int('0');
            len_b -= 1;

        sum = x + y + carry;
        if (sum >= 10):
            carry = 1;
            count += 1;
        else:
            carry = 0;
    return count;