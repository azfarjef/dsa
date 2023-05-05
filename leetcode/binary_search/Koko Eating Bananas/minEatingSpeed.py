from typing import List
import math

# Time: O(log(max(p)) * p), Space: O(1)
class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		l, r = 1, max(piles)
		res = r

		while l <= r:
			k = (l + r) // 2

			totalTime = 0
			for p in piles:
				totalTime += math.ceil(p/k)
			if totalTime <= h:
				res = min(res, k)
				r = k - 1
			else:
				l = k + 1
		return res

def test_minEatingSpeed():
	assert Solution().minEatingSpeed([3,6,7,11], 8) == 4
	assert Solution().minEatingSpeed([30,11,23,4,20], 5) == 30
	assert Solution().minEatingSpeed([30,11,23,4,20], 6) == 23

	print("All tests pass")

if __name__ == "__main__":
	test_minEatingSpeed()
