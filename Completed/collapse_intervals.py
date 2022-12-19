def collapse_intervals(items):
    if items:
        pre_num = min(items)
    else:
        None
    
    p_list = list()

    for number in sorted(items):
        if number != pre_num+1:
            p_list.append([number])
        elif len(p_list[-1]) > 1:
            p_list[-1][-1] = number
        else:
            p_list[-1].append(number)
        pre_num = number

    return ','.join(['-'.join(map(str,p)) for p in p_list])
