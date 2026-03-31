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
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                dic = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        val = board[i][j]
                        if val == ".":
                            continue
                        if val in dic:
                            return False
                        dic.add(val)
            

        return True