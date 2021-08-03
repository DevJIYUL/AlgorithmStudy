#https://www.acmicpc.net/problem/2606
#DFS
def dfs(v):
    global count
    visited[v] = True
    count += 1
    for i in range(1,N+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


N = int(input())
M = int(input())
count = 0
visited = [False] * (N+1)
graph = [[0] *(N + 1) for _ in range(N+1)]
for _ in range(M):
  x,y = map(int,input().split())
  graph[x][y] = 1
  graph[y][x] = 1 


dfs(1)
print(count-1)

#BFS
from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
count = 0
def bfs(v):
    global count
    queue = deque()
    queue.append(v)
    while queue:
        x = queue.popleft()
        if visited[x] == 0:
            count += 1
            visited[x] = 1
            for value in graph[x]:
                queue.append(value)
        if visited[x] == 1 :
            continue
bfs(1)

print(count-1)