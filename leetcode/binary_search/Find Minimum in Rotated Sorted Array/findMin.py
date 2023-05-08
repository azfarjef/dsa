from typing import List

# Time: O(logn), Space: O(1)
class Solution:
	def findMin(self, nums: List[int]) -> int:
		start, end = 0, len(nums) - 1
		curr_min = float('inf')

		while start < end:
			mid = (start + end) // 2
			curr_min = min(curr_min, nums[mid])

			if nums[mid] > nums[end]:
				start = mid + 1
			else:
				end = mid - 1
		return min(curr_min, nums[start])

def test_findMin():
	assert Solution().findMin([3,4,5,1,2]) == 1
	assert Solution().findMin([4,5,6,7,0,1,2]) == 0

	print("All tests passed.")

if __name__ == "__main__":
	test_findMin()