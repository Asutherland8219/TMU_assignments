def crag_score(dice):
    d = dict()
    low,high,odd,even = [1,2,3], [4,5,6], [1,3,5], [2,4,6]
    if sum(dice) == 13 and (dice[0] == dice[1] or dice[1] == dice[2] or dice[0] == dice[2]): 
        return 50
    elif sum(dice) == 13:
        return 26
    elif dice[0] == dice[1] == dice[2]:
        return 25
    elif all(x in dice for x in low) or all(x in dice for x in high) or all(x in dice for x in odd) or all(x in dice for x in even):
        return 20
    else:
        for die in dice:
            d[die] = d.get(die, 0) + 1
        x = [k*v for k,v in d.items()]
        return max(x)