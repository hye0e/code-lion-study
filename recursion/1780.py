# -*- coding: utf-8 -*-
import sys

input = sys.stdin.readline
N = int(input())
color = []
result = {-1: 0, 0: 0, 1: 0}


for _ in range(N):
    color.append(list(map(int, input().split())))

# 9칸 기준으로 다 같으면 True 리턴 False 리턴
def check(x, y, n):
    check_num = color[x][y]
    for i in range(n):
        for j in range(n):
            if check_num != color[x + i][y + j]:
                return False

    return True

def cut(x, y, n):
    print('===============')
    print('x = ', x)
    print('y = ', y)
    print('n = ', n)
    print('===============')
    # 9개 모두 같으면
    if check(x, y, n):
        result[color[x][y]] += 1
    # 같지 않으면 종이를 같은 크기의 종이 9개로 자르기
    else:
        for i in range(3):
            for j in range(3):
                 cut(x + i * n // 3, y + j * n // 3, n // 3)
    return

# 9개
cut(0, 0, N)
print(result)



