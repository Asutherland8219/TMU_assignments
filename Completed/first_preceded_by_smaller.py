def first_preceded_by_smaller(items, k=1):
    
    for i in range(len(items)):
        if sorted(items[0:i+1]).index(items[i]) >= k:
            return items[i]
    return None