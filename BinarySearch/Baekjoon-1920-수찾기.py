## BinarySearch
## Baekjoon 1920 수찾기
## https://www.acmicpc.net/problem/1920

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
MA = list(map(int,input().split()))

for i in range(M):

    find = False
    target = MA[i]

    start = 0 
    end = len(A) - 1

    while start <= end:
        mid = int((start + end) / 2)
        mid_value = A[mid]

        if mid_value > target:
            end = mid - 1
        elif mid_value < target:
            start = mid + 1
        else:
            find = True
            break

    if find:
        print(1)
    else:
        print(0)