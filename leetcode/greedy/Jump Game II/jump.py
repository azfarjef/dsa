from typing import List

# Time: O(n), Space: O(1)
class Solution:
	def jump(self, nums: List[int]) -> int:
		l, r = 0, 0
		res = 0

		while r < (len(nums) - 1):
			maxJump = 0
			for i in range(l, r + 1):
				maxJump = max(maxJump, i + nums[i])
			l = r + 1
			r = maxJump
			res += 1
		return res

def test_jump():
	assert Solution().jump([2,3,1,1,4]) == 2
	assert Solution().jump([2,3,0,1,4]) == 2

	print("All tests pass")

if __name__ == "__main__":
	test_jump()
