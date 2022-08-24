"""
5
55 185
58 183
88 186
60 175
46 155

1. x 정렬
2. y 정렬
"""
import sys

input = sys.stdin.readline

N = int(input())
x_list = [list(map(int, input().split())) for i in range(N)]
    
for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if x_list[i][0] < x_list[j][0] and x_list[i][1] < x_list[j][1]:
            rank += 1
    print(rank, end = ' ')
