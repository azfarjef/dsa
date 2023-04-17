from typing import List

# Time = O(n), Space = O(n)
class Solution:
	def sortedSquares(self, nums: List[int]) -> List[int]:
		n = len(nums)
		result = [0] * n
		left, right = 0, n - 1
		for i in range(n - 1, -1, -1):
			if abs(nums[left]) > abs(nums[right]):
				result[i] = nums[left] ** 2
				left += 1
			else:
				result[i] = nums[right] ** 2
				right -= 1
		return result

def test_sortedSquares():
	sol = Solution()

	nums1 = [-4, -1, 0, 3, 10]
	print(sol.sortedSquares(nums1))
	assert sol.sortedSquares(nums1) == [0, 1, 9, 16, 100]
	
	nums1 = [-7, -3, 2, 3, 11]
	assert sol.sortedSquares(nums1) == [4, 9, 9, 49, 121]

	nums1 = [0, 1, 2, 3, 4]
	assert sol.sortedSquares(nums1) == [0, 1, 4, 9, 16]

	print("All test cases pass")

if __name__ == "__main__":
	test_sortedSquares()
