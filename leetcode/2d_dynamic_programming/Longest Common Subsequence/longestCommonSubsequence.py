# Time: O(m*n), Space: O(m*n)
class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

		for i in range(len(text1) - 1, -1, -1):
			for j in range(len(text2) - 1, -1, -1):
				if text1[i] == text2[j]:
					dp[i][j] = 1 + dp[i + 1][j + 1]
				else:
					dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
		return dp[0][0]

def test_longestCommonSubsequence():
	assert Solution().longestCommonSubsequence("abcde", "ace") == 3
	assert Solution().longestCommonSubsequence("abc", "abc") == 3
	assert Solution().longestCommonSubsequence("abc", "def") == 0

	print("All tests passed.")

if __name__ == "__main__":
	test_longestCommonSubsequence()
