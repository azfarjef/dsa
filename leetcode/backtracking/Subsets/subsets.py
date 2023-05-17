from typing import List

# Time: O(n.2^n), Space: O(2^n)
class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    subset = []

    def dfs(i):
      if i >= len(nums):
        res.append(subset.copy())
        return
      # decision to include nums[i]
      subset.append(nums[i])
      dfs(i + 1)
      # decision to not include nums[i]
      subset.pop()
      dfs(i + 1)
      
    dfs(0)
    return res

def test_subsets():
  sol = Solution().subsets([1,2,3])
  
  assert sorted(sol) == [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]

  print("All tests passed!")

if __name__ == "__main__":
  test_subsets()