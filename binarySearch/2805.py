#4 7
#20 15 10 17
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

def cut_tree_sum(mid):
    sum = 0
    for tree in tree_list:
        if tree - mid >= 0:
            sum += tree - mid

    return sum

tree_list.sort()
left = 0
right = max(tree_list)
result = 0

while left <= right:
    mid = (left + right) // 2
    target = cut_tree_sum(mid)
    if target >= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)