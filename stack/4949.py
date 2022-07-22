import sys

input = sys.stdin.readline
result = []
while True:
    sentence = list(input())
    stack = []
    if sentence[-1] == '\n' and sentence[0] == '.':
        break
    flag = True

    for s in sentence:   
        if s == '(' or s == '[':
            stack.append(s)

        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: # 조건이 필요한 이유: ) 와 같이 하나만 들어올 수 있으므로 꼭 필요!
                flag = False
                break
        
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else: # 조건이 필요한 이유: ] 와 같이 하나만 들어올 수 있으므로 꼭 필요!
                flag = False
                break

    if flag and not stack:
        result.append('yes')
    else:
        result.append('no')

print('\n'.join(result))