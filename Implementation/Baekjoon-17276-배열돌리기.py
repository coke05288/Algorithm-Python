## 구현(Implementation)
## Baekjoon 17276 배열돌리기
## https://www.acmicpc.net/problem/17276

T = int(input())

def rotation(n, array, main_diagonal, center_column, sub_diagonal, center_raw, count, clockwise):
    print(main_diagonal)
    print(clockwise)
    
    return array

def solution(n, d):
    array = [list(map(int, input().split())) for _ in range(n)]
    
    abs_d = abs(d)
    count = abs_d//45

    for _ in range(count):
        center_raw = [array[n//2][i] for i in range(n)]
        center_column = [array[i][n//2] for i in range(n)]
        main_diagonal = [array[i][i] for i in range(n)]
        sub_diagonal = [array[i][n-i-1] for i in range(n)]

        if d > 0: # 시계방향
            for idx, val in enumerate(main_diagonal): # 주대각선 > 가운데열
                array[idx][n//2] = val
            for idx, val in enumerate(center_column): # 가운데열 > 부대각선
                array[idx][n-idx-1] = val
            for idx, val in enumerate(reversed(sub_diagonal)): # 부대각선 > 가운데행
                array[n//2][idx] = val
            for idx, val in enumerate(reversed(center_raw)): # 가운데행 > 주대각선
                array[n-idx-1][n-idx-1] = val
        else:
            for idx, val in enumerate(main_diagonal): # 주대각선 > 가운데행
                array[n//2][idx] = val
            for idx, val in enumerate(center_raw): # 가운데행 > 부대각선
                array[n-idx-1][idx] = val
            for idx, val in enumerate(sub_diagonal): # 부대각선 > 가운데열
                array[idx][n//2] = val
            for idx, val in enumerate(reversed(center_column)): # 가운데열 > 주대각선
                array[n-idx-1][n-idx-1] = val
    
    for i in range(n):
        print(" ".join(map(str, array[i])))

for _ in range(T):
    n, d = map(int, input().split())
    solution(n, d)



