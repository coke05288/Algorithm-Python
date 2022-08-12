## 구현(Implementation)
## Baekjoon 20053 최소, 최대 2
## https://www.acmicpc.net/problem/20053

for _ in range(int(input())):
    N = int(input())
    num_list = sorted(map(int, input().split()))
    print(num_list[0], num_list[-1])