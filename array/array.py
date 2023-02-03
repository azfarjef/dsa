def	array_practice():
	arr = [3, 2, 4, 5]

	arr.pop()
	print(f"After pop: {arr}")

	arr.append(6)
	print(f"After append 6: {arr}")

	print(f"Index of 4: {arr.index(4)}")

	arr.remove(4)
	print(f"Removed 4: {arr}")

	arr.reverse()
	print(f"Reversed: {arr}")
	print(f"Sorted returns: {sorted(arr)}")

	arr.sort()
	print(f"Sorted: {arr}")

	print(f"Last element: {arr[-1]}")
	print(f"Reverse arr: {arr[::-1]}")

def	main():
	array_practice()

if	__name__ == "__main__":
	main()


# #List traversal
# range(start, stop, hop)
# range(n) # [0,1,...,n-1]
# range(1,n) # [1,...,n-1]
# range(1,n,2) # [1,3,5,...,n-1] if n is even, or [1,3,5,...,n-2] if n is odd
# range(n,-1,-1) # [n,n-1,n-2,...,0]
# range(len(arr)) # Provides indices of an array arr
# range(len(arr)-1,-1,-1) # Provides indices of arr backwards

# # List slicing
# arr[w:s] # Wait w elements, start copy (:), stop before reaching index s
# arr = [1,2,3,4]
# arr[1:] = [2,3,4]
# arr[:2] = [1,2]

# #List manipulation
# arr = [1,2,3]
# [str(x) for x in arr] # Output: ['1','2','3']
# map(lambda x: str(x), arr) # Output: ['1','2','3']
# [str(x) for x in arr if x%2] # Output: ['1','3']

# # List as queue
# arr = [1,2,3]
# arr.append(x) # queue.push(x)
# arr.pop(0) #queue.pop()
# arr[0] #queue.peek()

# # List as stack
# arr = [1,2,3]
# arr.append(x) #stack.push(x)
# arr.pop() # stack.pop()
# arr[-1] # stack.peek()