# input matrix 0 is free space, 1 is wall, S is start and G is goal
grid = [
    ['S', 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 'G']
]

row = 6
col = 6

visited = []
path = []

def valid(x, y):
    if x < 0:
        return False
    if x >= row:
        return False
    if y < 0:
        return False
    if y >= col:
        return False

    return True

def dfs(x, y):
    if grid[x][y] == 'G':
        return True

    visited.append((x, y))

    # Down
    if valid(x + 1, y):
        if grid[x + 1][y] != 1 and (x + 1, y) not in visited:

            if dfs(x + 1, y):
                path.append(("Down", (x + 1, y)))
                return True

    # Right
    if valid(x, y + 1):
        if grid[x][y + 1] != 1 and (x, y + 1) not in visited:

            if dfs(x, y + 1):
                path.append(("Right", (x, y + 1)))
                return True

    # Up
    if valid(x - 1, y):
        if grid[x - 1][y] != 1 and (x - 1, y) not in visited:

            if dfs(x - 1, y):
                path.append(("Up", (x - 1, y)))
                return True

    # Left
    if valid(x, y - 1):
        if grid[x][y - 1] != 1 and (x, y - 1) not in visited:

            if dfs(x, y - 1):
                path.append(("Left", (x, y - 1)))
                return True

    return False

# Start DFS
if dfs(0, 0):
    path.reverse()

    print("Goal found")
    print("Number of moves required =", len(path))
    print()

    for move, position in path:
        print("Moving", move, position)
else:
    print("Goal not found")
    print("No path exists from Start to Goal.")