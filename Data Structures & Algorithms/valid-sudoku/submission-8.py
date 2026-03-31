class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            dic = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in dic:
                    return False
                dic.add(board[i][j])
        
        for j in range(len(board)):
            dic = set()
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in dic:
                    return False
                dic.add(board[i][j])

        for block_i in range(0, 9, 3):
            for block_j in range(0, 9, 3):
                dic = set()
                for i in range(block_i, block_i + 3):
                    for j in range(block_j, block_j + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in dic:
                            return False
                        dic.add(board[i][j])
            

        return True