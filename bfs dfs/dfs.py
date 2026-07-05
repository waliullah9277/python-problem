graph = {
    0:[1,2],
    1:[3,4],
    2:[5],
    3:[],
    4:[],
    5:[]
}

visited=[]

def dfs(node):

    if node in visited:
        return

    visited.append(node)
    print(node,end=" ")

    for neighbor in graph[node]:
        dfs(neighbor)

dfs(0)