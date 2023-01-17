from typing import List

# First try: Time = O(n^2), Space = O(1)
class mySolution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i, n in enumerate(nums):
			sum = n
			j = i
			for i, n in enumerate(nums):	
				if nums[i] + sum == target and i is not j:
					return ([i, j])

# Leetcode solution: Time = O(n), Space = O(n)
class goodSolution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		hashmap = {}
		length = len(nums)
		for i in range(length):
			hashmap[nums[i]] = i
		for i in range(length):
			complement = target - nums[i]
			if (complement in hashmap and hashmap[complement] != i):
				return ([i, hashmap[complement]])

def main():
	# a = mySolution()
	a = goodSolution()
	input = [3, 2, 4]

	result = a.twoSum(input, 6)
	print(f"The result is {result}")

if __name__ == "__main__":
	main()