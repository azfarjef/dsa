# Time: O(n^2), Space: O(1)
class Solution:
	def longestPalindrome(self, s: str) -> str:
		res = ""
		resLen = 0

		def calculate_length(l, r):
			nonlocal res, resLen
			
			while (l >= 0 and r < len(s) and s[l] == s[r]):
				if (r - l + 1 > resLen):
					res = s[l:r+1]
					resLen = r - l + 1
				l -= 1
				r += 1

		for i in range(len(s)):
			l, r = i, i

			calculate_length(l, r)
			calculate_length(l, r + 1)

		return res

def test_longestPalindrome():
	assert Solution().longestPalindrome("babad") == "bab"
	assert Solution().longestPalindrome("cbbd") == "bb"

	print("All tests passed")

if __name__ == "__main__":
	test_longestPalindrome()
