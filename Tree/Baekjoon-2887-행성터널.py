## Tree, MST(Minimum Spanning Tree)
## Baekjoon 2887 행성 터널
## https://www.acmicpc.net/problem/2887

N = int(input())
planets = []
roots = [i for i in range(N)]

for i in range(N):
    x, y, z = map(int, input().split())
    planets.append((i, x, y, z))

def find(x):
    if roots[x] != x:
        roots[x] = find(roots[x])
    
    return roots[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    
    if x > y:
        roots[y] = x
    else :
        roots[x] = y


def solution(planets):
    answer = 0
    
    edges = []

    for i in [1, 2, 3]:
        planets = sorted(planets, key = lambda x : x[i])
        edge = [(abs(b[i] - a[i]), a[0], b[0]) for a, b in zip(planets[:-1], planets[1:])]
        edges += edge

    edges = sorted(edges, key = lambda x : x[0])

    for edge in edges:
        if find(edge[1]) == find(edge[2]):
            continue

        answer += edge[0]
        union(edge[1], edge[2])

    return answer


print(solution(planets))