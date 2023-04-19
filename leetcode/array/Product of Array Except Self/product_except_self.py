from typing import List

# Time = O(n), Space = O(1)
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
		answer = [0] * n

		# Calculate product of all elements to the left of current element
		left_product = 1
		for i in range(n):
			answer[i] = left_product
			left_product *= nums[i]

		# Calculate product of all elements to the right of current element
		right_product = 1
		for i in range(n-1, -1, -1):
			answer[i] *= right_product
			right_product *= nums[i]

		return answer

def test_productExceptSelf():
	sol = Solution()

	assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
	assert sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

	print("All test cases pass")

if __name__ == "__main__":
	test_productExceptSelf()
		