# Link: https://codeforces.com/problemset/problem/4/A

'''
Goal: Find a number when divided by 2 or split, results even, from 1 to 100

    ex:
        8 -> (4+4)(6+2) YES
        5 -> (3+2) NO
        10 ->(6+4) YES

    Analysis
        if w is odd, NO

'''


# MY ANSWER

w = int(input())

if w % 2 == 0:
    for i in range(2,w):
        k = w - i
        if k % 2 == 0 and i % 2 == 0:
            print('Yes')
            break
    else:
        print('No')
else:
    print('No')



# Problems with This Approach
# Unnecessary Loop:
# You don’t need to check every possible i and k.
# We already know that any even number greater than 2 can be split into two even numbers.
# Misses an Important Case:
# w = 2 is even, but it cannot be split into two even numbers (because 1+1 is odd).
# Your loop doesn't run for w = 2, but it still prints "No" correctly.
# However, this means the loop is unnecessary.

# CORRECT ANSWER
#
# w = int(input())
#
# if w > 2 and w % 2 == 0:
#     print("YES")
# else:
#     print("NO")


