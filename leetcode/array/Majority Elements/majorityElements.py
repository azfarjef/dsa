from typing import List
import collections

# Hashmap: Time: O(n), Space: O(n)
class aSolution:
	def majorityElement(self, nums: List[int]) -> int:
		count = collections.Counter(nums)
		return max(count.keys(), key=count.get)

#Boyer-Moore Voting Algorithm: Time: O(n), Space: O(1)
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		count = 0
		candidate = None

		for num in nums:
			if count == 0:
				candidate = num
			count += (1 if num == candidate else -1)

		return candidate

def main():
	a = Solution()
	nums = [2,2,1,1,1,2,2]

	result = a.majorityElement(nums)
	print(result)

if __name__ == "__main__":
	main()
