array = [list(map(int,input().split())) for _ in range(10)]
if array[1][1] == 2:
  flag = 1
else:
  array[1][1]=9
flag = 0
block = True
i =1
j =1
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

def down(array):
  global flag
  global i
  #i += 1
  while array[i+1][j] != 1:
    i += 1
    if array[i][j+1] == 0:
      array[i][j] = 9
      break
    elif array[i][j] == 2:
      array[i][j] = 9
      flag = 1
      break
    else:
      array[i][j] = 9
      #i +=1
  return array
print()

while flag == 0 and block == True:
  right(array)
  down(array)
  if flag ==0 and array[i+1][j] == 1:
    block = False
for i in range(10):
  for j in range(10):
    print(array[i][j],end=" ")
  print()