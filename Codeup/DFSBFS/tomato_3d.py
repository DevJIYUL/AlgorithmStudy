#https://www.acmicpc.net/problem/7569
from collections import deque

M,N,H = map(int,input().split())
graph = []
max_ = -10
unmatured = False
for _ in range(N*H):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0,N,-N]
dy = [0,-1,0,1,0,0]
queue = deque()
for i in range(N*H):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i,j))

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N*H or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == -1 or graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

bfs()
for i in graph:
    for j in i:
        max_ = max(max_, j)
        if j == 0:
            unmatured = True
if unmatured:
    print(-1)
elif max_ == 1:
    print(0)
else:
    print(max_ -1)