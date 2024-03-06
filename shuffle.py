import random

list = [[1,2,3],[4,5,6],[7,8,9]]

for i in list:
  print(i)
  print()


def shuffle(list):
  for i in range(len(list)):
    for j in range(len(list[i])):
      randRow = random.randint(0,2)
      randCol = random.randint(0,2)
      list[i][j], list[randRow][randCol] = list[randRow][randCol], list[i][j]
  return list
for i in range(3):
  print()
shuffle(list)

for i in list:
  print(i)
  print()   