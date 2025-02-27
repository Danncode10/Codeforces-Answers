# Link: https://codeforces.com/problemset/problem/231/A
# 800 elo

'''
Goal:
count how many can problems they can solve, 2 or above count of 1 is considered solvable
'''

n = int(input())

count,sum = 0,0
for i in range(n):
    x = str(input()) # input with spaces, ex 1 1 0
    sum = int(x[0]) + int(x[2]) + int(x[4])
    if sum >= 2:
        count += 1

print(count)