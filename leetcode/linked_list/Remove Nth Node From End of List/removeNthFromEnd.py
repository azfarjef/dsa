from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# Time: O(n), Space: O(1)
class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		dummy = ListNode(0)
		dummy.next = head

		first = dummy
		second = dummy

		# Move second until n nodes
		for i in range(n):
			second = second.next

		# Move both pointers until first reach the Nth node from the end, second reach the end
		while second.next:
			first = first.next
			second = second.next

		# Remove nth node from the end
		first.next = first.next.next

		return dummy.next

def compare_linked_lists(head1, head2):
	while head1 and head2:
		if head1.val != head2.val:
			return False
		head1 = head1.next
		head2 = head2.next
	
	if head1 or head2:
		return False
	
	return True

def test_removeNthFromEnd():
	s = Solution()

	# Test Case 1
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
	n = 2
	expected_output = ListNode(1, ListNode(2, ListNode(3, ListNode(5))))
	assert compare_linked_lists(s.removeNthFromEnd(head, n), expected_output) == True
	
	# Test case 2
	head = ListNode(1)
	n = 1
	expected_output = None
	assert compare_linked_lists(s.removeNthFromEnd(head, n), expected_output) == True
	
	# Test case 3
	head = ListNode(1, ListNode(2))
	n = 1
	expected_output = ListNode(1)
	assert compare_linked_lists(s.removeNthFromEnd(head, n), expected_output) == True
	
	print("All test cases pass")

if __name__ == "__main__":
	test_removeNthFromEnd()
