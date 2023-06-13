class Node:
	def __init__(self, val=0, neighbors=None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []

# Time: O(n) where n = edge + nodes, Space: O(n)
class Solution:
	def cloneGraph(self, node: 'Node') -> 'Node':
		oldToNew = {}

		def dfs(node):
			if node in oldToNew:
				return oldToNew[node]

			copy = Node(node.val)
			oldToNew[node] = copy
			for nei in node.neighbors:
				copy.neighbors.append(dfs(nei))
			return copy

		return dfs(node) if node else None

def test_cloneGraph():
	node1 = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	node4 = Node(4)

	node1.neighbors = [node2, node4]
	node2.neighbors = [node1, node3]
	node3.neighbors = [node2, node4]
	node4.neighbors = [node1, node3]

	cloned = Solution().cloneGraph(node1)

	assert cloned is not node1
	assert cloned is not node2
	assert cloned is not node3
	assert cloned is not node4

	assert cloned.val == 1
	assert cloned.neighbors[0].val == 2
	assert cloned.neighbors[1].val == 4
	assert cloned.neighbors[0].neighbors[0].val == 1
	assert cloned.neighbors[0].neighbors[1].val == 3
	assert cloned.neighbors[1].neighbors[0].val == 1
	assert cloned.neighbors[1].neighbors[1].val == 3
	
	print("All tests pass!")

if __name__ == "__main__":
	test_cloneGraph()

