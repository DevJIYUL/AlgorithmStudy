#https://www.acmicpc.net/problem/11053
#limited 1 <= n <= 1,000
#limited 1 <= n <= 1,000,000 => binary_search O(logn)
import sys
input = sys.stdin.readline
n = int(input())
an = list(map(int,input().split()))
dp = [1 for _ in range(n)]


for i in range(n):
    for j in range(i):
        if an[i] > an[j]:
            dp[i] = max(dp[i],dp[j] +1)
print(max(dp))