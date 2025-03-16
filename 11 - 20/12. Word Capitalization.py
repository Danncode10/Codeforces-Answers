# Link: https://codeforces.com/problemset/problem/281/A
# 800 elo

#Notes
'''
upper function
'''

word = list(str(input()))
ans = ""

word[0] = word[0].upper()

for letter in word:
    ans += letter

print(ans)