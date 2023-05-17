from typing import List

# Time: O(2^n), Space: O(2^n)
class Solution:
	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		candidates.sort() # O(nlogn)

		res = []

		def backtrack(cur, pos, target):
			if target == 0:
				res.append(cur[:])
				return
			if target <= 0:
				return

			prev = -1
			for i in range(pos, len(candidates)):
				if candidates[i] == prev:
					continue
				cur.append(candidates[i])
				backtrack(cur, i + 1, target - candidates[i])
				cur.pop()
				prev = candidates[i]

		backtrack([], 0, target)
		return res

def test_combinationSum2():
	assert sorted(Solution().combinationSum2([10,1,2,7,6,1,5], 8)) == sorted([[1,1,6],[1,2,5],[1,7],[2,6]])
	assert sorted(Solution().combinationSum2([2,5,2,1,2], 5)) == sorted([[1,2,2],[5]])

	print("All tests passed!")

if __name__ == "__main__":
	test_combinationSum2()