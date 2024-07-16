## Brute Force
## Baekjoon 2231 분해합
## https://www.acmicpc.net/problem/2231

import sys

N = int(sys.stdin.readline().rstrip())
RN = N
answer = []

while N > 0:
    if RN == N + sum(list(map(int, str(N)))) : 
        answer.append(N)
    N -= 1

if len(answer) > 0:
    print(min(answer))
else:
    print(0)
