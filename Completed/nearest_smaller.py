def nearest_smaller(items):
    n, result = len(items), []
    for (i, e) in enumerate(items):
        j = 1
        while j < n:
            left = items[i - j] if i >= j else e
            right = items[i + j] if i+j < n else e
            if left < e or right < e:
                result.append(left if left < right else right)
                break
            j += 1
        else:
            result.append(e)
    return result