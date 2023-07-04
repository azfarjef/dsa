from typing import List

# Time: O(n*log n), Space: O(1)
class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		intervals.sort()
		res = 0
		lastEnd = intervals[0][1]

		for start, end in intervals[1:]:
			if start < lastEnd:
				res += 1
				lastEnd = min(lastEnd, end)
			else:
				lastEnd = end

		return res

def test_eraseOverlapIntervals():
	assert Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
	assert Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
	assert Solution().eraseOverlapIntervals([[1,2],[2,3]]) == 0

	print("All tests pass")

if __name__ == "__main__":
	test_eraseOverlapIntervals()
