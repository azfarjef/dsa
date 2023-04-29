from typing import List
import collections

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		ans = collections.defaultdict(list)

		for s in strs:
			count = [0] * 26
			for c in s:
				count[ord(c) - ord("a")] += 1
			ans[tuple(count)].append(s)
		return ans.values()

def test_groupAnagrams():
	print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
	assert Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["eat","tea","ate"],["tan","nat"],["bat"]]
	assert Solution().groupAnagrams([""]) == [['']]
	assert Solution().groupAnagrams(["a"]) == [["a"]]

	print("All tests passed")

if __name__ == "__main__":
	test_groupAnagrams()