def unscramble(words,word):
  result=[]
  for i in words:
    if i[0] == word[0] and i[-1] == word[-1] and len(word) == len(i):
      if sorted(list(word[1:-1])) == sorted(list(i[1:-1])):
        result.append(i)
  return result