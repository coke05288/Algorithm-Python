## 정렬
## Baekjoon 11650 좌표 정렬하기
## https://www.acmicpc.net/problem/11650

import sys
input = sys.stdin.readline

N = int(input())

point_list = list()

for _ in range(N):
    x, y = map(int, input().split())
    point_list.append([x, y])

point_list.sort()

for point in point_list:
    print(point[0], point[1])