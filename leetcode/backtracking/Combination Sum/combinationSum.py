from typing import List

# Time: O(2^target), Space: O(2^n)
class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		res = []

		def dfs(i, cur, total):
			if total == target:
				res.append(cur.copy())
				return
			if i >= len(candidates) or total > target:
				return

			cur.append(candidates[i])
			dfs(i, cur, total + candidates[i])
			cur.pop()
			dfs(i + 1, cur, total)

		dfs(0, [], 0)
		return res

def test_combinationSum():
	sol = Solution()
	assert sol.combinationSum([2,3,6,7], 7) == [[2,2,3],[7]]
	assert sol.combinationSum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]]
	assert sol.combinationSum([2], 1) == []
	assert sol.combinationSum([1], 1) == [[1]]
	assert sol.combinationSum([1], 2) == [[1,1]]
	print("All tests passed!")

if __name__ == "__main__":
	test_combinationSum()