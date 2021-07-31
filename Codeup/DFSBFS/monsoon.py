#https://www.acmicpc.net/problem/2468

#Can be where doesn't sinked like above example
'''
if water level is 1, doesn't sinked
ex)
3
2 2 2
2 2 2
2 2 2
solve)
1.set loop range => (0~max)
2.if max and min has same value => print(1)
'''

#BFS
from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
max_ = max(max(graph))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        a, b = queue.popleft()

        for i in range(4):
            na = a +dx[i]
            nb = b +dy[i]
            if na < 0 or na >= N or nb < 0 or nb >= N:
                continue
            if graph[na][nb] <= index:
                continue
            if graph[na][nb] > index and visited[na][nb] == 0:
                queue.append((na,nb))
                visited[na][nb] = 1
result = []
for index in range(0,max_+1):
    count = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > index and visited[i][j] == 0:
                bfs(i,j)
                count += 1
    result.append(count)
print(max(result))

#DFS
import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(a, b, idx):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[a][b] = 1
    for i in range(4):
        nowa, nowb = dx[i] + a, dy[i] + b
        if 0 <= nowa < N and 0 <= nowb < N and visited[nowa][
                nowb] == 0 and graph[nowa][nowb] > idx:
            dfs(nowa, nowb, idx)


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_ = max(max(graph))
min_ = min(min(graph))
count_list = []

for index in range(min_, max_+1):
    count = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > index and visited[i][j] == 0:
                dfs(i, j, index)
                count += 1
    count_list.append(count)
if max_ == min_:
    print(1)
else:
    print(max(count_list))
