def knight_jump(knight, start, end):
        spaces = []
        for i in range(0, len(start)):
                spaces.append(abs(start[i] - end[i]))
        if set(knight) == set(spaces):
                return True
        return False
