#https://www.acmicpc.net/problem/12100
import sys, copy
input = sys.stdin.readline
result = []
def dfs(cur):
    global board
    result.append(max(max(board)))
    if cur == 5:    
        return
    
    temp = copy.deepcopy(board)
    
    for angle in direction:
        x = 360 - angle
        a = copy.deepcopy(rotate(temp,angle))
        b = copy.deepcopy(move(a))
        m = copy.deepcopy(rotate(b,x))
        board = copy.deepcopy(m)

        dfs(cur+1)
    return

def move(b):
    temp_b = []
    for i in b:
        new = [x for x in i if x !=0]
        for j in range(1,len(new)):
            if new[j-1] == new[j]:
                new[j-1] = 2*new[j]
                new[j] = 0
        new = [x for x in new if x != 0]
        temp_b.append(new+[0]*(n-len(new)))
    return temp_b



def rotate(m,d):
    n = len(m)
    ret = [[0]*n for i in range(n)]

    #아래로
    if d == 90:
        for r in range(n):
            for c in range(n):
                ret[c][n-1-r] = m[r][c]
    #오른쪽
    elif d == 180:
        for r in range(n):
            for c in range(n):
                ret[n-1-r][n-1-c] = m[r][c]
    #위로
    elif d == 270:
        for r in range(n):
            for c in range(n):
                ret[n-1-c][r] = m[r][c]
    #왼쪽
    elif d == 360 or d == 0:
        for r in range(n):
            for c in range(n):
                ret[r][c] = m[r][c]
    return ret

def print_b(b):
    for i in range(n):
        for j in range(n):
            print(b[i][j],end = " ")
        print()

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
direction = (90,180,270,360)
dfs(0)
print(len(result))
print(max(result))