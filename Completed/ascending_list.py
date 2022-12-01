# Determine whehter the sequency of items is strictly ascending 

import numbers


items = [1,2,2]

def is_ascending(items):
    # last = list[0]

    # for value in list:
    #     if value < last:
    #         return False
    #     previous = value 
    
    # return True 

    for x in range(len(items) - 1):
        if items[x] >= items[x + 1]:
            return False
    return True