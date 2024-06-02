import datetime
''' Depth FirstSearch 
Advantages over BFS:
- On binary tree generally requires less memory
- Can be easily implemented with recursion
Disadvantages:
Doesn't necessarily find the shortest path
'''

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

# Iterative


def dfs(graph, start):
    # check if vertex is visited
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append(neighbor)

    return visited


# Recursive
visited = set()


def dfsRecursion(graph, vertex, visited):
    if vertex not in visited:
        visited.add(vertex)
        for neighbor in graph[vertex]:
            dfsRecursion(graph, neighbor, visited)

    return visited


print(dfsRecursion(graph, 'A', visited))
print(dfs(graph, 'A'))
