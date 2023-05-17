from typing import List

# Time: O(n!), Space: O(n!)
class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    res = []
    
    if len(nums) == 1:
      return [nums[:]] # deep copy
    
    for i in range(len(nums)):
      n = nums.pop(0)
      perms = self.permute(nums)

      for perm in perms:
        perm.append(n)
      res.extend(perms)
      nums.append(n)
    return res
  
def test_permute():
  sol = Solution()
  assert sorted(sol.permute([1,2,3])) == sorted([[1,2,3],[2,3,1],[3,1,2],[1,3,2],[2,1,3],[3,2,1]])
  assert sorted(sol.permute([0,1])) == sorted([[0,1],[1,0]])
  assert sol.permute([1]) == [[1]]
  print("All tests passed!")

if __name__ == "__main__":
  test_permute()
