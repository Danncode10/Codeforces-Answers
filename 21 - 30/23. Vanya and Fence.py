# Link: https://codeforces.com/problemset/problem/677/A
# Elo: 800 elo

no_friends, height = map(int, input().split())

list_of_height = []

for h in map(int, input().split()):
	list_of_height.append(h)


# Now we have list of height, compare if it is greater than height

ans = 0

for h in list_of_height:
	if h > height: 
		ans += 2
	else:
		ans += 1

print(ans)

