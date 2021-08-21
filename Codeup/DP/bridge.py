#https://www.acmicpc.net/problem/1010
'''
DP TOP-DOWN(RECURSION)
dp : dict( n,value )
'''
dp = {}
def factorial_recursion(n):
    global dp

    if n in dp:
        return dp[n]
    elif n <= 1:
        return 1
    else:
        dp[n] = n * factorial_recursion(n-1)
        return dp[n]
    return dp[n] if n > 1 else 1

T= int(input())
for i in range(T):
    N,M = map(int,input().split())
    print(factorial_recursion(M)//(factorial_recursion(N)*factorial_recursion(M-N)))