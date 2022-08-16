import sys

input = sys.stdin.readline

N, H = map(int, input().split())
down = []
up = []

for i in range(N):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))

left = 0
right = max(obstacle_list)

while left <= right:
    mid = (left + right) // 2
    