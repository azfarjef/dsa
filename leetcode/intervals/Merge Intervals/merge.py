from typing import List

# Time: O(n*log n), Space: O(n)
class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		intervals.sort(key=lambda x: x[0])
		res = [intervals[0]]

		for start, end in intervals:
			lastEnd = res[-1][1]

			if  start <= lastEnd:
				res[-1][1] = max(lastEnd, end)
			else:
				res.append([start, end])
		return res

def test_merge():
	assert Solution().merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
	assert Solution().merge([[1,4],[4,5]]) == [[1,5]]

	print("All tests pass")

if __name__ == "__main__":
	test_merge()
