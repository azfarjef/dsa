class MyQueue:

	def __init__(self):
		self.s1 = []
		self.s2 = []

	def __str__(self):
		return "% s" % (self.s1)

	def push(self, x: int) -> None:
		while self.s1:
			self.s2.append(self.s1.pop())
		self.s1.append(x)
		while self.s2:
			self.s1.append(self.s2.pop())
	
	def pop(self) -> int:
		return self.s1.pop()

	def peek(self) -> int:
		return self.s1[-1]

	def empty(self) -> bool:
		return not self.s1

def main():
	obj = MyQueue()
	obj.push(1)
	obj.push(2)
	print(obj)
	print(obj.peek())
	print(obj.pop())
	print(obj.empty())
	print(obj)

if __name__ == "__main__":
	main()

	