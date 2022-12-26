## 그리디 알고리즘
## 백준 21758 꿀따기
## https://www.acmicpc.net/problem/21758

from sys import stdin

n = int(stdin.readline())
arr = list(stdin.readline().rstrip().split(" "))

l_dp = [0 for i in range(n+1)]
r_dp = [0 for i in range(n+1)]

def solution(n, arr):
    # 벌꿀 리스트의 총합
    arr_sum = sum(arr)
    # 벌꿀의 최대값 초기화
    max_honey = -1

    # 벌꿀의 최대값 초기화
    max_honey_left = -1
    # 벌꿀의 최대값 초기화
    max_honey_right = -1
    
    # max_case_none 구하기
    for i in range(1, n-1):
        temp  = arr_sum - arr[0] - arr[n-1] + arr[i]
        if max_honey < temp:
            max_honey = temp
    
    # print(max_honey)

    # 누적합 구하기
    for i in range(1, n+1, 1):
        l_dp[i] = l_dp[i-1] + arr[i-1]
    
    # print("l_dp : ", l_dp)

    for i in range(n-1, -1, -1):
        r_dp[i] = r_dp[i+1] + arr[i]

    # print("r_dp : ", r_dp)

    # 제일 오른쪽에 벌꿀통이 있을때
    for i in range(2, n):
        # 제일 왼쪽 꿀벌이 얻는 벌꿀 개수 : (l_dp[n] - l_dp[1])
        # arr 기준 i-1 번째(제일 왼쪽 다음 거 부터 시작) 꿀벌이 얻는 벌꿀 개수 : (l_dp[n] - l_dp[1])
        temp  = (l_dp[n] - l_dp[1]) + (l_dp[n] - l_dp[i]) - arr[i-1]
        if max_honey < temp:
            max_honey = temp

    # print("오른쪽에 벌꿀통 있을 때 최대 값 : ", max_honey_right)

    # 제일 왼쪽에 벌꿀통이 있을때
    for i in range(n-2, -1, -1):
        # 제일 오른쪽 꿀벌이 얻는 벌꿀 개수 : (r_dp[0] - r_dp[n-1])
        # arr 기준 i-1 번째(제일 오른쪽 이전 거 부터 시작) 꿀벌이 얻는 벌꿀 개수 : (l_dp[n] - l_dp[1])
        temp  = (r_dp[0] - r_dp[n-1]) + (r_dp[0] - r_dp[i]) - arr[i]
        if max_honey < temp:
            max_honey = temp
    
    # print("왼쪽에 벌꿀통 있을 때 최대 값 : ",max_honey_left)

    return max_honey

print(solution(n, arr))