# Time: O(M+N), Space: O(M+N)
class Solution:
	def backspaceCompare(self, s: str, t: str) -> bool:
		def build(S):
			stack = []
			for c in S:
				if c != '#':
					stack.append(c)
				elif stack:
					stack.pop()
			return "".join(stack)
		return build(s) == build(t)

def main():
	a = Solution()
	result = a.backspaceCompare("ab#c", "ad#c")
	print(result)

if __name__ == "__main__":
	main()
