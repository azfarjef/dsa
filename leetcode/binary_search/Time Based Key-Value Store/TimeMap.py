class TimeMap:
	def __init__(self):
		self.keyStore = {} # { key: [[value, timestamp], ...] }
	
	# Time: O(1), Space: O(1)
	def set(self, key: str, value: str, timestamp: int) -> None:
		if key not in self.keyStore:
			self.keyStore[key] = []
		self.keyStore[key].append([value, timestamp])

	# Time: O(logn), Space: O(1)
	def get(self, key: str, timestamp: int) -> str:
		element = self.keyStore.get(key, [])
		l, r = 0, len(element) - 1
		res = ""

		while l <= r:
			m = (l + r) // 2
			if element[m][1] <= timestamp:
				res = element[m][0]
				l = m + 1
			else:
				r = m - 1
		return res
	

def test_TimeMap():
	T = TimeMap()
	T.set("foo", "bar", 1)
	assert T.get("foo", 1) == "bar"
	assert T.get("foo", 3) == "bar"
	T.set("foo", "bar2", 4)
	assert T.get("foo", 4) == "bar2"
	assert T.get("foo", 5) == "bar2"

	print("All tests passed")

if __name__ == "__main__":
	test_TimeMap()