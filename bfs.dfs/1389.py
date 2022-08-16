import sys
from collections import deque

N, M = map(int, input().split())
graph = [[] * M]
for i in range(M):
    graph.append([])

    node, vertex = map(int, input().split())
    graph[node].append(vertex)