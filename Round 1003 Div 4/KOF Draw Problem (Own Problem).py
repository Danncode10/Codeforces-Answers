
bingo = [
    [1,2,3],[4,5,6],[7,8,9],
    [1,4,7],[2,5,8],[3,6,9],
    [1,5,9],[3,5,7]
    # The patterns are sorted
]

num = list(map(int, input().split()))

# Find chance of win

for i in range(len(num)):
    for j in range(len(bingo)):
        if num[i] in bingo[i]:
            print(bingo[i])


