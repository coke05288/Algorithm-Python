## 그리디 알고리즘
## 백준 2217 로프
## https://www.acmicpc.net/problem/2217
from sys import stdin

N = int(stdin.readline())
K = []

for _ in range(N):
    K.append(int(stdin.readline()))

def solution(_K):
    answer = 0

    temp_K = sorted(_K)
    
    for i in range(len(_K)):
        temp_answer = temp_K[i] * (len(_K)-i)
        if answer < temp_answer:
            answer = temp_answer

    return answer

print(solution(K))