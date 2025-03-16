# Link: https://codeforces.com/problemset/problem/59/A
# 800 elo

'''
Notes:
.isupper() and .islower() function

.upper() and .lower()
'''

word = input()

# Count low and uppercase:
low = 0
up = 0

for letter in word:
    if letter.isupper():
        up += 1
    if letter.islower():
        low += 1

if low >= up:
    print(word.lower())
else:
    print(word.upper())