import collections
def frequency_sort(elems):
    counter = len(elems)
    fin = sorted(elems,key=lambda x: (counter [x],-x),reverse=True)
    return (fin)