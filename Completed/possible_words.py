def possible_words(words,pattern):
  match = []
  for word in words:
    match_true = True
    if len(word)==len(pattern):
      for i in range(len(pattern)):
        if pattern[i].isalpha():
          if pattern[i] != word[i]:
            match_true = False
            break
        else:
          if word[i] in pattern:
            match_true = False
            break
      if match_true:
        match.append(word)
  return match