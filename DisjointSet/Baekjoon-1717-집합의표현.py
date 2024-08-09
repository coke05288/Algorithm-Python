## 분리집합(DisjointSet)
## Baekjoon 1717 집합의표현
## https://www.acmicpc.net/problem/1717

n, m = map(int, input().split())
root = [i for i in range(n + 1)]

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
        root[y] = x
    else :
        root[x] = y

for _ in range(m):
    o, a, b = map(int, input().split())

    if o == 0:
        union(a, b)
    elif o == 1:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')

