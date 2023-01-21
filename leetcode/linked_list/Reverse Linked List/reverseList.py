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
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		prev = None
		current = head

		while current:
			temp = current.next
			current.next = prev
			prev = current
			current = temp
		
		return prev

def main():
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	a = Solution()

	result = a.reverseList(head)
	print(result)

if __name__ == "__main__":
	main()
