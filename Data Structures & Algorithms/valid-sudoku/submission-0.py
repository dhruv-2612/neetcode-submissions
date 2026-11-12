class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            flags = [False] * 10
            for j in range(9):
                if board[i][j] != "." and flags[int(board[i][j])] != True:
                    flags[int(board[i][j])] = True
                elif board[i][j] == ".":
                    continue
                else:
                    return False
        for i in range(9):
            flags = [False] * 10
            for j in range(9):
                if board[j][i] != "." and flags[int(board[j][i])] != True:
                    flags[int(board[j][i])] = True
                elif board[j][i] == ".":
                    continue
                else:
                    return False
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                flags = [False] * 10
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] != "." and flags[int(board[k][l])] != True:
                            flags[int(board[k][l])] = True
                        elif board[k][l] == ".":
                            continue
                        else:
                            return False

        return True
                    

        