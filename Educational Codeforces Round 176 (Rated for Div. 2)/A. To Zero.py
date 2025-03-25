#NOT ANSWERED

t = int(input())
operation_count = 1

for i in range(t):
    n, k = map(int, input().split())
    # while n > 0:
    #     n = n - k
    #     operation_count += 1
    operation_count = (n // k) + 1

print(operation_count)

