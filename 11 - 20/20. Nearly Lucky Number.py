# Link: https://codeforces.com/problemset/problem/110/A
# 800 elo

# Read input as a string
number = input()

# Initialize a counter for lucky digits
lucky_digit_count = 0

# Count occurrences of '4' and '7'
for digit in number:
    if digit == "4" or digit == "7":
        lucky_digit_count += 1

# Check if the count is exactly 4 or 7
if lucky_digit_count in (4, 7):
    print("YES")
else:
    print("NO")

