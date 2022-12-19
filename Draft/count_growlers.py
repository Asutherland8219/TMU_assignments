
def count_growlers(animals): 
  growlers = 0
  
  for animalIndex in range(len(animals)):
    if (animals[animalIndex] == "cat") or (animals[animalIndex] == "dog"):  # look left
      Cats = 0
      Dogs = 0
      for subAI in range(0, animalIndex):
        if (animals[subAI] == "cat") or (animals[subAI] == "tac"):
          Cats +=1
        elif (animals[subAI] == "dog") or (animals[subAI] == "god"):
          Dogs +=1
      if (Dogs > Cats):
        growlers += 1    

    elif (animals[animalIndex] == "tac") or (animals[animalIndex] == "god"): # look right
      Cats = 0
      Dogs = 0
      for subAI in range(animalIndex+1, len(animals)):
        if (animals[subAI] == "cat") or (animals[subAI] == "tac"):
          Cats +=1
        elif (animals[subAI] == "dog") or (animals[subAI] == "god"):
          Dogs +=1
      if (Dogs > Cats):
        growlers += 1    

  
  return growlers