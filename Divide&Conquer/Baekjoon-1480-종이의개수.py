## Divide & Conquer
## Baekjoon 1780 종이의 개수
## https://www.acmicpc.net/problem/1780

import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0, 0]

def check_paper(type, N, paper):
    can_use = True
    prev = type

    for i in range(N):
        for j in range(N):
            if paper[i][j] != prev:
                can_use = False
            prev = paper[i][j]

    if can_use:
        return prev
    else:
        return 444

def divide(N, paper):
    type = paper[0][0]

    if check_paper(type, N, paper) == -1:
        answer[0] += 1
    elif check_paper(type, N, paper) == 0:
        answer[1] += 1
    elif check_paper(type, N, paper) == 1:
        answer[2] += 1
    else:
        for i in range(3):
            for j in range(3):
                divide(N // 3, [row[(N // 3) * j : (N // 3) * (j + 1)] for row in paper[(N // 3) * i : (N // 3) * (i + 1)]])


divide(N, paper)
print('\n'.join(map(str, answer)))