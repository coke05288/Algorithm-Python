## DFS & BFS
## Baekjoon 1260 DFS와 BFS
from collections import deque

# 값 입력
N, M, V = map(int, input().split(" "))

# 인접행렬 그래프 입력
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split(" "))
    graph[i][j] = graph[j][i] = 1

# DFS 재귀 함수
visit_dfs = [0] * (N+1)

def DFS(_v):
    visit_dfs[_v] = 1

    print(_v, end = " ")

    for i in range(1, N+1):
        if visit_dfs[i] == 0 and graph[i][_v]:
            DFS(i)

# BFS 함수
visit_bfs = [0] * (N+1)

def BFS(_v):
    visit_bfs[_v] = 1
    queue = deque()
    queue.append(_v)

    while queue:
        node = queue.popleft()

        print(node, end = " ")

        for i in range(N+1):
            if visit_bfs[i] == 0 and graph[i][node]:
                queue.append(i)
                visit_bfs[i] = 1 

# DFS 함수 실행
DFS(V)

print()

# BFS 함수 실행
BFS(V)