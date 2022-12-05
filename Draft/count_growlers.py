def count_growlers(items):
    dominators = 0
    for index,item in enumerate(items):
        dominator = True
        for right_item in items[index + 1:]:
            if item <= right_item:
                dominator = False
                break
        if dominator:
            dominators = dominators + 1        
    return dominators