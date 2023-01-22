from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def __str__(self):
		output = ""
		current = self
		while current:
			output += str(current.val) + " -> "
			current = current.next
		return output

# Time: O(n), Space: O(1)
class Solution:
	def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
		slow = head
		fast = head

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		return slow

def main():
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)

	a = Solution()

	result = a.middleNode(head)
	print(result)

if __name__ == "__main__":
	main()
