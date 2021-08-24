#https://www.acmicpc.net/problem/11052
'''
dp리스트는 카드의 가격이 저장되어있는 리스트 p에 대하여 x번째에(x개 카드를 구입하는데) 가장 비싼 가격을 구해 저장한다.
gausee(x)는 dp[x]에 들어갈 값을 정하는 함수로써 다음과 같다.
ex) input : 10 9 8 7 6
index : 0 1  2  3  4  5
    p : 0 10 9  8  7  6
   dp : 0 10 20 30 40 50
   gausee(2)는 max(max(현재 최대값),dp[1]+dp[2-1])
   gausee(3)는 max(max(현재 최대값),dp[1]+dp[3-1])
   gausee(4)는 max(max(현재 최대값),dp[1]+dp[4-1]) ,max(max(현재 최대값),dp[2]+dp[4-2])
   gausee(5)는 max(max(현재 최대값),dp[1]+dp[5-1]) ,max(max(현재 최대값),dp[2]+dp[5-2])
   gausee(6)는 max(max(현재 최대값),dp[1]+dp[6-1]) ,max(max(현재 최대값),dp[2]+dp[6-2]), max(max(현재 최대값),dp[3]+dp[6-3])
   ...
   식으로 계산된다.
'''
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