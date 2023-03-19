## 구현(Implementation), 투포인터(Two-Pointer)
## Baekjoon 2018 수들의 합 5
## https://www.acmicpc.net/problem/2018

import sys
input = sys.stdin.readline

N = int(input())
answer = 0

start, end = 1, 1
sum = 1

while end != N:
    if sum == N:
        answer += 1
        end += 1
        sum += end
    elif sum > N:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end

print(answer)

