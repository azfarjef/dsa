from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Time: O(n), Space: O(1)
class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return None

    tmp = root.left
    root.left = root.right
    root.right = tmp
    
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root

def test_invertTree():
  node1 = TreeNode(1)
  node2 = TreeNode(2)
  node3 = TreeNode(3)
  node4 = TreeNode(4)
  node5 = TreeNode(5)
  node6 = TreeNode(6)
  node7 = TreeNode(7)  

  node1.left = node2
  node1.right = node3
  node2.left = node4
  node2.right = node5
  node3.left = node6
  node3.right = node7  

  solution = Solution().invertTree(node1)

  assert solution.val == 1
  assert solution.left.val == 3
  assert solution.right.val == 2
  assert solution.left.left.val == 7
  assert solution.left.right.val == 6
  assert solution.right.left.val == 5
  assert solution.right.right.val == 4
  
  print("All tests passed!")
  
if __name__ == "__main__":
	test_invertTree()
  