s = "ooOXxX"

def xo(s):
  #first use .count() to count how many x's and o's are inside the string
  #then check if the amount are equal
  #should also be case insensitive
  o = s.count("o") + s.count("O")
  x = s.count("x") + s.count("X")
  if o == x:
    return True
  else:
    return False


#better solution

# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')


# Notes:
# figure out why  o = s.count("o" and "O") doesn't work for counting capital letters as well


print (s.count("o" and "O"))