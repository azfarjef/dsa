from typing import List

# Time: O(n), Space: O(n)
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		dp = {} # key: (i, buying), val: max_profit

		def dfs(i, buying):
			if i >= len(prices):
				return 0
			if (i, buying) in dp:
				return dp[(i, buying)]
			
			cooldown = dfs(i + 1, buying)
			if buying:
				buy = dfs(i + 1, not buying) - prices[i]
				dp[(i, buying)] = max(buy, cooldown)
			else:
				sell = dfs(i + 2, not buying) + prices[i]
				dp[(i, buying)] = max(sell, cooldown)
			return dp[(i, buying)]
		
		return dfs(0, True)

def test_maxProfit():
	assert Solution().maxProfit([1,2,3,0,2]) == 3
	assert Solution().maxProfit([1]) == 0

	print("All tests passed")

if __name__ == "__main__":
	test_maxProfit()
