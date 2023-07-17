from typing import List

# Time: O(n), Space: O(1)
class Solution:
	def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
		if sum(gas) < sum(cost):
			return -1

		total = 0
		res = 0
		
		for i in range(len(gas)):
			total += gas[i] - cost[i]
			if total < 0:
				total = 0
				res = i + 1

		return res

class Solution2:
	def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
		start, end = len(gas) - 1, 0
		total = gas[start] - cost[start]

		while start >= end:
			while total < 0 and start >= end:
				start -= 1
				total += gas[start] - cost[start]
			if start == end:
				return start
			total += gas[end] - cost[end]
			end += 1
		return -1

def test_canCompleteCircuit():
	assert Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) == 3
	assert Solution().canCompleteCircuit([2,3,4], [3,4,3]) == -1

	print("All tests passed")

if __name__ == "__main__":
	test_canCompleteCircuit()
