# Time: O(n), Space: O(1)
class Solution:
	def myAtoi(self, s: str) -> int:
		s = s.lstrip()

		if not s:
			return 0

		sign = 1
		result = 0

		if s[0] == '-':
			sign = -1
			s = s[1:]
		elif s[0] == '+':
			s = s[1:]

		for char in s:
			if char.isdigit():
				result = result * 10 + int(char)
			else:
				break

		result *= sign

		if result < -2**31:
			return -2**31
		elif result > 2**31 - 1:
			return 2**31 - 1
		else:
			return result

def test_myAtoi():
	sol = Solution()

	assert sol.myAtoi("42") == 42
	assert sol.myAtoi("  -42") == -42
	assert sol.myAtoi("42 with words") == 42

	print("All test cases pass")

if __name__ == "__main__":
	test_myAtoi()
