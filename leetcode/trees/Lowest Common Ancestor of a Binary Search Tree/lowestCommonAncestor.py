class TreeNode:
  def __init__(self, x, left=None, right=None):
    self.val = x
    self.left = left
    self.right = right

# Time: O(logn), Space: O(1)
class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    cur = root
    
    while cur:
      if p.val < cur.val and q.val < cur.val:
        cur = cur.left
      elif p.val > cur.val and q.val > cur.val:
        cur = cur.right
      else:
        return cur
      
def test_lowestCommonAncestor():
  root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
  q = TreeNode(8)
  p = TreeNode(2)

  solution = Solution().lowestCommonAncestor(root, p, q)
  assert solution.val == root.val
  
  q = TreeNode(4)
  solution = Solution().lowestCommonAncestor(root, p, q)
  assert solution.val == root.left.val
  
  print("All test cases passed!")

if __name__ == "__main__":
  test_lowestCommonAncestor()
