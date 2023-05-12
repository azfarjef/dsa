from typing import Optional
from collections import deque

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# Recursive DFS, Time: O(n), Space: O(1)
class Solution:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		if not root:
			return 0
		return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
  
# Iterative DFS, Time: O(n), Space: O(n)
class Solution2:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		if not root:
			return 0
		stack = [(root, 1)]
		max_depth = 0
		while stack:
			node, depth = stack.pop()
			if node:
				max_depth = max(max_depth, depth)
				stack.append((node.left, depth + 1))
				stack.append((node.right, depth + 1))
		return max_depth

# Iterative BFS, Time: O(n), Space: O(n)
class Solution3:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		q = deque()
		if root:
			q.append(root)
		max_depth = 0

		while q:
			for i in range(len(q)):
				node = q.popleft()
				if node.left:
					q.append(node.left)
				if node.right:
					q.append(node.right)
			max_depth += 1
		return max_depth
  
def test_maxDepth():
	solution = Solution()

	root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
	assert solution.maxDepth(root) == 3, 'wrong result'  
	root = TreeNode(1, None, TreeNode(2))
	assert solution.maxDepth(root) == 2, 'wrong result'  
	root = None
	assert solution.maxDepth(root) == 0, 'wrong result'  
	root = TreeNode(0)
	assert solution.maxDepth(root) == 1, 'wrong result'

	print('All tests passed!')
  
if __name__ == '__main__':
	test_maxDepth()