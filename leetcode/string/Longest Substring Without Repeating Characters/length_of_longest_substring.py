# Time: O(n), Space: O(1), size of ASCII character set (128)
# Sliding window technique
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		n = len(s)
		i, j = 0, 0
		max_len = 0
		char_set = set()
		while i < n and j < n:
			if s[j] not in char_set:
				char_set.add(s[j])
				j += 1
				max_len = max(max_len, j - i)
			else:
				char_set.remove(s[i])
				i += 1
		return max_len

def test_lengthOfLongestSubstring():
	sol = Solution()

	assert sol.lengthOfLongestSubstring("abcabcbb") == 3
	assert sol.lengthOfLongestSubstring("bbbbb") == 1
	assert sol.lengthOfLongestSubstring("pwwkew") == 3

	print("All test cases pass")

if __name__ == "__main__":
	test_lengthOfLongestSubstring()
