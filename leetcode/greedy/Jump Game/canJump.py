from typing import List

# Time: O(n), Space: O(1)
class Solution:
	def canJump(self, nums: List[int]) -> bool:
		goal = len(nums) - 1

		for i in range(len(nums) - 2, -1, -1):
			if i + nums[i] >= goal:
				goal = i
		
		return goal == 0

def test_canJump():
	assert Solution().canJump([2,3,1,1,4]) == True
	assert Solution().canJump([3,2,1,0,4]) == False
	assert Solution().canJump([0]) == True

	print("All tests passed.")

if __name__ == "__main__":
	test_canJump()
