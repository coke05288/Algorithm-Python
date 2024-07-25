## Stack
## Baekjoon 2046 풍선터뜨리기
## https://www.acmicpc.net/problem/2046

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
balloons = list(map(int, input().split()))
dq = deque(enumerate(balloons))

answer = []
is_left = True

while dq:
    if is_left:
        next = dq.popleft()
    else:
        next = dq.pop()

    answer.append(next[0] + 1)

    if dq:
        if next[1] > 0:
            is_left = True
            for _ in range(next[1] - 1):    
                dq.append(dq.popleft())
        elif next[1] < 0:
            is_left = False
            for i_ in range(abs(next[1]) - 1):    
                dq.appendleft(dq.pop())

print(' '.join(map(str, answer)))