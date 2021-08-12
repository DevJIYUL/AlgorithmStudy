#https://www.acmicpc.net/problem/2156
n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))
d=[0] * 10000
d[0] = l[0]
if n >= 2:
    d[1] = l[0] +l[1] 
if n >= 3:
    d[2] = max(l[2]+l[0],l[2]+l[1],d[1])
    for i in range(3,n):
        d[i] = max(l[i] + l[i-1] + d[i-3],l[i] + d[i-2],d[i-1])
print(max(d))