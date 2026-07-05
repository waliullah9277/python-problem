grid = [
    [0, 0, 1],
    [0, 1, 0],
    [0, 0, 'G']
]

visited = []
path = []

direction = [
    (1,0,"Down"),
    (0,1,"Right"),
    (-1,0,"Up"),
    (0,-1,"Left")
]

def valid(x,y):

    return 0<=x<3 and 0<=y<3

def dfs(x,y):

    if grid[x][y]=='G':
        return True

    visited.append((x,y))

    for dx,dy,move in direction:

        nx=x+dx
        ny=y+dy

        if valid(nx,ny):

            if grid[nx][ny]!=1 and (nx,ny) not in visited:

                if dfs(nx,ny):

                    path.append(move)

                    return True

    return False

if dfs(0,0):

    path.reverse()

    print("Goal Found")
    print()

    print("Path")

    for move in path:

        print(move)
else:
    print("Goal Not Found")
