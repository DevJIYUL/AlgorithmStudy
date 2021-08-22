#https://www.acmicpc.net/problem/11057
'''
dp can be 2D list
when dp setted, considerate figure like 1D,2D
Even set dp considerate how represente the answer
디피 리스트를 정햇더라도 어떻게 답을 유도하게 표현할지 잘생각해야한다.
'''
n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n)]

for q in range(10):
    dp[0][q] = 1

for i in range(1,n):
    for j in range(10):
        for k in range(j,10):
            dp[i][j] += dp[i-1][k] % 10007



print(sum(dp[-1])%10007)