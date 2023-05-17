from typing import List

# Time: O(n.2^n), Space: O(2^n)
class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		res = []
		nums.sort() # O(nlogn)

		def backtrack(i, subset):
			if i == len(nums):
				res.append(subset[::])
				return
			
			# decision to include nums[i]
			subset.append(nums[i])
			backtrack(i + 1, subset)
			subset.pop()
			# decision to not include nums[i]
			while i + 1 < len(nums) and nums[i] == nums[i + 1]:
				i += 1
			backtrack(i + 1, subset)

		backtrack(0, [])
		return res

def test_subsetsWithDup():
	sol = Solution()
	assert sorted(sol.subsetsWithDup([1,2,2])) == sorted([[],[1],[1,2],[1,2,2],[2],[2,2]])
	assert sorted(sol.subsetsWithDup([0])) == sorted([[],[0]])

	print("All tests passed!")

if __name__ == "__main__":
	test_subsetsWithDup()