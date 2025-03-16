# Link: So
# 800 elo
#Notes:
'''
pop(index) --> Removes list at certain index

sometimes while loops are better than for loops

    - Use for when the number of iterations is fixed or known beforehand (e.g., looping over a range, list, or string).
    - Use while when the number of iterations is dynamic or depends on a condition that may change (in our case the size of 'a' changes every pop()
    (e.g., modifying a list while iterating, waiting for a condition to be met).

'''

n = int(input())
a = list(str(input()))
k = 0 # Output
i = 0

while i < len(a) - 1:
    if a[i] == a[i+1]:
        a.pop(i)
        k += 1
    else:
        i+=1

print(k)
