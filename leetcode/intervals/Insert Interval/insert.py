from typing import List

# Time: O(n), Space: O(1)
class Solution:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		result = []
		for i in range(len(intervals)):
			if newInterval[1] < intervals[i][0]:
				result.append(newInterval)
				return result + intervals[i:]
			elif newInterval[0] > intervals[i][1]:
				result.append(intervals[i])
			else:
				newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
		result.append(newInterval)
		return result

def main():
	a = Solution()
	intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
	newInterval = [4,8]

	result = a.insert(intervals, newInterval)
	print(result)

if __name__ == "__main__":
	main()
