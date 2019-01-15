from functools import reduce 
def transform_list(list_in):
  list_out = []

  for i in range(len(list_in)):
    memory = list_in.pop(0)
    list_out.append(reduce(lambda x, y: x*y, list_in))
    list_in.append(memory)
  return list_out

print(transform_list(list_in = [1, 2, 3, 4, 5]))

