## 그리디 알고리즘
## 백준 1343 폴리노미오
## https://www.acmicpc.net/problem/1343

board = input()

def solution(board):
    board = board.replace("XXXX", "AAAA")
    board = board.replace("XX", "BB")

    if "X" in board:
        return -1
    else:
        return board

print(solution(board))