from typing import List

# Time: O(n) Space: O(1)
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		min_price = float('inf')
		max_profit = 0
		for i in range(len(prices)):
			if prices[i] < min_price:
				min_price = prices[i]
			elif prices[i] - min_price > max_profit:
				max_profit = prices[i] - min_price
		return max_profit

def main():
	a = Solution()
	prices = [7,1,5,3,6,4]

	result = a.maxProfit(prices)
	print(result)

if __name__ == "__main__":
	main()