# Link: https://codeforces.com/problemset/problem/158/A
# 800 elo

n,k = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort()
scores.reverse() # Highest to lowest
passers = 0

last = 0 # value of index, para pag may same score they will be passer

for i in range(n):
    if scores[i] == 0:
        break
    if i < k:
       passers += 1
       last = scores[i]
    elif last == scores[i]:
       passers += 1
    else:
       break

print(passers)
