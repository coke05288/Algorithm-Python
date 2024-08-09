## 분리집합(DisjointSet), 유니온파인드(Union-Find)
## Baekjoon 20040 사이클 게임
## https://www.acmicpc.net/problem/20040

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

root = [i for i in range(n)]

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x > y:
        root[x] = y
    else :
        root[y] = x

def solution(n, m):
    is_cycle = False
    count = 0

    for _ in range(m):
        p1, p2 = map(int, input().split())

        if not is_cycle:
            count += 1

        if find(p1) != find(p2):
            union(p1, p2)
        else:
            is_cycle = True

    if is_cycle:
        return count
    else:
        return 0
            
print(solution(n, m))
    