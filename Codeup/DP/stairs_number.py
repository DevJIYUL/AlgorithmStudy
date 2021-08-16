#https://www.acmicpc.net/problem/10844
'''
d(i,j)
i : Make stair number with i digits
j : How many number is contained
ex) d(2,4)
How many number 4 at 2 digits stait number
#Don't try to find answer directly
it cause some errors
think about DP concept!!
'''
N = int(input())
d = [[0 for _ in range(10)] for _ in range(N) ]
for i in range(1,len(d[0])):
    d[0][i] = 1
for i in range(1,N):
    d[i][0] += d[i-1][1]
    d[i][9] += d[i-1][8]
    for j in range(1,9):
        d[i][j] += d[i-1][j-1] + d[i-1][j+1]
print(sum(d[N-1])%1000000000)