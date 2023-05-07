from typing import List

# Bucket Sort
# Time: O(n), Space: O(n)
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		count = {}
		freq = [[] for i in range (len(nums) + 1)]

		for n in nums:
			count[n] = 1 + count.get(n, 0)
		for n, c in count.items():
			freq[c].append(n)

		res = []
		for i in range(len(freq) - 1, 0, -1):
			for n in freq[i]:
				res.append(n)
				if len(res) == k:
					return res
	
# test topKFrequent
def test_topKFrequent():
	assert Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
	assert Solution().topKFrequent([1], 1) == [1]

	print("All tests passed")

if __name__ == "__main__":
	test_topKFrequent()
