## 구간합
## Baekjoon 11659 구간합구하기4
## https://www.acmicpc.net/problem/11659
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
perfix_sum_list = [0]

for i in range(len(num_list)):
    perfix_sum_list.append(perfix_sum_list[i] + num_list[i])

for _ in range(M):
    i, j = map(int, input().split())
    print(perfix_sum_list[j] - perfix_sum_list[i-1])