# Time: O(m*n), Space: O(n)
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		# initialize the last row
		row = [1] * n

		for i in range(m -1):
			newRow = [1] * n
			for j in range(n - 2, -1, -1):
				newRow[j] = newRow[j + 1] + row[j]
			row = newRow
		return row[0]

def test_uniquePaths():
	assert Solution().uniquePaths(3, 2) == 3
	assert Solution().uniquePaths(7, 3) == 28
	assert Solution().uniquePaths(3, 3) == 6

	print("All tests passed.")

if __name__ == "__main__":
	test_uniquePaths()