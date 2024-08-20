## 구현(Implementation), 슬라이딩 윈도우
## Baekjoon 29700 우당탕탕 영화예매
## https://www.acmicpc.net/problem/29700

N, M, K = map(int, input().split())
seats = []

for _ in range(N):
    seats.append(list(input().strip()))

def solution(N, M, K, seats):
    answer = 0

    for i in range(N):
        window = []
        for j in range(M):
            if len(window) < K:
                window.append(seats[i][j])
            elif len(window) == K:
                window.pop(0)
                window.append(seats[i][j])

            if K == window.count('0'):
                answer += 1

    return answer

print(solution(N, M, K, seats))