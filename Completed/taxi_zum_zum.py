def taxi_zum_zum(moves):
    dir = [1, 0, 0, 0]
    result = [0, 0]
    for i in range(len(moves)):
        if moves[i] == 'L':
            if dir.index(1) == 0:
                dir[0] = 0
                dir[3] = 1
            else:
                one_index = dir.index(1)
                dir[one_index - 1] = 1
                dir[one_index] = 0

        if moves[i] == 'R':
            if dir.index(1) == 3:
                dir[0] = 1
                dir[3] = 0
            else:
                one_index = dir.index(1)
                dir[one_index + 1] = 1
                dir[one_index] = 0

        if moves[i] == 'F':
            if dir.index(1) == 0: result[1] += 1
            elif dir.index(1) == 1: result[0] += 1
            elif dir.index(1) == 2: result[1] -= 1
            else: result[0] -= 1
    return (result,)