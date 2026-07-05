from collections import deque

grid = [
    [0, 0, 1],
    [0, 1, 0],
    [0, 0, 'G']
]

queue = deque()
visited = []

# Down, Right, Up, Left
direction = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

queue.append((0, 0))
visited.append((0, 0))

while queue:

    x, y = queue.popleft()

    # Goal পাওয়া গেছে
    if grid[x][y] == 'G':
        print("Goal Found")
        break

    for dx, dy in direction:

        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:

            if grid[nx][ny] != 1 and (nx, ny) not in visited:

                visited.append((nx, ny))
                queue.append((nx, ny))