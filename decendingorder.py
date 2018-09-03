num = 2341

def decendingOrder(num):
  listNum = [int(x) for x in str(num)] #converts to list
  listNum.sort(reverse=True)
  listNum = int(''.join(map(str, listNum)))
  return listNum

# num = [int(x) for x in str(num)]
# #output is [4,2,5,1]
# num.sort(reverse=True)
# num = int(''.join(map(str,num)))

# print (num)

print (decendingOrder(num))