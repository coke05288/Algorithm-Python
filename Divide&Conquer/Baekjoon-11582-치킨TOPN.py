## Divide & Conquer
## Baekjoon 11582 치킨 TOP N
## https://www.acmicpc.net/problem/11582

import math
import sys
input = sys.stdin.readline

N = int(input())
flavors = list(map(int, input().split()))
k = int(input())


def k_merge_sort(N, flavors, k, depth):

    if len(flavors) < 2:
        return flavors
    
    mid = len(flavors) // 2

    left_arr = k_merge_sort(N, flavors[:mid], k, depth + 1)
    right_arr = k_merge_sort(N, flavors[mid:], k, depth + 1)

    merge_arr = []
    
    if math.log2(k) <= depth:
        merge_arr = merge(left_arr, right_arr)
    else:
        merge_arr = left_arr + right_arr
    
    return merge_arr

def merge(left_arr, right_arr):
    
    left, right = 0, 0
    merge_arr = []

    while len(left_arr) > left and len(right_arr) > right:
        if left_arr[left] <= right_arr[right]:
            merge_arr.append(left_arr[left])
            left += 1
        else:
            merge_arr.append(right_arr[right])
            right += 1

    merge_arr += left_arr[left:]
    merge_arr += right_arr[right:]

    return merge_arr


print(" ".join(map(str, k_merge_sort(N, flavors, k, 0))))