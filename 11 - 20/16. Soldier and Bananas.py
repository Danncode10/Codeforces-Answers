# Link: https://codeforces.com/problemset/problem/546/A
# 800 elo

'''
Notes:
k = price of first banana
n = his current dollars
w = number of banana

Find how much money left needed

'''

k, n, w = map(int, input().split())

total = 0

for i in range(1, w+1):
    total = total + (i * k)

n = total - n

if n < 0:
    print(0) # No need to borrow if 0
else:
    print(n)