from typing import List
from collections import defaultdict, Counter
import copy

# Time: O(mn.4^L), Space: O(mn + L)
class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		rows, cols = len(board), len(board[0])
		boardDic = defaultdict(int)
		for i in range(rows):
			for j in range(cols):
				boardDic[board[i][j]] += 1

		wordDic = Counter(word)
		for c in wordDic:
			if c not in boardDic or boardDic[c] < wordDic[c]:
				return False

		for i in range(rows):
			for j in range(cols):
				if board[i][j] == word[0]:
					if self.dfs(i, j, 0, board, word):
						return True

		return False

	def dfs(self, i, j, k, board, word):
		if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or k >= len(word) or word[k] != board[i][j]:
			return False

		if k == len(word) - 1:
			return True

		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

		for x, y in directions:
			tmp = board[i][j]
			board[i][j] = -1

			if self.dfs(i + x, j + y, k + 1, board, word):
				return True

			board[i][j] = tmp

def test_exist():
	board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
	word1 = "ABCCED"
	word2 = "SEE"
	word3 = "ABCB"

	assert Solution().exist(copy.deepcopy(board), word1) == True
	assert Solution().exist(copy.deepcopy(board), word2) == True
	assert Solution().exist(board, word3) == False

	print("All tests passed!")

if __name__ == "__main__":
	test_exist()