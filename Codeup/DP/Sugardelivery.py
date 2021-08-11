#https://www.acmicpc.net/problem/2839

n = int(input())

d = [50001] * (n+1)
d[0] = 0
bag = [3,5]
for i in range(2):
    for j in range(bag[i],n+1):
        d[j] = min(d[j],d[j-bag[i]] +1)
if d[n] == 50001:
    print(-1)
else:
    print(d[n])
