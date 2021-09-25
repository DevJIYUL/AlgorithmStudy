#https://www.acmicpc.net/problem/9465
t = int(input())
for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(2):
        graph.append(list(map(int,input().split())))
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0],dp[1][0] = graph[0][0],graph[1][0]
    if n >=2:
        dp[0][1],dp[1][1] = graph[1][0] + graph[0][1],graph[0][0]+graph[1][1]
    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1] + graph[0][i],dp[1][i-2] + graph[0][i])
        dp[1][i] = max(dp[0][i-1] + graph[1][i],dp[0][i-2] + graph[1][i])
    print(max(dp[0][n-1],dp[1][n-1]))