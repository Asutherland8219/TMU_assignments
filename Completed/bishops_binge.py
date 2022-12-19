from operator import index
from re import X


def safe_squares_bishops(n, bishops):
    index = 0
    for row in range(n):
        for col in range(n):
            x = True
            for pos in bishops:
                if abs(row - pos[0]) == abs(col - pos[1]):
                    x = False
                    break
            if x:index += 1
    return index