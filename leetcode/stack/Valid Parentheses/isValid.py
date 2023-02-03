# Time: O(n), Space: O(n)
class Solution:
	def isValid(self, s:str) -> bool:
		pair = dict(('()', '[]', '{}'))
		stack = []
		for c in s:
			if c in "([{":
				stack.append(c)
			else:
				if len(stack) == 0:
					return False
				if c != pair[stack.pop()]:
					return False
		return len(stack) == 0

def main():
	a = Solution()
	s1 = "([{}])"
	s2 = "([{}]"

	print(a.isValid(s1))
	print(a.isValid(s2))

if __name__ == "__main__":
	main()
