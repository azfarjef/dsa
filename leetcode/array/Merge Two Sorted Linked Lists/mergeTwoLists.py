from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def append(self, val):
		node = ListNode(val)
		while self.next:
			self = self.next
		self.next = node

	def listtoll(self, l):
		self.val = l[0]
		for n in l[1:]:
			node = ListNode(n)
			self.next = node
			self = self.next

	def __str__(self):
		output = ""
		while self:
			output += str(self.val) + " -> "
			self = self.next
		return output

class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		if list1 is None:
			return list2
		if list2 is None:
			return list1

		dummy = ListNode()
		pointer = dummy
		while list1 and list2:
			if list1.val < list2.val:
				pointer.next = list1
				list1 = list1.next
			else:
				pointer.next = list2
				list2 = list2.next
			pointer = pointer.next

		if list1:
			pointer.next = list1
		else:
			pointer.next = list2

		return dummy.next

def main():
	l1 = [1,2,4]
	l2 = [1,3,4]

	list1 = ListNode()
	list2 = ListNode()
	list1.listtoll(l1)
	list2.listtoll(l2)
	print(list1)
	print(list2)

	a = Solution()
	result = a.mergeTwoLists(list1, list2)
	print(result)

if __name__ == "__main__":
	main()