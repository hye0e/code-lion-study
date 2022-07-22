import sys
from collections import deque

input = sys.stdin.readline

testcase = int(input())

result = []
for i in range(testcase):
    N, M = map(int, input().split())
    important = int(input())
    important_dict = {}
    for j in range(N):
        important_dict[j] = important # index 

    for k in range(0, len(important_dict) - 1):
        if important_dict[k + 1] >= important_dict[k]:
            temp = important_dict[k]
            important_dict.pop(k)
            important_dict[k] = temp
    
    result.append(important_dict[M])


