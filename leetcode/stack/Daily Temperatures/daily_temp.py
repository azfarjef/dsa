from typing import List

# Time: O(n), Space: O(n)
class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		n = len(temperatures)
		stack = []
		answer = [0] * n

		for i in range(n-1, -1, -1):
			while stack and temperatures[i] >= temperatures[stack[-1]]:
				stack.pop()
			if stack:
				answer[i] = stack[-1] - i
			stack.append(i)

		return answer

def test_dailyTemperatures():
	sol = Solution()

	assert sol.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
	assert sol.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
	assert sol.dailyTemperatures([30,60,90]) == [1,1,0]

	print("All test cases pass")

if __name__ == "__main__":
	test_dailyTemperatures()
