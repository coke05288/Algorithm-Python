## DFS & BFS
## Baekjoon 2606 바이러스
## https://www.acmicpc.net/problem/2606

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
m = int(input())

answer = 0

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


def dfs(v):
    global answer

    visited[v] = True
    answer += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)

print(answer-1)