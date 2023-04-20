# Time: O(n), Space: O(n)
class Solution:
	def longestPalindrome(self, s:str) -> int:
		freq = {}
		for c in s:
			freq[c] = freq.get(c, 0) + 1
		
		length = 0
		for c, f in freq.items():
			length += f // 2 * 2
		
		if length < len(s):
			length += 1
		
		return length

def test_longestPalindrome():
	sol = Solution()

	assert sol.longestPalindrome("catdogcar") == 5
	assert sol.longestPalindrome("a") == 1

	print("All test cases pass")

if __name__ == "__main__":
	test_longestPalindrome()