#https://www.acmicpc.net/problem/2579
n = int(input())
stair = []
for i in range(n):
    stair.append(int(input()))

dp = [[0 for _ in range(3)] for _ in range(n)]
dp[0][1] = stair[0]
for i in range(1,n):
    #0 don't tracked
    #1 one time tracked
    #2 continully two time tracked
    #if i is 0, it could be max(i-1 of 1, i-1 of 2)
    #if i is 1, i-1 should be 0
    #if i is 2, i-1 should be 1
    dp[i][0] = max(dp[i-1][1],dp[i-1][2])
    dp[i][1] = dp[i-1][0] + stair[i]
    dp[i][2] = dp[i-1][1] + stair[i]

print(max(dp[n-1][1],dp[n-1][2]))