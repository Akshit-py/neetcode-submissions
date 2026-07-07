class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[0]*9
        cols=[0]*9
        subMat=[0]*9
        for i in range(9):
            for j in range(9):
                
                if board[i][j]=='.':
                    continue
                
                val=int(board[i][j])
                pos=1 << (val-1)

                if (rows[i] & pos) > 0:
                    return False
                rows[i] |= pos

                if (cols[j] & pos) > 0:
                    return False
                cols[j] |= pos

                idx=(i//3)*3+j//3
                if (subMat[idx] & pos) > 0:
                    return False
                subMat[idx] |= pos

        return True

        