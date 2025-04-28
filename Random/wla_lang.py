# 1. Sorting:

unsorted_array = [42, 7, 19, 3, 25, 14, 8, 1]

n = len(unsorted_array)

for i in range(n):
    for j in range(0, n - i - 1):
        if unsorted_array[j] > unsorted_array[j+1]:
            #swap:
            unsorted_array[j], unsorted_array[j+1] = unsorted_array[j+1], unsorted_array[j]

print(unsorted_array)



