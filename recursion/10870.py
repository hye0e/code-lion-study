import sys

def recursion(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return recursion(num - 1) + recursion(num - 2)

n = int(sys.stdin.readline())
print(recursion(n))

