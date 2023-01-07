## 구현(Implementation)
## Baekjoon 2525 단축키지정
## https://www.acmicpc.net/problem/2525

A, B = map(int, input().split())
C = int(input())

B += C

if B >= 60 :
    A += B//60
    B -= 60 * (B//60)

if A >= 24:
    A -= 24

print("{} {}".format(A, B))