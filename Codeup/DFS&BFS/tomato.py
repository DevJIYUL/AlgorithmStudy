#https://www.acmicpc.net/problem/7576
#basic bfs
from collections import deque

M,N = map(int,input().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
graph = []
max_ = -10
unmatured = False
for _ in range(N):
    graph.append(list(map(int,input().split())))
queue = deque()
for numx, i in enumerate(graph):
    for numy, j in enumerate(i):
        if j == 1:
            queue.append((numx,numy))


def  bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1 or graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
bfs()

for a in graph:
    for value in a:
        max_ = max(max_,value)
        if value == 0:
            unmatured = True
if unmatured == True:
    print(-1)
elif max_ == 1:
    print(0)
else:
    print(max_ -1)