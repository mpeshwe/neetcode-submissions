class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False]*len(board[0])] * len(board)
        def backtrack(row, col, index) : 
            if index >= len(word) :
                return True
            if row >=len(board) or row < 0 or col >= len(board[0]) or col < 0 :
                return False
            if board[row][col] != word[index] :
                return False
            # else :
            #     visited[row][col] = True
            #     up=False
            #     down=False
            #     left=False
            #     right=False
            #     if not visited[row-1][col] and row-1 > 0 : 
            #         up = backtrack(row-1,col,index+1)
            #     if (row+1) >= len(board) and (not visited[row+1][col] ) :
            #         down = backtrack(row+1,col,index+1)
            #     if not visited[row][col-1] and col-1 > 0:
            #         left = backtrack(row,col-1,index+1)
            #     if not visited[row][col+1] and (col+1) < len(board[0]) :
            #         right = backtrack(row,col+1,index+1)

            #     return up or down or left or right
            temp =  board[row][col]
            board[row][col] = "@"

            if backtrack(row-1, col, index+1) or backtrack(row+1, col, index+1) or backtrack(row, col-1, index+1) or backtrack(row, col+1, index+1):
                return True
            board[row][col] = temp
            return False

        # ans = False
        for row in range(len(board)) :
            for col in range(len(board[0])) : 
                if board[row][col] == word[0] :
                    if backtrack(row,col,0) :
                        return True
        return False