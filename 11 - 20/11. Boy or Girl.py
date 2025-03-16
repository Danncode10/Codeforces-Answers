# Link: https://codeforces.com/problemset/problem/236/A
# 800 elo

#Notes:
'''
.replace function
set function
'''

name = str(input())  # Take input from user

name = set(name)  # Convert string to a set (removes duplicate letters)
n = len(name)  # Count the number of unique letters

if n % 2 == 0:  # If even, print "CHAT WITH HER!"
    print("CHAT WITH HER!")
else:  # If odd, print "IGNORE HIM!"
    print("IGNORE HIM!")


# count = 0

# for i in range(len(name)):
#     for j in range(len(name)):
#         if name[i] == name[j]:
#             count += 1
#             name = name.replace(name[i], "")
#             name = name.replace(name[j], "")

# Make the name, be distinct. Therefore use set(), not list()