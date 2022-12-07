


def count_dominators(items):
    index = 0
    for key,item in enumerate(items):
        dominator = True
        for right_item in items[key + 1:]:
            if item <= right_item:
                dominator = False
                break
        if dominator:
            index = index + 1        
    return index

