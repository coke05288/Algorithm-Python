## Tree, MST(Minimum Spanning Tree)
## Baekjoon 1197 최소 스패닝 트리
## https://www.acmicpc.net/problem/1197

V, E = map(int, input().split())

edges = []

root = [i for i in range(V + 1)]
rank = [0 for _ in range(V + 1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

def find(x):
    if root[x] != x:
        root[x] = find(root[x])

    return root[x]
    
def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    
    if rank[x] > rank[y]: 
        root[y] = x
    else:
        root[x] = y

        if rank[x] == rank[y]:
            rank[x] += 1

def solution(edges):
    answer = 0
    
    edges = sorted(edges, key = lambda x : x[0])

    for edge in edges:
        if find(edge[1]) == find(edge[2]):
            continue

        union(edge[1], edge[2])
        answer += edge[0]
             
    return answer

print(solution(edges))