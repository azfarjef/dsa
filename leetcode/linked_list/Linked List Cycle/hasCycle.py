from typing import Optional

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# Time: O(n), Space: O(1)
class Solution:
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		pointer1 = head
		pointer2 = head
		while pointer2 != None and pointer2.next != None:
			pointer1 = pointer1.next
			pointer2 = pointer2.next.next
			if pointer1 == pointer2:
				return True
		return False

def main():
	head = ListNode(3)
	head.next = ListNode(0)
	head.next.next = (ListNode(4))
	head.next.next.next = head

	a = Solution()
	result = a.hasCycle(head)

	print(result)

if __name__ == "__main__":
	main()