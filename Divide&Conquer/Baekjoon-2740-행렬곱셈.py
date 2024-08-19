## Divide & Conquer
## Baekjoon 2740 행렬곱셈
## https://www.acmicpc.net/problem/2740

AN, AM = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(AN)]

BN, BM = map(int, input().split())
B = [list(map(int,input().split())) for _ in range(BN)]

answer = [[0 for _ in range(BM)] for _ in range(AN)]

for i in range(AN):
    for j in range(BM):
        answer[i][j] = sum([A[i][k] * B[k][j] for k in range(AM)])
    print(" ".join(map(str, answer[i])))