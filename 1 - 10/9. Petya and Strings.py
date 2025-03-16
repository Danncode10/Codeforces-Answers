# Link: https://codeforces.com/problemset/problem/112/A
# 800 elo

# NOTES
'''
print(ord('A')) ---> 65

'''

word1 = str(input().upper())
word2 = str(input().upper())

def int_val(word, i):
    return ord(word[i])

result = 0

for i in range(len(word1)):
    if int_val(word1, i) > int_val(word2, i):
        result = 1
        break
    if int_val(word1, i) < int_val(word2, i):
        result = -1
        break

print(result)