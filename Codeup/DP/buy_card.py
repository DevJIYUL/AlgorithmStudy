#https://www.acmicpc.net/problem/11052
import math
def gauss(n):
    index = 1
    max_ = p[n]
    while index < math.ceil((n+1)/2):#4
        max_ = max(max_ ,dp[index] + dp[n-index])
        index += 1
    return max_
N = int(input())
p=list(map(int,input().split()))
p.insert(0,0)
dp=[0]
dp.append(p[1])
for i in range(2,N+1):
    dp.append(gauss(i))
print(gauss(N))