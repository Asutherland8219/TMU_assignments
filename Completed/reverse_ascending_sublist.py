
def reverse_ascending_sublists(items):
    
    index = 0

    for i, item in enumerate(items):
        if i + 1 >= len(items) or item >= items[i + 1]:
            items[index:i + 1] = items[index:i + 1][::-1]
            index = i + 1

    return items