class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            r = []
            for j in range(9):
                if board[i][j] in set(r) and board[i][j] != '.':
                    return False
                else:
                    r.append(board[i][j])

            c = []
            for j in range(9):
                if board[j][i] in set(c) and board[j][i] != '.':
                    return False
                else:
                    c.append(board[j][i])
        boxR = 0
        boxC = 0
        i = 0
        Box = []
        end = False
        while boxR * 3 + 3 != 12:
            for j in range(boxC * 3, boxC * 3 + 3):
                if board[i][j] in set(Box) and board[i][j] != '.':
                    return False
                else:
                    Box.append(board[i][j])
                if len(Box) == 9:
                    boxR += 1
                    Box = []
                    if boxR == 3 or boxR == 6:
                        boxC += 1
                        boxR = 0
                        i = -1
                        if j == 8:
                            end = True
                            break
            if end:
                break
            i += 1
        return True
