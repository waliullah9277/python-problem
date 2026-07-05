from collections import deque

graph={
    0:[1,2],
    1:[3,4],
    2:[5],
    3:[],
    4:[],
    5:[]
}

visited=[]
queue=deque()

queue.append(0)
visited.append(0)

while queue:

    node=queue.popleft()

    print(node,end=" ")

    for neighbor in graph[node]:

        if neighbor not in visited:

            visited.append(neighbor)
            queue.append(neighbor)