def eliminate_neighbours(items):
    if len(items) == 1:  
        return 1
    og_len = len(items)
    index = 0
    for i in range(1, len(items) + 1):
        if i in items:
            index += 1
            if len(items) == 1:
                items.pop(0)
                break
            center = items.index(i)
            left = center - 1
            if left < 0 or ((center + 1) < len(items) and items[center + 1] > items[left]):
                left = center + 1
            value = items[left]
            if center > left:
                center = left
            items.pop(center)
            items.pop(center)
            if value == og_len:
                break
    return index