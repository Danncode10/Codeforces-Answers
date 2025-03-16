# Link: https://codeforces.com/problemset/problem/977/A
# 800 elo

'''
Notes:
    n = number
    k = subtract for how many times

Nice way to remove letters from a word
    [start:end]

    example 1:
        w = w[:-1]  # creates a new string that includes all characters except the last one.

    example 2:
        w = w[:4] + w[5:]  # Remove the character at index 4


'''

n, k = map(int, input().split())

w = ""

for _ in range(k):
    w = str(n)
    # Find the last digit if non-zero

    if w[-1] == "0":
        w = w[:-1]  # creates a new string that includes all characters except the last one.
        n = int(w)
    else:
        n -= 1

print(n)
