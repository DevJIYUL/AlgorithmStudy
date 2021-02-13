global array
array = [list(map(int,input().split())) for _ in range(10)]
array[1][1]=2
current = array[1][1]
i =1
j =1
def right(array):
  global i
  i += 1
  while array[i][j] !=1:
    if array[i][j] == 2:
      array[i][j]=9
      break
    else:
      array[i][j]=9
    i +=1
  return 
def down(array):
  global j
  j += 1
  while array[i][j] !=1:
    if array[i][j] == 2:
      array[i][j]=9
      break
    else:
      array[i][j]=9
    j +=1
  return 
for _ in range(20):
  right(array)
  down(array)
for i in range(10):
  for j in range(10):
    print(array[i][j],end=" ")
  print()