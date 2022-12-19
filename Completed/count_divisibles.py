def count_divisibles_in_range(start, end, n):
    return (end - (start - n - start % n)) // n - 1 + (1 if start % n == 0 else 0)