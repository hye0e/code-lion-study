import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
word_list = [list(input().strip()) for _ in range(N)]
result = 0

for word in word_list:
    stack = deque()
    stack.append(word[0])
    for i in range(1, len(word)):
        if not stack:
            stack.append(word[i])
            continue
        
        if stack[-1] != word[i]:
            stack.append(word[i])
        elif stack[-1] == word[i]:
            stack.pop()

    if not stack:
        result += 1

print(result)