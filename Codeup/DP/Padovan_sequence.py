g#https://www.acmicpc.net/problem/9461
'''
1. Divide 2 case △ and ▽
d[0] is △ sequence
d[1] is ▽ sequence
2. find a role between d[0] and d[1]
'''
import math
t = int(input())
n = []
for _ in range(t):
    n.append(int(input()))
index = math.ceil(max(n)/2)
d = [[0 for _ in range(52)] for _ in range(2)]
d[0][1],d[0][2],d[1][1],d[1][2] = 1,1,1,2
for i in range(3,index + 1):
    d[0][i] = d[1][i-1] + d[1][i-3]
    d[1][i] = d[0][i] + d[0][i-2]
for k in n:
    if k % 2 == 1:
        print(d[0][math.ceil(k/2)])
    else:
        print(d[1][math.ceil(k/2)])