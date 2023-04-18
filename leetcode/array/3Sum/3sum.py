from typing import List

# Time = O(n^2), Space = O(1)
class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		n = len(nums)
		nums.sort()
		ans = []
		for i in range(n-2):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			l, r = i+1, n-1
			while l < r:
				sum = nums[i] + nums[l] + nums[r]
				if sum < 0:
					l += 1
				elif sum > 0:
					r -= 1
				else:
					ans.append([nums[i], nums[l], nums[r]])
					while l < r and nums[l] == nums[l+1]:
						l += 1
					while l < r and nums[r] == nums[r-1]:
						r -= 1
					l += 1
					r -= 1
		return ans

def test_threeSum():
	sol = Solution()

	assert sol.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
	assert sol.threeSum([0,1,1]) == []
	assert sol.threeSum([0,0,0]) == [[0,0,0]]
	assert sol.threeSum([1,2,-2,-1]) == []
	assert sol.threeSum([1,-1,-1,0]) == [[-1,0,1]]
	print("All test cases pass")

if __name__ == "__main__":
	test_threeSum()