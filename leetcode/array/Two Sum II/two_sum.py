from typing import List

# Time: O(n), Space: O(1)
class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		l, r = 0, len(numbers) - 1

		while l < r:
			curSum = numbers[l] + numbers[r]

			if curSum > target:
				r -= 1
			elif curSum < target:
				l += 1
			else:
				return [l + 1, r + 1]

def test_twoSum():
	 assert Solution().twoSum([2,7,11,15], 9) == [1,2]
	 assert Solution().twoSum([2,3,4], 6) == [1,3]
	 assert Solution().twoSum([-1,0], -1) == [1,2]

	 print("All tests pass")

if __name__ == "__main__":
	test_twoSum()
