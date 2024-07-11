## Tree
## Baekjoon 1967 트리의 지름
## https://www.acmicpc.net/problem/1967

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    tree[u].append((v, w))
    tree[v].append((u, w))

def dfs(v, _length):

    for node, weight in tree[v]:
        if visited[node] == -1:
            new_weight = _length + weight
            visited[node] = new_weight
            dfs(node, new_weight)

    return 


visited = [-1] * (n + 1)
visited[1] = 0

dfs(1, 0)

temp = 0
endpoint = 0

for i in range(1, len(visited)):
    if temp < visited[i]:
        temp = visited[i]
        endpoint = i

visited = [-1] * (n + 1)
visited[endpoint] = 0

dfs(endpoint, 0)

print(max(visited))
    