# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline

N = int(input())
color = [list(map(int, input().split())) for _ in range(N)]
result = {-1: 0, 0: 0, 1:0}

# 1. 같은 숫자인지 계속해서 체크하기 
# 2. 아니라면 자르기
def check(start_x, start_y, n):
    check_num = color[start_x][start_y]
    for i in range(n):
        for j in range(n):
            if check_num != color[start_x + i][start_y + j]:
                return False
    return True

def divide(start_x, start_y, n):
    if check(start_x, start_y, n):
        result[color[start_x][start_y]] += 1
    else:
        for i in range(3):
            for j in range(3):
                # 첫째 줄에 N(1 ≤ N ≤ 37, N은 3k 꼴) 이므로 3개씩 나누어서 재귀 호출
                divide(start_x + i * n // 3, start_y + j * n // 3, n // 3)
    return

divide(0,0,N)
print(result)