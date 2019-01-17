'''
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''


def find_sum(list_e, k):
  for i in range(0,len(list_e)-1):
    for j in range(i+1,len(list_e)):
      if (list_e[i] + list_e[j]) == k:
        return True

list_e = [0, 7, 3, 8]
k = 14



if find_sum2(list_e,k):
  print('K IS A SUM of two numbers in the LIST')
else:
  print('K IS NOT A SUM of two numbers in the LIST')
