#https://www.acmicpc.net/problem/7562
'''
length : chessboard size
graph : chessboard
departure : starting point as deque
destination : target point
'''
from collections import deque
import sys
def bfs(length):
    while start:
        dx = [1,2,2,1,-1,-2,-2,-1]
        dy = [2,1,-1,-2,-2,-1,1,2]
        x,y = start.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < length and graph[nx][ny] == 0:
                start.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
N = int(sys.stdin.readline())
start = deque()
answer=[]
for i in range(N):
    length = int(sys.stdin.readline())
    graph = [[0 for _ in range(length)] for _ in range(length)]
    departure = list(map(int,sys.stdin.readline().split()))
    start.append([departure[0],departure[1]])
    destination = list(map(int,sys.stdin.readline().split()))
    #if departure == destination case
    if departure == destination:
        answer.append(0)
        continue
    bfs(length)
    answer.append(graph[destination[0]][destination[1]])
for value in answer:
    print(value)