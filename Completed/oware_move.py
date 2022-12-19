def oware_move(board, house):  # Entirely From Class
    s, n = board[house], len(board)
    pstn = house
    board[house] = 0
    while s > 0:
        index = 0
        for i in range(pstn + 1, len(board)):
            board[i] += 1
            index = i
            s -= 1
            if s == 0:
                break
        if s > 0:
            for i in range(house):
                board[i] += 1
                s -= 1
                if s == 0:
                    break
        else:
            while board[index] in [2, 3] and index >= n / 2:
                board[index] = 0
                index -= 1
    return board
