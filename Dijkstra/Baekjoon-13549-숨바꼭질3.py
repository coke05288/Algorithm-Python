## 다익스트라(Dijkstra)
## Baekjoon 13549 숨바꼭질3
## https://www.acmicpc.net/problem/13549

import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())
dp = [INF] * 100001

queue = []

def dijkstra(n, k):
    if k <= n:
        print(n - k)
        return
    
    heapq.heappush(queue, (0, n))

    while queue:
        w, n = heapq.heappop(queue)
        for nx in [n - 1, n + 1, n * 2]:
            if nx >= 0 and nx < 100001:
                if nx == n * 2 and dp[nx] == INF:
                    dp[nx] = w
                    heapq.heappush(queue, (w, nx))
                elif dp[nx] == INF:
                    dp[nx] = w + 1
                    heapq.heappush(queue, (w + 1, nx))
    
    print(dp[k])

dijkstra(N, K)