## 다익스트라(Dijkstra)
## Baekjoon 1916 최소비용구하기
## https://www.acmicpc.net/problem/1916

import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

start, end = map(int, input().split())

def solution(start, end, graph):

    heap = []
    dp = [INF] * (N + 1)
    
    heapq.heappush(heap, (0, start))
    dp[start] = 0

    while heap:
        w, e = heapq.heappop(heap)
        
        if dp[e] < w:
            continue

        for tw, te in graph[e]:
            nw = tw + w
            if nw < dp[te]:
                dp[te] = nw
                heapq.heappush(heap, (nw, te))

    return dp[end]

print(solution(start, end, graph))
