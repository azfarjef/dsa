from typing import List
import heapq

# Time: O(n*log n), Space: O(n)
class Solution2:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		nums.sort()
		return nums[-k]

# Time: O(n + k*log n), Space: O(n)
class Solution3:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		heapq.heapify(nums)
		while len(nums) > k:
			heapq.heappop(nums)
		return nums[0]

# Time: Worst: O(n^2) Average: O(n), Space: O(1)
class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		k = len(nums) - k

		def quickSelect(l, r):
			pivot, p = nums[r], l
			for i in range(l, r):
				if nums[i] <= pivot:
					nums[p], nums[i] = nums[i], nums[p]
					p += 1
			nums[p], nums[r] = nums[r], nums[p]

			if p > k:
				return quickSelect(l, p - 1)
			elif p < k:
				return quickSelect(p + 1, r)
			else:
				return nums[p]

		return quickSelect(0, len(nums) - 1)

def test_findKthLargest():
	assert Solution().findKthLargest([3,2,1,5,6,4], 2) == 5
	assert Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4

	print("All tests passed.")

if __name__ == "__main__":
	test_findKthLargest()
