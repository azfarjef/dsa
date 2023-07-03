from typing import List
import heapq

# Time: O(n*log n), Space: O(n)
class Solution:
	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		heap = []
		for x, y in points:
			dist = (x**2 + y**2)
			heap.append([dist, x, y])
		
		heapq.heapify(heap)
		res = []
		for i in range(k):
			dist, x, y = heapq.heappop(heap)
			res.append([x, y])
		return res

def test_k_closest():
	assert Solution().kClosest([[1,3],[-2,2]], 1) == [[-2,2]]
	assert Solution().kClosest([[3,3],[5,-1],[-2,4]], 2) == [[3,3],[-2,4]]

	print("All test passed")

if __name__ == "__main__":
	test_k_closest()
