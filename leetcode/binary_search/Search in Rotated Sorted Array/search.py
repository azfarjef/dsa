from typing import List

# Time: O(logn), Space: O(1)
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		l, r = 0, len(nums) - 1
		while l <= r:
			m = (l + r) // 2
			if target == nums[m]:
				return m
			# left sorted portion
			if nums[l] <= nums[m]:
				if target > nums[m] or target < nums[l]:
						l = m + 1
				else:
						r = m - 1
			#right sorted portion
			else:
				if target < nums[m] or target > nums[r]:
						r = m - 1
				else:
						l = m + 1
		return -1

def test_search():
	assert Solution().search([4,5,6,7,0,1,2], 0) == 4
	assert Solution().search([4,5,6,7,0,1,2], 3) == -1
	assert Solution().search([1], 0) == -1

	print("All tests passed")

if __name__ == "__main__":
	test_search()