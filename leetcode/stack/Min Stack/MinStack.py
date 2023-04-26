# Time: O(1), Space: O(n)
class MinStack:
	def __init__(self):
		self.stack = []
		self.min_stack = []

	def push(self, val: int) -> None:
		self.stack.append(val)
		if not self.min_stack or val <= self.min_stack[-1]:
			self.min_stack.append(val)
	
	def pop(self) -> None:
		val = self.stack.pop()
		if val == self.min_stack[-1]:
			self.min_stack.pop()

	def top(self) -> int:
		return self.stack[-1]

	def getMin(self) -> int:
		return self.min_stack[-1]

def test_MinStack(in1, in2, out):
	minStack = MinStack()

	output = [None]
	for i in range(len(in1)):
		if in1[i] == "push":
			val = int(in2[i][0])
			output.append(minStack.push(val))
		elif in1[i] == "pop":
			output.append(minStack.pop())
		elif in1[i] == "top":
			result = minStack.top()
			output.append(result)
		elif in1[i] == "getMin":
			output.append(minStack.getMin())
	
	print(output)
	print(out)
	assert output == out
	print("All test cases pass")

if __name__ == "__main__":
	input1 = ["MinStack","push","push","push","getMin","pop","top","getMin"]
	input2 = [[],[-2],[0],[-3],[],[],[],[]]
	output = [None, None, None, None, -3, None, 0, -2]
	
	test_MinStack(input1, input2, output)