class ListNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.prev = None
		self.next = None

# TIme: O(n), Space: O(1)
class LRUCache:
	def __init__(self, capacity:int):
		self.dic = dict()
		self.capacity = capacity
		self.head = ListNode(0, 0)
		self.tail = ListNode(-1, -1)
		self.head.next = self.tail
		self.tail.prev = self.head

	def get(self, key:int) -> int:
		if key in self.dic:
			node = self.dic[key]
			self.removeFromList(node)
			self.insertIntoHead(node)
			return node.value
		else:
			return -1
		
	def put(self, key:int, value:int) -> None:
		if key in self.dic:
			node = self.dic[key]
			self.removeFromList(node)
			self.insertIntoHead(node)
			node.value = value
		else:
			if len(self.dic) >= self.capacity:
				self.removeFromTail()
			node = ListNode(key, value)
			self.dic[key] = node
			self.insertIntoHead(node)

	def removeFromList(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev

	def insertIntoHead(self, node):
		temp = self.head.next
		self.head.next = node
		node.prev = self.head
		node.next = temp
		temp.prev = node

	def removeFromTail(self):
		if len(self.dic) == 0:
			return
		tailNode = self.tail.prev
		del self.dic[tailNode.key]
		self.removeFromList(tailNode)

def main():
	lru = LRUCache(2)

	lru.put(1, 1)
	lru.put(2, 2)
	print(lru.get(1))
	lru.put(3, 3)
	print(lru.get(2))
	lru.put(4, 4)
	print(lru.get(1))
	print(lru.get(3))
	print(lru.get(4))

if __name__ == "__main__":
	main()