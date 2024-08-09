## 분리집합(DisjointSet)
## Baekjoon 1717 집합의표현
## https://www.acmicpc.net/problem/1717

n, m = map(int, input().split())
root = [i for i in range(n + 1)]
rank = [0 for i in range(n + 1)]

def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if root[x] > root[y]:
        root[y] = x
    elif root[x] < root[y]:
        root[x] = y
    else:
        rank[x] += 1        

for _ in range(m):
    o, a, b = map(int, input().split())

    if o == 0:
        union(a, b)
    elif o == 1:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')

