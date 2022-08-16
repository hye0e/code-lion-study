import queue


from collections import deque
def BFS(graph, root):
    visited = []
    queue = ([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited)),