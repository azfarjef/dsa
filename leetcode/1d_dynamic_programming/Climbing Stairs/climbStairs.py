# Time: O(n), Space: O(1)
class Solution:
	def climbStairs(self, n: int) -> int:
		one, two = 1, 1

		for i in range(n-1):
			temp = one
			one = one + two
			two = temp
		
		return one

def test_climbStairs():
	assert Solution().climbStairs(2) == 2
	assert Solution().climbStairs(3) == 3
	assert Solution().climbStairs(5) == 8

	print("All tests passed")

if __name__ == "__main__":
	test_climbStairs()
