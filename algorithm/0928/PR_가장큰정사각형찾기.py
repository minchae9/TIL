"""
테스트 케이스는 통과하였으나,
효율성 테스트를 통과하지 못함 (시간 초과).
"""

def solution(board):
    mx = 0
    for r in range(len(board)):
        if len(board)-r < mx:
            break
        for c in range(len(board[0])):
            if len(board[0]) - c < mx:
                break
            if board[r][c] == 1:
                i = min(len(board)-r, len(board[0])-c)  # 가능한 최대 크기
                if i == 1:
                    mx = 1
                    break
                if i < mx:
                    continue
                while i > 1:    # 최대 크기부터 내림차순으로 확인함
                    if i < mx:
                        break
                    flag = False
                    for h in range(r, r+i):
                        if flag:
                            break
                        for v in range(c, c+i):
                            if board[h][v] == 0:
                                i -= 1
                                flag = True
                                break
                    else:
                        if i > mx:
                            mx = i
                        break
    return mx*mx