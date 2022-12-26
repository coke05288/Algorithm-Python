## 그리디 알고리즘
## 백준 1343 폴리노미오
## https://www.acmicpc.net/problem/1343

board = input()


def solution(_board):
    _board = _board.replace("XXXX", "AAAA")
    _board = _board.replace("XX", "BB")

    if "X" in _board:
        return -1
    else:
        return _board

print(solution(board))