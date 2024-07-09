## 다익스트라(Dijkstra)
## Baekjoon 1753 최단경로
## https://www.acmicpc.net/problem/1753

import sys, heapq

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
dp = [INF] * (V + 1)
heap = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

def dijkstra(start):

    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        w, v = heapq.heappop(heap) # w : 방문노드 가중치 / v : 방문 노드

        if dp[v] < w:
            continue

        for tw, tv in graph[v]: # tv : 방문할 노드 / tw : 방문할 노드 가중치
            nw = tw + w
            if nw < dp[tv]:
                dp[tv] = nw
                heapq.heappush(heap, (nw, tv))
                
dijkstra(K)

for i in range(1, V + 1):
    print("INF" if dp[i] == INF else dp[i])