from collections import deque

grid=[
[0,0,1],
[0,0,0],
[1,0,0]
]

queue=deque()
visited=[]

direction=[
(1,0),
(0,1),
(-1,0),
(0,-1)
]

queue.append((0,0))
visited.append((0,0))

while queue:

    x,y=queue.popleft()

    print(x,y)

    for dx,dy in direction:

        nx=x+dx
        ny=y+dy

        if 0<=nx<3 and 0<=ny<3:

            if grid[nx][ny]==0 and (nx,ny) not in visited:

                visited.append((nx,ny))
                queue.append((nx,ny))

print(visited)