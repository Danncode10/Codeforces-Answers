# Link: https://codeforces.com/problemset/problem/266/B
# 800 elo

# n, t = map(int, input().split())
#
# arr = list(input())
# new_arr = arr
#
# while t > 0:
#     for i in range(n):
#         if arr[i] == 'G' and not(i == 0):
#             if arr[i-1] == 'B':
#                 # swap new Arr
#                 new_arr[i], new_arr[i-1] = 'B', 'G'
#                 i += 1 # --------------> Forgot about this, So that avoid double swap
#     # new_arr is modified
#     arr = new_arr
#     t -= 1
#
# print(arr)


# compare arr from the last index

# while t > 0:
#     for i in range(n):
#         if arr[n-i] == 'G' and arr[n-i-1] == 'B':
#             # SWAP in new array and SKIP next arra index
#             new_arr[n - i], new_arr[n-i-1] = new_arr[n-i-1], new_arr[n - i]
#     t -= 1
#
# print(arr)


n, t = map(int, input().split())

arr = list(input())

while t > 0:
    i = 0
    while i < n - 1:
        if arr[i] == 'B' and arr[i+1] == 'G':
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 2  # after swap, skip next index
        else:
            i += 1
    t -= 1

print(''.join(arr))

