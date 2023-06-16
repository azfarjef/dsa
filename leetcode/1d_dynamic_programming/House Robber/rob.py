from typing import List

# Time: O(n), Space: O(1)
class Solution:
	def rob(self, nums: List[int]) -> int:
		rob1, rob2 = 0, 0

		for n in nums:
			temp = max(rob1 + n, rob2)
			rob1 = rob2
			rob2 = temp
		
		return rob2

def test_rob():
	assert Solution().rob([1, 2, 3, 1]) == 4
	assert Solution().rob([2, 7, 9, 3, 1]) == 12

	print("All tests passed")

if __name__ == "__main__":
	test_rob()
