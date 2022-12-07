from math import sqrt
def sum_of_two_squares(n):
    sq = int(sqrt(n))
    for i in range(sq, 0, -1):
        x = n - i ** 2
        if (int(sqrt(x))) ** 2 == x and int(sqrt(x)) > 0:
            return i, int(sqrt(x))