## 구현(Implementation), 투포인터(Two-pointer), 슬라이딩윈도우(Sliding Window)
## Baekjoon 10025 게으른백곰
## https://www.acmicpc.net/problem/10025

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

answer = 0

ice_arr = [0 for _ in range(1000001)]

for _ in range(N):
    g, x = map(int, input().split())
    ice_arr[x] = g

K = K * 2 + 1
temp_sum = 0

for i in range(1000001):
    if i >= K:
        temp_sum -= ice_arr[i - K]
    temp_sum += ice_arr[i]
    answer = max(temp_sum, answer)

print(answer)