## BinarySearch
## Baekjoon 2110 공유기설치
## https://www.acmicpc.net/problem/2110
import math, sys
input = sys.stdin.readline

# N, C 입력
N, C = map(int, input().split())
# X 입력
X = [int(input()) for i in range(N)]

# 이진 탐색을 위한 X 정렬
X.sort(reverse=False)

# 이진 탐색을 위한 start, end index
start = 1
end = X[-1] - X[0]
# 결과값을 담을 answer 변수
answer = 0

# 이진 탐색
if C == 2:
    print(end)
else:
    while start < end:
        mid = (start + end) // 2
        now = X[0]
        count = 1

        for i in range(N):
            # 지금 집(now) 기준 mid 거리 만큼 떨어진 집 체크
            if X[i] >= now + mid :
                now = X[i] # 해당 집에 공유기 설치, 지금 집 변경
                count += 1
        
        # C 를 기준으로 공유기를 설치한 집 개수 파악후, 많으면 길이 늘리고, 적으면 줄이고.
        if count >= C:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    print(answer)