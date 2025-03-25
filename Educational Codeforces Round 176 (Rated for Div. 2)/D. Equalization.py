import sys


def min_cost_to_equal(x, y):
    if x == y:
        return 0  # Already equal

    cost_x = {}
    cost = 0
    k = 1

    # Reduce x to 0, storing costs
    while x > 0:
        cost_x[x] = cost
        cost += 2 ** k
        k += 1
        x //= 2  # Integer division

    # Reduce y to find the common ancestor
    cost = 0
    k = 1

    while y > 0:
        if y in cost_x:
            return cost + cost_x[y]  # Total cost
        cost += 2 ** k
        k += 1
        y //= 2  # Integer division

    return cost  # This should never be reached logically


def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])  # Number of test cases
    index += 1
    results = []

    for _ in range(t):
        x, y = int(data[index]), int(data[index + 1])
        index += 2
        results.append(str(min_cost_to_equal(x, y)))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
