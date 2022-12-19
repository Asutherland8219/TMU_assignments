
def bulgarian_solitaire(piles, k):
    index = 0
    total_sum = int(k*(k+1)//2)
    check_list = list(range(1, k+1))
    piles = [i for i in piles if i != 0]
    while True:
        if all(x in piles for x in check_list): break
        else:
            piles = [x - 1 for x in piles]
            piles = [i for i in piles if i != 0]
            appended_value = total_sum - sum(piles)
            piles.append(appended_value)
            index +=1    
    return index
