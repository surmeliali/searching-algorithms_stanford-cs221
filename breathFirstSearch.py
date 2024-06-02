''' Breath First Search
Advantages over DFS:
- finds the shortest path between the starting point and any other reacheable node.
- generally requires more memory
'''
from collections import deque  # using list is not ideal since adding an element at 0 index cost extra memory...

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def bfs(graph, start):

    q = deque()
    # using set decreases the lookup time,  asuming order is not important...
    visited = set()

    visited.add(start)
    q.append(start)

    while q:
        vertex = q.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

    return visited


print(bfs(graph, 'A'))
