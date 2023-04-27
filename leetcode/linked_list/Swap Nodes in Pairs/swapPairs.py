from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# Time: O(n), Space: O(1)
class Solution:
	def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
		dummy = ListNode(0)
		dummy.next = head

		prev, curr = dummy, head

		while curr and curr.next:
			first, second = curr, curr.next
			
			first.next = second.next
			second.next = first
			prev.next = second

			prev = first
			curr = first.next

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

def test_swapPairs():
	s = Solution()

	head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
	assert compare_linked_lists(s.swapPairs(head), ListNode(2, ListNode(1, ListNode(4, ListNode(3))))) == True


	assert compare_linked_lists(s.swapPairs(None), None) == True

	assert compare_linked_lists(s.swapPairs(ListNode(1)), ListNode(1)) == True

	assert compare_linked_lists(s.swapPairs(ListNode(1, ListNode(2))), ListNode(2, ListNode(1))) == True
	
	print("All tests passed")

if __name__ == "__main__":
	test_swapPairs()
