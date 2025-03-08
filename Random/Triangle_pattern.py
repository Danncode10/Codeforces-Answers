from itertools import repeat
from operator import index

n = 5

# Triangle

# for i in range(n+1):
#     print("*" * i)
#
# print()
#
# for i in range(n+1):
#     for j in range(i):
#         print(j, end="")
#     print()


# Space then Triangle

# for i in range(n+1):
#     print(" " * (n-i), "*" * i)
#
# print()
#
# for i in range(n+1):
#     print(" " * (n - i), end="")
#     for j in range(i):
#         print(j, end="")
#     print()


# Full Triangle

# for i in range(n+1):
#     print(" " * (n-i), "*" * i, end="")
#     print("*" * (i-1))
# print()
#
# for i in range(n+1):
#     print(" " * (n-i), end="")
#     print("* " * i)
# print()
#
# for i in range(n+1):
#     print(" " * (n - i), end="")
#     for j in range(i):
#         print(" ", end="")
#         print(j, end="")
#     print()

# Diamond

# for i in range(n+1):
#     print(" " * (n-i), "*" * i, end="")
#     print("*" * (i-1))
# for i in range(n):
#     print(" " * (i+1), end="")
#     print("*" * (n - i), end="")
#     print("*" * (n - i - 1))
#
#
# print()
#
# for i in range(n+1):
#     print(" " * (n-i), end="")
#     print("* " * i)
#
# for i in range(n):
#     print(" " * (i+1), end="")
#     print("* " * (n - i - 1))
#
# print()
#
# for i in range(n+1):
#     print(" " * (n - i), end="")
#     for j in range(i):
#         print(" ", end="")
#         print(j, end="")
#     print()
#
# for i in range(n):
#     print(" " * (i + 1), end="")
#     for j in range(0, n - i - 1):
#         print(" ", end="")
#         print(j, end="")
#     print()


# Double Diamond

sp_len = n
repeat = 20 - 1

def top_tri(index):
    print("  " * (sp_len - index), end="")
    print("* " * i, end="")

def bot_tri(index):
    print("  " * (index + 1), end="")
    print("* " * (n - i - 1), end="")

for i in range(n+1):
    print(" " * (n-i), end="")
    print("* " * i, end="")
    for _ in range(repeat):
        top_tri(i)
    print()


for i in range(n):
    print(" " * (i+1), end="")
    print("* " * (n - i - 1), end="")
    for _ in range(repeat):
        bot_tri(i)
    print()

print()








