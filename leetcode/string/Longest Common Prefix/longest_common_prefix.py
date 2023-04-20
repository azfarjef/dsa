from typing import List

# Time: O(nm log m), n is the length of the list, m is the length of the longest string
# Space: O(1)
class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		if not strs:
			return ""

		strs.sort()

		first = strs[0]
		last = strs[-1]
		for i, char in enumerate(first):
			if last[i] != char:
				return first[:i]

		return first

def test_longestCommonPrefix():
	sol = Solution()

	assert sol.longestCommonPrefix(["flower", "chickenny", "flo", "flood"]) == ""
	assert sol.longestCommonPrefix(["flower","flow","flight"]) == "fl"

	print("All test cases pass")

if __name__ == "__main__":
	test_longestCommonPrefix()