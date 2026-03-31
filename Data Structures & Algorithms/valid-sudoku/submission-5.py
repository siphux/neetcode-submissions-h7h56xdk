class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            dic = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in dic:
                    dic.add(board[i][j])
                else:
                    return False
        for j in range(len(board)):
            dic = set()
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in dic:
                    dic.add(board[i][j])
                else:
                    return False
        for block_i in range(0, 9, 3):
            for block_j in range(0, 9, 3):
                dic = set()
                for i in range(block_i, block_i + 3):
                    for j in range(block_j, block_j + 3):
                        val = board[i][j]
                        if val == ".":
                            continue
                        if val in dic:
                            return False
                        dic.add(val)
            

        return True