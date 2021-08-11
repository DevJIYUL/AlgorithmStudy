#https://www.acmicpc.net/problem/1149
'''
small problem can solve big problem
4
1 1 1
1 1 1
2 1 2
9 1 9
=> 5
It is wrong way to define 
if 1st house is red, 2nd house is min(2nd_house_BLUE,2nd_house_GREEN) [X]
if 2nd house is red, 2nd house is 2nd_house_RED + min(1st_house_BLUE, 1st_house_GREEN) [O]
'''
n = int(input())
house = []
for i in range(n):
    house.append(list(map(int,input().split())))


for j in range(1,n):
    house[j][0] = house[j][0] + min(house[j-1][1],house[j-1][2])
    house[j][1] = house[j][1] + min(house[j-1][0],house[j-1][2])
    house[j][2] = house[j][2] + min(house[j-1][0],house[j-1][1])

print(min(house[n-1]))