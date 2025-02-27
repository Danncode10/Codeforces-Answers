# Link: https://codeforces.com/problemset/problem/71/A

'''
Goal:
    find first letter, find how many letters are there and subtract 2, find the last letter. But if the total length is short n < 10, keep the word

    ex. localization -> l10n

'''

n = int(input()) # Get how many input
# get the len

for _ in range(n):
    word = str(input())
    if len(word) > 10:
         first_letter = word[0]
         last_letter = word[len(word) - 1]
         new_word = first_letter + str(len(word) - 2) + last_letter
         print(new_word)
    else:
        print(word)

