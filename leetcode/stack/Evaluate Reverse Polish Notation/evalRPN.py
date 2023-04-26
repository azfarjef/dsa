from typing import List

# Time: O(n), Space: O(n)
class Solution:
	def evalRPN(self, tokens: List[str]) -> int:
		stack = []
		for token in tokens:
			if token in ["+", "-", "*", "/"]:
				op2 = stack.pop()
				op1 = stack.pop()
				if token == "+":
					stack.append(op1 + op2)
				elif token == "-":
					stack.append(op1 - op2)
				elif token == "*":
					stack.append(op1 * op2)
				else:
					stack.append(int(op1 / op2))
			else:
				stack.append(int(token))
		return stack[0]

def test_evalRPN():
	sol = Solution()

	assert sol.evalRPN(["2","1","+","3","*"]) == 9
	assert sol.evalRPN(["4","13","5","/","+"]) == 6
	assert sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22

	print("All test cases pass")

if __name__ == "__main__":
	test_evalRPN()
