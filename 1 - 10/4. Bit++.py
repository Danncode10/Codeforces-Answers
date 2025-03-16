# Link: https://codeforces.com/problemset/problem/282/A
# 800 elo

n = int(input())

value = 0
for i in range(n):
    line = str(input())
    if line == "++X" or line == "X++":
        value += 1
    elif line == "--X" or line == "X--":
        value -= 1

print(value)