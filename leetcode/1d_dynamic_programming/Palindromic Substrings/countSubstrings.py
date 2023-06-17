# Time: O(n^2), Space: O(1)
class Solution:
	def countSubstrings(self, s: str) -> int:
		res = 0

		def count_palindromes(l, r):
			nonlocal res

			while (l >= 0 and r < len(s) and s[l] == s[r]):
				res += 1
				l -= 1
				r += 1

		for i in range(len(s)):
			count_palindromes(i, i)
			count_palindromes(i, i + 1)

		return res

def test_countSubstrings():
	assert Solution().countSubstrings("abc") == 3
	assert Solution().countSubstrings("aaa") == 6

	print("All tests passed")

if __name__ == "__main__":
	test_countSubstrings()
