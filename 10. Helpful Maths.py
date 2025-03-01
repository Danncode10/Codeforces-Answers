# Link: https://codeforces.com/problemset/problem/339/A
# 800 elo

inp = list(map(int, input().split('+')))

inp.sort()

n = len(inp)
output = ""
for i in range(n-1):
    output = output + str(inp[i]) + "+"

output = output + str(inp[-1])

print(output)