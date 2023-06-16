from typing import List

# Time: O(n), Space: O(1)
class Solution:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		cost.append(0)

		for i in range(len(cost) - 3, -1, -1):
			cost[i] += min(cost[i+1], cost[i+2])

		return min(cost[0], cost[1])

def test_minCostClimbingStairs():
	assert Solution().minCostClimbingStairs([10, 15, 20]) == 15
	assert Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

	print("All tests passed")

if __name__ == "__main__":
	test_minCostClimbingStairs()
