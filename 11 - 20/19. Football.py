# Link: https://codeforces.com/problemset/problem/96/A
# 900 elo

n = input()
zeros = 0
ones = 0
is_dangerous = False

for c in n:
    if c == '0':
        zeros += 1
        ones = 0
    else:
        ones += 1
        zeros = 0
    if zeros == 7 or ones == 7:
        is_dangerous = True
        break

print('YES' if is_dangerous else 'NO')

