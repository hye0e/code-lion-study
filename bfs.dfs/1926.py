import sys
from collections import deque
"""
그림의 개수
가장 넓은 그림의 넓이 출력

1. bfs 로 상하좌우로 움직여서 0인 곳 세기
2. 0이 몇개인지 list로 받고 max 찾기
"""
input = sys.stdin.readline

n, m = map(int, input().split())
# 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip().split())))    

def bfs(x, y):
    each_cnt = 1
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_step_x = x + dx[i]
            next_step_y = y + dy[i]
            if 0 <= next_step_x < n and 0 <= next_step_y < m:
                if graph[next_step_x][next_step_y] == 1:
                    graph[next_step_x][next_step_y] = 0
                    queue.append((next_step_x, next_step_y))
                    each_cnt += 1
    return each_cnt

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

    
cnt = 0
max_count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            max_count = max(max_count, bfs(i, j))
            cnt += 1
print(cnt)
print(max_count)