from typing import List

# Kadane's Algorithm
# Time: O(n), Space: O(1)
class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		res = nums[0]
		total = 0

		for num in nums:
			total += num
			res = max(res, total)
			if total < 0:
				total = 0
		return res

def test_maxSubArray():
	assert Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
	assert Solution().maxSubArray([1]) == 1
	assert Solution().maxSubArray([5,4,-1,7,8]) == 23

	print("All tests passed.")

if __name__ == "__main__":
	test_maxSubArray()
