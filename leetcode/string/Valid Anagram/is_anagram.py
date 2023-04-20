# Time: O(n), Space: O(k), k is the number of unique character in the string
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		
		count = {}
		for c in s:
			count[c] = count.get(c, 0) + 1

		for c in t:
			if c not in count:
				return False
			count[c] -= 1
			if count[c] == 0:
				del count[c]

		return len(count) == 0

def test_isAnagram():
	sol = Solution()

	assert sol.isAnagram("anagram", "nagaram") == True
	assert sol.isAnagram("rat", "car") == False

	print("All test cases pass")

if __name__ == "__main__":
	test_isAnagram()
