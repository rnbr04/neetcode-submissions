from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        row = defaultdict(set)
        col = defaultdict(set)
        sub_box = defaultdict(set)

        for r in range(N):
            for c in range(N):
                ele = board[r][c]
                if ele == ".":
                    continue
                
                if (ele in row[r] or
                    ele in col[c] or
                    ele in sub_box[(r//3, c//3)]):
                    return False
                
                row[r].add(ele)
                col[c].add(ele)
                sub_box[(r//3, c//3)].add(ele)
        return True