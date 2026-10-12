class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if board [r][c] != "O":
                return

            board[r][c] = "#"

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr = r+dr
                nc = c+dc
                dfs(nr, nc)

        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
