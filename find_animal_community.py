# You are given a matrix/grid. you need to find the largest community (count) of animals which are interconnected. (You can move in 8 directions)

# grid = [
#         [1,1,0,0,1],
#         [1,0,1,0,0],
#         [0,0,1,0,0],
#         [0,0,0,0,1],
#         [1,1,0,1,0]
#     ]
# output => 5

grid = [
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0]
]

# -1,0  -1,1  0,1  1,1  1,0  1,-1  0,-1  -1,-1


def printGrid(grid):
    for i in range(len(grid)):
        print(grid[i])


def find_animals(grid):
    maxCount = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # print(i,j)
            if grid[i][j] == 1:
                count = dfs(i, j, grid)
                # print('count = ',count)
                # printGrid(grid)
                if count > maxCount:
                    maxCount = count
    print(maxCount)


def dfs(row, column, grid):
    rowVect = [-1, -1, 0, 1, 1, 1, 0, -1]
    columnVect = [0, 1, 1, 1, 0, -1, -1, -1]
    grid[row][column] = 'v'
    count = 1
    # count += 1
    for i in range(len(rowVect)):
        if canMove(row+rowVect[i], column+columnVect[i], grid):
            # print(row+rowVect[i], column+columnVect[i])
            count += dfs(row+rowVect[i], column+columnVect[i], grid)
    return count


def canMove(row, column, grid):
    if column >= 0 and row >= 0 and column < len(grid[0]) and row < len(grid) and grid[row][column] == 1:
        return True
    else:
        return False


printGrid(grid)
find_animals(grid)
print()
printGrid(grid)
