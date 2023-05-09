from typing import Optional

# Time: O(n), Space: O(1)
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def reorderList(self, head: Optional[ListNode]) -> None:
		# find the middle of the linked list
		slow, fast = head, head.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		# reverse the second half of the linked list
		second = slow.next
		prev = slow.next = None
		while second:
			tmp = second.next
			second.next = prev
			prev = second
			second = tmp

		# merge two halfs
		first, second = head, prev
		while second:
			tmp1, tmp2 = first.next, second.next
			first.next = second
			second.next = tmp1
			first, second = tmp1, tmp2

def compare_linked_lists(head1, head2):
	while head1 and head2:
		if head1.val != head2.val:
			return False
		head1 = head1.next
		head2 = head2.next
	
	if head1 or head2:
		return False
	
	return True
	
def test_reorderList():
	list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
	expected = ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))

	Solution().reorderList(list1)
	assert compare_linked_lists(list1, expected) == True

	print("All tests passed.")

if __name__ == "__main__":
	test_reorderList()