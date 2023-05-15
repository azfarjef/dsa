from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Time: O(p + q), Space: O(1)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    
def test_isSameTree():
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert Solution().isSameTree(root1, root2) == True
    root1 = TreeNode(1, TreeNode(2))
    root2 = TreeNode(1, None, TreeNode(2))
    assert Solution().isSameTree(root1, root2) == False
    root1 = TreeNode(1, TreeNode(2), TreeNode(1))
    root2 = TreeNode(1, TreeNode(1), TreeNode(2))
    assert Solution().isSameTree(root1, root2) == False
    print("All tests passed")
    
if __name__ == "__main__":
    test_isSameTree()