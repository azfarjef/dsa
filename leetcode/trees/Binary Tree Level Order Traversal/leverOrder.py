from typing import Optional, List
from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
# Time: O(n), Space: O(n)
class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    res = []
    q = deque()
    if root:
      q.append(root)
      
    while q:
      val = []
      
      for i in range(len(q)):
        node = q.popleft()
        val.append(node.val)
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      res.append(val)
    return res
  
def test_levelOrder():
  root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
  assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]
  
  root = TreeNode(1)
  assert Solution().levelOrder(root) == [[1]]
  
  root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
  assert Solution().levelOrder(root) == [[1], [2, 3], [4]]
  
  print("All tests passed!")

if __name__ == "__main__":
  test_levelOrder()