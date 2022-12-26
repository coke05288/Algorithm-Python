## 그리디 알고리즘
## 백준 1343 폴리노미오
## https://www.acmicpc.net/problem/1343
## 다 되는데 왜 오답인거임?

remove_set = {""}
board = input()
can_board = [i for i in board.split(".") if i not in remove_set]

def check_dot():
    dot_baord = []
    temp = []

    for i in range(len(board)):
        if board[i] == ".":
            temp.append(board[i])
            if i == len(board) - 1:
                dot_baord.append("".join(temp))
        else:
            if temp:
                dot_baord.append("".join(temp))
                temp = []
    

    return dot_baord

def solution(board):
    answer = []
    temp_answer = []

    for u_board in board:
        
        temp_board_num = len(u_board)
        temp_unit_answer = []
        
        while temp_board_num > 0:
            if temp_board_num >= 4:
                temp_unit_answer.append("AAAA")
                temp_board_num -= 4
            elif temp_board_num >= 2:
                temp_unit_answer.append("BB")
                temp_board_num -= 2
            else:
                return -1
        
        temp_answer.append("".join(temp_unit_answer))

    
    cant_board = check_dot()
    
    answer_idx= 0
    dot_idx = 0

    while True:
        if answer_idx == len(temp_answer) and dot_idx == len(cant_board):
            break
        else:
            if answer_idx != len(temp_answer):
                answer.append(temp_answer[answer_idx])
                answer_idx += 1
            if dot_idx != len(cant_board):
                answer.append(cant_board[dot_idx])
                dot_idx += 1

    answer = "".join(answer)

    if "A" not in answer and "B" not in answer:
        return -1
    else:
        return "".join(answer)

print(solution(can_board))