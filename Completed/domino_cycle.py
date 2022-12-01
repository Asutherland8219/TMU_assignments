### Match the 2nd value of the pair with the 2nd item in the 2nd pair

def domino_cycle(tiles):
    index = 0
    if len(tiles) is 0:
      return True
  
    if len(tiles) == 1:
        return tiles[0][0] == tiles[0][1]
            
    else:
        while index <= (len(tiles) - 1):
            if (tiles[index][1] == tiles[index+1][0]):
                index += 1
            
            return False
        
        if tiles[0][0] == tiles[-1][1]:
            return True
        else:
            return False
            