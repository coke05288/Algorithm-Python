## 누적합
## Baekjoon 1806 부분합
## https://www.acmicpc.net/problem/1806

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
An = list(map(int, input().split()))

temp_sum = An[0]
answer = 100001

s = 0
e = 0

while True:
    if temp_sum < S:
        e += 1
        if e == N : 
            break
        temp_sum += An[e]
    else:
        temp_sum -= An[s]
        answer = min(answer, e - s + 1)
        s += 1

print(answer if answer != 100001 else 0)