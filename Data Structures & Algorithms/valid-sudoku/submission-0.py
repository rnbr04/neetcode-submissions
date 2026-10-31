class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check sub-box validity
        N = 9
        
        # iterate through the sudoku
        for i in range(N):
            for j in range(N):
                # if first element of sub-box
                if (i % 3 == 0) and (j % 3 == 0):
                    # invalid_sub_box
                    if not self.isValidSubBox(i, j, board):
                        return False
                    
                # since valid_sub_box
                # check the respective row
                hash_set = set()
                for k in range(N):
                    if board[i][k] == ".":
                        continue
                    # if any duplicate
                    if board[i][k] in hash_set:
                        return False
                    hash_set.add(board[i][k])
                # check the respective column
                hash_set = set()
                for k in range(N):
                    if board[k][j] == ".":
                        continue
                    # if any duplicate
                    if board[k][j] in hash_set:
                        return False
                    hash_set.add(board[k][j])
                
        return True
    
    def isValidSubBox(self, row: int, col: int, board: List[List[str]]) -> bool:
        hash_set = set()
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if board[i][j] == ".":
                        continue
                if board[i][j] in hash_set:
                    return False
                hash_set.add(board[i][j])
        return True 