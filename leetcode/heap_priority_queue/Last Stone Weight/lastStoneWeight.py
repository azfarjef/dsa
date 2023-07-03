from typing import List
import heapq

# Time: O(n*log n), Space: O(n)
class Solution:
	def lastStoneWeight(self, stones: List[int]) -> int:
		stones = [-s for s in stones]
		heapq.heapify(stones)

		while len(stones) > 1:
			x = heapq.heappop(stones)
			y = heapq.heappop(stones)

			if y > x:
				heapq.heappush(stones, x - y)

		return abs(stones[0]) if stones else 0

def test_lastStoneWeight():
	assert Solution().lastStoneWeight([2,7,4,1,8,1]) == 1
	assert Solution().lastStoneWeight([2,2]) == 0

	print("All tests passed.")

if __name__ == "__main__":
	test_lastStoneWeight()
