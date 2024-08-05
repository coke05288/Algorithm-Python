## 그리디 알고리즘
## 백준 11000 강의실배정
## https://www.acmicpc.net/problem/11000

import heapq

N = int(input())

answer = 0
classes_time = list()

for _ in range(N):
    S, T = map(int, input().split())
    classes_time.append([S, T])

sorted_classes_time = sorted(classes_time, key = lambda x : (x[0], x[1]))

heap = [sorted_classes_time[0][1]]

for i in range(1, N):
    if sorted_classes_time[i][0] >= heap[0]:
        heapq.heappop(heap)

    heapq.heappush(heap, sorted_classes_time[i][1])

print(len(heap))