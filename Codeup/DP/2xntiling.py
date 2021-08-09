#https://www.acmicpc.net/problem/11726
'''
n이 1일때 d[2]를 정의 함으로 인덱스 런타임 에러가 발생
'''
n = int(input())
if n >=3:
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 2
    for i in range(3,n+1):
        d[i] = (d[i-1] + d[i-2])%10007
    print(d[n])
elif n == 1:
    print(1)
elif n == 2:
    print(2)