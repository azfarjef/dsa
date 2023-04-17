from typing import List

# Time = O(n), Space = O(1)
class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		i = 0
		for j in range(len(nums)):
			if nums[j] != 0:
				nums[i], nums[j] = nums[j], nums[i]
				i += 1

def test_moveZeroes():
	sol = Solution()

	nums1 = [0, 1, 0, 3, 12]
	sol.moveZeroes(nums1)
	assert nums1 == [1, 3, 12, 0, 0]

	nums2 = [0]
	sol.moveZeroes(nums2)
	assert nums2 == [0]

	nums3 = [1, 2, 3, 4, 5]
	sol.moveZeroes(nums3)
	assert nums3 == [1, 2, 3, 4, 5]

	nums4 = [0, 0, 0, 0, 1 ,2, 3]
	sol.moveZeroes(nums4)
	assert nums4 == [1, 2, 3, 0, 0, 0, 0]

	print("All test cases pass")

if __name__ == "__main__":
	test_moveZeroes()