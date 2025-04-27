# Link: https://codeforces.com/problemset/problem/1030/A
# 800 elo

n = int(input())

ans = []

for a in map(int, input().split()):
	ans.append(a)

if 1 in ans:
	print("HARD")

else:
	print("EASy")