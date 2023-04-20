# Time: O(n), Space: O(1)
class Solution:
	def isPalindrome(self, s: str) -> bool:
		s = ''.join(filter(str.isalnum, s.lower()))

		left, right = 0, len(s) - 1
		while left < right:
			if s[left] != s[right]:
				return False
			left += 1
			right -= 1
		return True

def test_isPalindrome():
	sol = Solution()

	assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
	assert sol.isPalindrome("race a car") == False
	assert sol.isPalindrome(" ") == True

	print("All test cases pass")

if __name__ == "__main__":
	test_isPalindrome()
