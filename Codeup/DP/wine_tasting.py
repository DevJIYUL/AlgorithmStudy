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

"""
d[n]는 n번째 와인까지 최적의 값일때
n번째를 안마시는지 한번 마시는지 두번마시는지로 나눈 겨웅


d = [[0 for _ in range(3)] for _ in range(n)]
d[0][1] = a[0]
for i in range(1,n):
    d[i][0] = max(d[i-1][0],d[i-1][1],d[i-1][2])
    d[i][1] = d[i-1][0] + a[i]
    d[i][2] = d[i-1][1] + a[i]
print(max(d[n-1]))

d[n]는 n번째 와인까지 최적의 값일때
d[n][0]이면 마시게하고
d[n][1]이면 안마시게한다.

d = [[0,0] for _ in range(n)]
d[0][0] = a[0]
if n >= 2:
    d[1][0] = a[0]+a[1]
if n >= 3:
    d[2][0] = max(a[0] + a[1],a[1] + a[2],a[0] + a[2])
    for i in range(3,n):
        if (a[i]+a[i-1]+d[i-3][0] > d[i-1][0]) or (a[i]+d[i-2][0] > d[i-1][0]):
            d[i][1] = 1
        else:
            d[i][1] = 0
        if d[i][1] == 1:
            d[i][0] = max(d[i-2][0],d[i-3][0] + a[i-1]) + a[i]
        else:
            d[i][0] = d[i-1][0]
print(d[n-1][0])

"""