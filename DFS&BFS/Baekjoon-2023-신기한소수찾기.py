## DFS & BFS
## Baekjoon 2023 신기한 소수 찾기
## https://www.acmicpc.net/problem/2023

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())

def checkPrime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False

    return True

def dfs(v):
    if len(str(v)) == N:
        print(v)
    else:
        for i in range(1, 10, 2):
            temp_num = int(str(v) + str(i))
            if checkPrime(temp_num):
                dfs(temp_num)

def solution():
    for i in [2, 3, 5, 7]:
        dfs(i)

solution()