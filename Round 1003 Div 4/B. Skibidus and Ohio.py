# Link: https://codeforces.com/contest/2065/problem/B

# I used hint to understand the problem

# n = int(input())
#
# answers = []
#
# for _ in range(n):
#     word = input().strip()
#     count = 0
#
#     for i in range(len(word) - 1):
#         if word[i] == word[i+1]:
#             count += 1
#
#     min_count = len(word) - count
#     answers.append(min_count)
#
# for x in answers:
#     print(x)


n = int(input())  # Number of test cases

answers = []

for _ in range(n):
    word = input().strip()  # Read input string
    count = 0  # Count of adjacent duplicates

    # Count adjacent duplicates
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1

    if count == 0:
        count = len(word)

    answers.append(count)  # Store result

# Print all results
for x in answers:
    print(x)


