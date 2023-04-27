from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# Time: O(n), Space: O(1)
class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		# Find the middle of the list
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		# Reverse the second half of the list
		prev = None
		curr = slow
		while curr:
			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp

		#Compare the first and second halves of the list
		first = head
		second = prev
		while second:
			if first.val != second.val:
				return False
			first = first.next
			second = second.next

		return True

def test_isPalindrome():
	#Test case 1
	head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
	assert Solution().isPalindrome(head) == True

	# Test case 2
	head = ListNode(1, ListNode(2))
	assert Solution().isPalindrome(head) == False

	# Test case 3
	head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
	assert Solution().isPalindrome(head) == True

	# Test case 4
	head = ListNode(1, ListNode(0, ListNode(1)))
	assert Solution().isPalindrome(head) == True

	# Test case 5
	head = ListNode(1, ListNode(0, ListNode(2)))
	assert Solution().isPalindrome(head) == False

	print("All test cases pass")

if __name__ == "__main__":
	test_isPalindrome()
