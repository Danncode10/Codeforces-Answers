# Link:  https://codeforces.com/problemset/problem/263/A
# 800 elo
# Time: NOT FINISHED

# input
for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        r = i
        c = row.index(1)

# Compute the Manhattan distance from (r,c) to (2, 2)
print(abs(r-2) + abs(c-2))



