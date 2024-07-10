## Stack & Queue
## elice-code-challenge day3 문자열압축해제

from collections import deque
import sys

input = sys.stdin.readline

S = list(input().rstrip())
answer = list()

queue = deque()

def solution(s):
    for i in range(len(s)):
        temp = deque()
        
        if s[i] == '(':
            queue.append('*')
            continue
        elif s[i] == ')':
            v = queue.pop()
            while(v != '*'):
                temp.appendleft(v)
                v = queue.pop()
            queue.append(int(queue.pop()) * ''.join(map(str, temp)))
            continue
        else:
            queue.append(s[i])

    return ''.join(map(str, queue))

result = solution(S)

# print(result)
print(len(result))