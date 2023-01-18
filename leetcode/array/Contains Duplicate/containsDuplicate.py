from typing import List

# Time: O(n) Space: O(n)
class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		aset = set()
		for num in nums:
			if num in aset:
				return True
			else:
				aset.add(num)
		return False
			
def main():
	a = Solution()
	nums = [1,2,3,1]

	result = a.containsDuplicate(nums)
	print(result)

if __name__ == "__main__":
	main()