# Time: O(26n), Space: O(1)
class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		count = {}
		res = 0

		l = 0
		maxf = 0
		for r in range(len(s)):
			count[s[r]] = 1 + count.get(s[r], 0)
			maxf = max(maxf, count[s[r]])

			if (r - l + 1) - maxf > k:
				count[s[l]] -= 1
				l += 1

			res = max(res, r - l + 1)
		return res

def test_characterReplacement():
	assert Solution().characterReplacement("ABAB", 2) == 4
	assert Solution().characterReplacement("AABABBA", 1) == 4

	print("All tests passed.")

if __name__ == "__main__":
	test_characterReplacement()
