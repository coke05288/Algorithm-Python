## Stack
## Baekjoon 9012 괄호
## https://www.acmicpc.net/problem/9012

import sys
input = sys.stdin.readline

T = int(input())

stack = []

for _ in range(T):
    stream = list(input().rstrip())

    is_VPS = True

    for i in range(len(stream)):
        if stream[i] == '(':
            stack.append(stream[i])
        else:
            if stack:
                stack.pop()
            else:
                is_VPS = False
                break
    
    if not stack:
        if not is_VPS:
            print("NO")       
        else:
            print("YES")
    else:
        print("NO")
    

    stack.clear()

