
## DFS & BFS
## DFS와 BFS

N, M, V = map(int, input().split(" "))

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

print(graph)