l = [1,2,'a','b']

def filter_list(l):
  filteredList = [e for e in l if isinstance(e, int)]
  return filteredList

print (filter_list(l))