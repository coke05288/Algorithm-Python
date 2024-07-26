## 구현(Implementation)
## Baekjoon 2750 수 정렬하기
## https://www.acmicpc.net/problem/2750

N = int(input())
arr = []

def c_sort():
    for i in range(len(arr)-1):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp


for _ in range(N):
    arr.append(int(input()))

c_sort()

for i in arr:
    print(i)