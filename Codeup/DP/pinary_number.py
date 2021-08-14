#https://www.acmicpc.net/problem/2193
#If you draw tree structure, you can find recurrence relation
n = int(input())
dp = [0 for _ in range(n)]
dp[0] = 1
if n >= 2:
    dp[1] = 1
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
print(dp[n-1])