
def expand_intervals(intervals):
    result = []
    for i in intervals.split(','):
        if i == '':
            continue
        if '-' not in i:
            result.append(int(i))
        else:
            l,h = map(int, i.split('-'))
            result+= range(l,h+1)
    return str(result)