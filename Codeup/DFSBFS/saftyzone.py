#https://www.acmicpc.net/problem/14502
'''
Causion
when second empty_combi loop
check the virus queue
'''
import copy
from collections import deque
from itertools import combinations
N,M = map(int,input().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
graph = []
empty = []
queue = deque()
virus = deque()
result = 0
safty = 0
def bfs():
    while virus:
        x,y = virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if clone[nx][ny] == 1:
                continue
            if clone[nx][ny] == 0:
                clone[nx][ny] = 2
                virus.append((nx,ny))

for i in range(N):
    graph.append(list(map(int,input().split())))
#Find empty and virus location then append empty(list) and queue.
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty.append((i,j))
        if graph[i][j] == 2:
            queue.append((i,j))
#Combination 3 location of the whole empty
empty_combi = tuple(combinations(empty,3))
#When it's repeated every new clones are setted each empty_combi
#Spread virus
for a,b,c in empty_combi:
    clone = copy.deepcopy(graph)
    clone[a[0]][a[1]] = 1
    clone[b[0]][b[1]] = 1
    clone[c[0]][c[1]] = 1
    virus = copy.deepcopy(queue)
    bfs()
    for i in range(N):
        for j in range(M):
            if clone[i][j] == 0:
                safty += 1

    result = max(result,safty)
    safty = 0
print(result)
