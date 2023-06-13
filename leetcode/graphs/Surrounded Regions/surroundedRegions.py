from typing import List

# Time: O(m*n), Space: O(m*n)
class Solution:
	def solve(self, board: List[List[str]]) -> None:
		ROWS, COLS = len(board), len(board[0])

		def dfs_capture(r, c):
			if (r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != 'O'):
				return
			board[r][c] = 'T'
			dfs_capture(r + 1, c)
			dfs_capture(r - 1, c)
			dfs_capture(r, c + 1)
			dfs_capture(r, c - 1)

		# Capture unsurrounded regions (Change O to T)
		for r in range(ROWS):
			for c in range(COLS):
				if board[r][c] == 'O' and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
					dfs_capture(r, c)

		# Capture surrounded regions (Change O to X)
		for r in range(ROWS):
			for c in range(COLS):
				if board[r][c] == 'O':
					board[r][c] = 'X'
			
		# Uncapture unsurrounded regions (Change T to O)
		for r in range(ROWS):
			for c in range(COLS):
				if board[r][c] == 'T':
					board[r][c] = 'O'

def test_solve():
	board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
	result = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

	Solution().solve(board)
	assert board == result

	print("All tests passed.")

if __name__ == "__main__":
	test_solve()