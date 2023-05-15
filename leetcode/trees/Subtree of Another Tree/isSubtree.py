from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Time: O(T*S), Space: O(1)
class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if not subRoot:
      return True
    if not root:
      return False
    
    if self.isSameTree(root, subRoot):
      return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if not p and not q:
          return True
      if not p or not q or p.val != q.val:
          return False
      return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
  
def test_isSubtree():
  root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
  subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
  assert Solution().isSubtree(root, subRoot) == True  
  root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
  subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
  assert Solution().isSubtree(root, subRoot) == False  
  print("All tests passed")
  
if __name__ == "__main__":
  test_isSubtree()
