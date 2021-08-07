import sys
sys.setrecursionlimit(100000)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def dfs(x,y,days):
    global max_days
    max_days = -10

    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[x][y] < graph[nx][ny]:
            graph[x][y] = 99
            days += 1
            dfs(nx,ny,days)
            max_days = max(max_days,days)        
            return True
    return False
for i in range(n):
    for j in range(n):
        dfs(i,j,1)
print(max_days)