import sys


def count_paint_ways(n, m, a):
    a.sort(reverse=True)  # Sort paint capacities in descending order

    # Pick the two largest capacities
    max1 = a[0]  # Largest paint amount
    max2 = a[1]  # Second largest paint amount

    # Number of ways to split the planks into two contiguous parts
    if max1 + max2 < n:
        return 0  # Not enough paint to cover the fence

    return min(max1, n - max1) + 1  # Count valid splits


def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])  # Number of test cases
    index += 1
    results = []

    for _ in range(t):
        n, m = int(data[index]), int(data[index + 1])
        index += 2
        a = list(map(int, data[index:index + m]))
        index += m
        results.append(str(count_paint_ways(n, m, a)))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
