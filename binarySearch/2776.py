import sys

input = sys.stdin.readline

T = int(input())

def binarySearch(target, left, right):
    while left <= right:
        mid = (left + right) // 2

        if book_1[mid] == target:
            print(1)
            nothing = False
            break
        elif book_1[mid] > target:
            right = mid - 1
            nothing = True
        else:
            left = mid + 1
            nothing = True
            
    if nothing:
        print(0)

for i in range(T):
    N = int(input())
    book_1 = list(map(int, input().strip().split()))
    M = int(input())
    book_2 = list(map(int, input().strip().split()))

    book_1.sort()
    left = 0
    right = len(book_1) - 1
    nothing = False

    for target in book_2:
        binarySearch(target, left, right)

