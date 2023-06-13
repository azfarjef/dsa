from typing import List

# Time: O(m*n), Space: O(m*n)
class Solution:
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		ROWS, COLS = len(grid), len(grid[0])
		visit = set()

		def dfs(r, c):
			if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r, c) in visit):
				return 0
			
			visit.add((r, c))
			return ( 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))

		area = 0
		for r in range(ROWS):
			for c in range(COLS):
				area = max(area, dfs(r, c))

		return area

def test_maxAreaOfIsland():
	grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

	assert Solution().maxAreaOfIsland(grid) == 6

	print("All test passed")

if __name__ == "__main__":
	test_maxAreaOfIsland()