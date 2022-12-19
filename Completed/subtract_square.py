def subtract_square(queries):
    result = []
    state = [False]
    for x in range(1, queries[len(queries) - 1] + 1):  
        y = 1
        while True:
            if x - y * y < 0:
                state.append(False)
                break
            if not state[x - y * y]:
                state.append(True)
                break
            else:
                y += 1
    for x in range(0, len(queries)):  
        result.append(state[queries[x]])
    return result