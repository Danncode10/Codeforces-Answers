#Link: https://codeforces.com/problemset/problem/41/A
# 800 elo
'''
Notes:
    reversing a string
    word[::-1]
'''

import sys

word1 = str(sys.stdin.readline().strip())
word2 = str(sys.stdin.readline().strip())

if word2 == word1[::-1]:
    print("YES")

else:
    print("NO")