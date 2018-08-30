# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
  # Your code here
  if count < 10:
    return "Number of donuts: {}".format(count)
  elif count >= 10:
    return "Number of donuts: many"

print (donuts(5))

# 2. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
  # Your code here
  if len(s) < 2:
    return ''
  return s[:2] + s[-2:]
