def candy_share(candies):
    n = len(candies) 
    index = 0  
    while True:  
        if not any(i >= 2 for i in candies): 
            return index  
        index += 1
        new_candies = [0] * n
        for x in range(n):
            if candies[x] >= 2:  
                candies[x] -= 2  
                if x == n - 1:  
                    new_candies[x - 1] += 1  
                    new_candies[0] += 1  
                else:
                    new_candies[x - 1] += 1  
                    new_candies[x + 1] += 1  
            new_candies[x] += candies[x]  
        candies = new_candies  