## DFS & BFS
## Baekjoon 11725 트리의 부모 찾기
## https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
parent_nodes = [0 for _ in range(n+1)]

for _ in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)



def dfs(v):
    for i in graph[v]:
        if parent_nodes[i] == 0:
            parent_nodes[i] = v
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(parent_nodes[i])