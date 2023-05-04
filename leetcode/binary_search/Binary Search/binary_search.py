from typing import List

# Time: O(log n), means how many times we can divide n by 2, Space: O(1)
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		l, r = 0, len(nums) - 1

		while l <= r:
			m = l + ((r - l) // 2) # (l + r) // 2 can lead to overflow
			if nums[m] > target:
				r = m - 1
			elif nums[m] < target:
				l = m + 1
			else:
				return m
		return -1

def test_search():
	assert Solution().search([-1,0,3,5,9,12], 9) == 4
	assert Solution().search([-1,0,3,5,9,12], 2) == -1

	print("All tests pass")

if __name__ == "__main__":
	test_search()