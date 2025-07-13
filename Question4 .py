from collections import deque

stack = []
queue = deque()

while True:
    print("\nChoose operation:")
    print("1. Push (Stack)")
    print("2. Pop (Stack)")
    print("3. Enqueue (Queue)")
    print("4. Dequeue (Queue)")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        val = input("Enter value to push onto stack: ")
        stack.append(val)
        print("Stack after push:", stack)

    elif choice == '2':
        if stack:
            popped = stack.pop()
            print("Popped from stack:", popped)
            print("Stack now:", stack)
        else:
            print("Stack is empty.")

    elif choice == '3':
        val = input("Enter value to enqueue into queue: ")
        queue.append(val)
        print("Queue after enqueue:", list(queue))

    elif choice == '4':
        if queue:
            dequeued = queue.popleft()
            print("Dequeued from queue:", dequeued)
            print("Queue now:", list(queue))
        else:
            print("Queue is empty.")

    elif choice == '5':
        print("Exiting.")
        break

    else:
        print("Invalid choice. Try again.")