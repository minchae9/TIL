def solution(board):
    mx = 0
    k = min(len(board), len(board[0]))
    if k <= 1:	# 한 변이 1을 넘을 수 없는 경우
        for r in range(len(board)):
            for j in range(len(board[0])):
                if board[r][j] == 1:
                    return 1	# 사각형이 존재하면, 1
        else:	# 사각형이 존재하지 않음, 0
            return 0
    else:
        for x in range(1, len(board)):
            for y in range(1, len(board[0])):
                if board[x][y]:
                    board[x][y] = min(board[x][y-1], board[x-1][y-1], board[x-1][y]) + 1
                    if board[x][y] > mx:
                        mx = board[x][y]
        return mx ** 2