
def check_block(m, n, board):

    blocks = set()

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == board[i][j-1] == board[i-1][j-1] == board[i-1][j] != '0':
                blocks |= set([(i,j), (i, j-1), (i-1, j-1), (i-1, j)])

    for i, j in blocks:
        board[i][j] = '0'

    for idx, row in enumerate(board):
        empty = list('0' * row.count('0'))
        not_empty = []
        
        for blk in row:
            if blk != '0':
                not_empty.append(blk)

        board[idx] = empty + not_empty

    return len(blocks)


def solution(m, n, board):
    answer = 0

    temp_board = list(map(list, zip(*board)))

    while True:
        temp_count = check_block(m, n, temp_board)
        
        if temp_count == 0 : return answer
        
        answer += temp_count 

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))