
def count_dominators(items):
    empty_list = []
    inversed = items[::-1]
    for i in range(len(inversed)):
        if i == 0:
            empty_list.append(items[-1])
        if inversed[i] > empty_list[-1]:
            empty_list.append(inversed[i])
    return len(empty_list)