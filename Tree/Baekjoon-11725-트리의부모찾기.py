## Tree
## Baekjoon 11725 트리의 부모 찾기
## https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = [0] * (N+1)

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            result[i] = v

dfs(1)

for i in range(1, len(result)):
    print(result[i])