## 누적합
## Baekjoon 10986 나머지합
## https://www.acmicpc.net/problem/10986

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
S = [0] * N
C = [0] * M
S[0] = A[0]

answer = 0

for i in range(1, N):
    S[i] = A[i] + S[i-1]

for i in S:
    remain_num = i % M
    if remain_num == 0:
        answer += 1
    C[remain_num] += 1

for i in C:
    if i > 1:
        answer += i * (i-1) // 2

print(answer)