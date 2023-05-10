from typing import Optional

class Node:
	def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
		self.val = int(x)
		self.next = next
		self.random = random

# Time: O(n), Space: O(n)	
class Solution:
	def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
		oldToCopy = { None: None }
		
		cur = head
		while cur:
			copy = Node(cur.val)
			oldToCopy[cur] = copy
			cur = cur.next
			
		cur = head
		while cur:
			copy = oldToCopy[cur]
			copy.next = oldToCopy[cur.next]
			copy.random = oldToCopy[cur.random]
			cur = cur.next

		return oldToCopy[head]

def test_copyRandomList():
	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)

	node1.next = node2
	node2.next = node3
	node1.random = node3
	node2.random = node1
	node3.random = node2

	solution = Solution().copyRandomList(node1)
	assert solution.val == 1
	assert solution.next.val == 2
	assert solution.next.next.val == 3
	assert solution.random.val == 3
	assert solution.next.random.val == 1
	assert solution.next.next.random.val == 2

	print("All tests passed.")

if __name__ == "__main__":
	test_copyRandomList()