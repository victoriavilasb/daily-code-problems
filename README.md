## Daily Code Problems

Esse repositório contém os problemas enviados na newsletter do Daily Code Problems, inicialmente feitos na linguagem Python.

### Para se inscrever
[Para se inscrever acesse este link](https://www.dailycodingproblem.com/)

### Exemplo de problema proposto

Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
Upgrade to premium and get in-depth solutions to every problem.
If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

**Solution**

```python
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

```
