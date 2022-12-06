def expand_intervals(intervals):
    result = []
    for i in intervals.split(','):
        if '-' not in i:
            result.append(int(i))
        else:
            x,y = map(int, i.split('-'))
            result += range(x,y+1)
    return result