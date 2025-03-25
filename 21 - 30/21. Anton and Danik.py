# Link: https://codeforces.com/problemset/problem/734/A
# 800 elo
import sys

n = int(sys.stdin.readline().strip())
s = str(sys.stdin.readline().strip())

a = s.count('A')
d = s.count('D')

if a > d:
    print("Anton")

elif a == d:
    print("Friendship")

else:
    print("Danik")