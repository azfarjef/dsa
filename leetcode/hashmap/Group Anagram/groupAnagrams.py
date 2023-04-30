from typing import List
import collections

# Time: O(n k log k), Space: O(n * k) 
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
	result = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
	expected = [["ate","eat","tea"],["nat","tan"],["bat"]]
	assert sorted(map(sorted, result)) == sorted(map(sorted, expected))
	
	result = Solution().groupAnagrams([""])
	expected = [[""]]
	assert sorted(map(sorted, result)) == sorted(map(sorted, expected))
	
	result = Solution().groupAnagrams(["a"])
	expected = [["a"]]
	assert sorted(map(sorted, result)) == sorted(map(sorted, expected))

	print("All tests passed")


if __name__ == "__main__":
	test_groupAnagrams()
