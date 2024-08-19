## 구현(Implementation), 슬라이딩 윈도우(Sliding Window)
## Baekjoon 30804 과일탕후루
## https://www.acmicpc.net/problem/30804

import sys
input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

tanghuru = [0 for _ in range(10)]

def solution(N, S):
    answer = 0

    start = 0
    tanghuru_count = 0

    for end in range(N):
        tanghuru[S[end]] += 1

        if tanghuru[S[end]] == 1:
            tanghuru_count += 1

        while tanghuru_count > 2:
            tanghuru[S[start]] -= 1

            if tanghuru[S[start]] == 0:
                tanghuru_count -= 1

            start += 1

        answer = max(answer, end - start + 1)
    
    return answer

print(solution(N, S))