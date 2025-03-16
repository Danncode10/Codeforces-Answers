#Link: https://codeforces.com/problemset/problem/617/A
# 800 elo

'''
Notes:
    // = integer division
'''

n = int(input())

# Solution 1
# c = 0
# while(True):
#     n = n - 5
#     if n < 5:
#         c += 1
#         break
#     c += 1
#
# print(c)


# Solution 2

# r = n % 5
# c = (n // 5) + 1
# print(c)

# Solution 3

c = 1
while True:
    n = n - 5
    if n <= 0:
        break
    c+=1
print(c)