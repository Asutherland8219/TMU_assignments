import math
import math
from statistics import median 

def tukeys_ninthers(items):
    iter = int(math.log(len(items), 3))
    arr = items
    working_arr = []
    for i in range(iter):
        for j in range(0, len(arr), 3):
            working_arr.append(median([ arr[j], arr[j+1] , arr[j+2] ]))
        arr = working_arr
        working_arr = []
    return median(arr)