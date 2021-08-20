#https://www.acmicpc.net/problem/1707
'''
1. Get graph like all elements connected state
2. Color indicate adjacent elements to 1 or -1
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(i,color):
    visited[i] = color
    for k in graph[i]:
        #처음 방문하게되면 인접한 점과 다른색으로 표시한다
        if visited[k] == 0:
            if not dfs(k,-color):
                return False
        #이미 방문한 곳이라면 거짓을 반환한다
        elif visited[k] == visited[i]:
            return False
    return True
K = int(input())
for _ in range(K):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for i in range(E):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    print(graph)
    bipatite = True
    for j in range(1,V+1):
        if visited[j] == 0:
            bipatite = dfs(j,1)
            if not bipatite:
                break
    if bipatite == True:
        print("YES")
    else:
        print("NO")