grid=[
[0,0,1],
[0,0,0],
[1,0,0]
]

visited=[]

direction=[
(1,0),
(0,1),
(-1,0),
(0,-1)
]

def valid(x,y):

    return 0<=x<3 and 0<=y<3

def dfs(x,y):

    visited.append((x,y))
    print(x,y)

    for dx,dy in direction:

        nx=x+dx
        ny=y+dy

        if valid(nx,ny):

            if grid[nx][ny]==0 and (nx,ny) not in visited:

                dfs(nx,ny)

dfs(0,0)

print(visited)