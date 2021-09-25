#https://www.acmicpc.net/problem/14888
n = int(input())
an = list(map(int,input().split()))
arr = list(map(int,input().split()))

num = 1
sik = an[0]
result = []
def bfs(num):
    global sik
    if num == n:
        result.append(sik)
        return  
    #사칙연산 되는곳
    for j in range(4):
        #사칙연산이 불가능한 경우
        if arr[j] == 0:
            continue
        #사칙연산이 가능한 경우
        arr[j] -= 1
        if j == 0:
            sik = sik + an[num]
        elif j == 1:
            sik = sik - an[num]
        elif j == 2:
            sik = sik * an[num]
        elif j == 3:
            if sik >=0:
                division = sik % an[num]
                sik = sik // an[num]
            else:
                division = (-sik % an[num]) * -1
                sik = (-sik // an[num])*-1
        bfs(num+1)
        arr[j] += 1
        if j == 0:
            sik = sik - an[num]
        elif j ==1:
            sik = sik + an[num]
        elif j == 2:
            sik = sik // an[num]
        elif j == 3:
            sik = sik * an[num] + division 


bfs(num)

print(max(result))
print(min(result))

