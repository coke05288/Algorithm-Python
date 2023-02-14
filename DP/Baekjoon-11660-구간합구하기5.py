## 동적계획법(Dynamic Programming), 누적합
## Baekjoon 11660 구간합구하기 5
## https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [[0] * (N+1)]
D = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N):
    temp_list = [0] + list(map(int, input().split()))
    A.append(temp_list)

for i in range(1, N+1):
    for j in range(1, N+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1])