def find_sum(list_e, k):
  for i in range(0,len(list_e)-1):
    for j in range(i+1,len(list_e)):
      if (list_e[i] + list_e[j]) == k:
        return True

list_e = list(map(lambda num: int(num), input().split(' ')))
k = int(input())

if find_sum(list_e,k):
  print('K IS A SUM of two numbers in the LIST')
else:
  print('K IS NOT A SUM of two numbers in the LIST')
