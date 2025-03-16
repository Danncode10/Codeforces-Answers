# Link: https://codeforces.com/problemset/problem/118/A
# 1000 elo

vowel = ['a', 'e', 'i', 'o', 'u', 'y']

word = str(input().lower())
new_word = ""

for letter in word:
    if letter in vowel:
        new_letter = ""
    else:
        new_letter = "." + letter
    new_word = new_word + new_letter

print(new_word)

