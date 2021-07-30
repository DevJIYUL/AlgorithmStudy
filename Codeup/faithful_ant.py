#10*10 input ant area(food,block,available way)
array = [list(map(int,input().split())) for _ in range(10)]
flag = 0
block = True
i =1
j =1
#moving of ant right toward
def right(array):
  global flag
  global j
  #j += 1
  while array[i][j+1] != 1:
    j += 1
    if array[i][j] == 2:
      array[i][j] = 9
      flag = 1
      break
    else:
      array[i][j] = 9
      #j +=1
  return array
#moving of ant down toward
def down(array):
  global flag
  global i
  #i += 1
  while array[i+1][j] != 1:
    i += 1
    if array[i][j] == 2:
      array[i][j] = 9
      flag = 1
      break
    elif array[i][j+1] == 0:
      array[i][j] = 9
      break
    else:
      array[i][j] = 9
      #i +=1
  return array
#some of exception
#if food on (1,1)
if array[1][1] == 2:
  array[1][1]=9
  flag = 1
else:
  array[1][1]=9
#ant exec
while flag == 0 and block == True:
  right(array)
  if flag == 1:
    break
  down(array)
  if flag ==0 and array[i+1][j] == 1 and array[i][j+1] == 1:
    block = False
#showing ant track
for i in range(10):
  for j in range(10):
    print(array[i][j],end=" ")
  print()