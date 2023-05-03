from typing import List

# Time and space: O(4^n / sqrt(n))
class Solution:
	def generateParentheses(self, n: int) -> List[str]:
		stack = []
		res = []

		def backtrack(openN, closeN):
			if openN == closeN == n:
				res.append("".join(stack))
				return

			if openN < n:
				stack.append("(")
				backtrack(openN + 1, closeN)
				stack.pop()
			
			if closeN < openN:
				stack.append(")")
				backtrack(openN, closeN + 1)
				stack.pop()
			
		backtrack(0, 0)
		return res

def test_generateParentheses():
	assert Solution().generateParentheses(3) == ["((()))","(()())","(())()","()(())","()()()"]
	assert Solution().generateParentheses(1) == ["()"]

	print("All tests pass")

if __name__ == "__main__":
	test_generateParentheses()