from queue import Queue

def main():
	q = Queue()

	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	print(q.data)
	q.dequeue()
	print(q.data)
	print(f"queue.empty() = {q.empty()}")
	q.dequeue()
	print(q.data)
	q.dequeue()
	print(q.data)
	print(f"queue.empty() = {q.empty()}")

if __name__ == "__main__":
	main()
