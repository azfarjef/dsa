from typing import List
import heapq

class KthLargest:

	# Time: O(n*log k), Space: O(k)
	def __init__(self, k: int, nums: List[int]):
		# minHeap wuth K largest integers
		self.minHeap, self.k = nums, k
		heapq.heapify(self.minHeap)
		while len(self.minHeap) > k:
			heapq.heappop(self.minHeap)

	# Time: O(log k), Space: O(k)
	def add(self, val: int) -> int:
		heapq.heappush(self.minHeap, val)
		if len(self.minHeap) > self.k:
			heapq.heappop(self.minHeap)
		return self.minHeap[0]

def test_kth_largest():
	heap = KthLargest(3, [4,5,8,2])
	assert heap.add(3) == 4
	assert heap.add(5) == 5
	assert heap.add(10) == 5
	assert heap.add(9) == 8

	print("All tests passed.")

if __name__ == "__main__":
	test_kth_largest()
