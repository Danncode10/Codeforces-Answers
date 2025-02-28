#Link: https://codeforces.com/contest/2065/problem/A

n = int(input())
answers = []

for i in range(n):
    word = str(input())
    if 'us' == word[-2:]: #-2 kase 2 words ang us
        new_word = word[0:-2] + "i"
    else:
        new_word = word
    answers.append(new_word)

#Print result
for a in answers:
    print(a)