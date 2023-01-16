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