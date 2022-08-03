import sys
import math

X, Y = map(int, sys.stdin.readline().split())
Z = math.trunc((Y / X) * 100)

left = 0
right = Z
target = Z + 1
cant_flag = False
result = 0
temp = Z

while left <= right and Z == temp:
    X += 1
    Y += 1
    Z = math.trunc((Y / X) * 100)

    mid = (left + right) // 2
    if target == mid:
        cant_flag = False
        break
    elif target > mid:
        left = mid + 1
        cant_flag = True
    else:
        right = mid - 1
        cant_flag = True
    result += 1

if cant_flag:
    print(-1)
else:
    print(result)
