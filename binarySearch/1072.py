import sys
import math

X, Y = map(int, sys.stdin.readline().split())
Z = math.trunc((Y / X) * 100)

left = 1
right = X

result = 0

if Z >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        if math.trunc((Y + mid / X + mid) * 100) <= Z:
            left = mid + 1
        else:
            result = mid
            right = mid - 1
            cant_flag = True

    print(result)
