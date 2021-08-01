#https://www.acmicpc.net/problem/7569
'''
Use 3D list like above
graph=[
      [[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]
      [[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]
      ]

'''
from collections import deque

M,N,H = map(int,input().split())
graph = []
max_ = -10
unmatured = False
for _ in range(H):
    temp =[]
    for j in range(N):
        temp.append(list(map(int,input().split())))
    graph.append(temp)

dz = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < H and 0 <= ny < M and 0 <= nx < N and graph[nz][nx][ny] == 0:
                queue.append((nz,nx,ny))
                graph[nz][nx][ny] = graph[z][x][y] + 1

bfs()

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                unmatured = True
            max_ = max(max_, k)

if unmatured:
    print(-1)
elif max_ == 1:
    print(0)
else:
    print(max_ -1)