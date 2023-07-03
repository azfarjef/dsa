from typing import List

class Solution:
	def change(self, amount: int, coins: List[int]) -> int:
		# MEMOIZATION, Time: O(n*m), Space: O(n*m)
		cache = {}

		def dfs(i, a):
			if a == amount:
				return 1
			if a > amount:
				return 0
			if i >= len(coins):
				return 0
			if (i, a) in cache:
				return cache[(i, a)]
			
			cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
			return cache[(i, a)]
		
		return dfs(0, 0)
	
def test_change():
	assert Solution().change(5, [1,2,5]) == 4
	assert Solution().change(3, [2]) == 0
	assert Solution().change(10, [10]) == 1

	print("All tests passed")

if __name__ == "__main__":
	test_change()
