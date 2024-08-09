from collections import deque

queue_exm = deque()

queue_exm.append('x')

queue_exm.append('y')

queue_exm.append('z')

print("Queue before operations")

print(queue_exm)

# Dequeuing elements

print("\nDequeuing elements")

print(queue_exm.popleft())

print(queue_exm.popleft())

print(queue_exm.popleft())

print("\nQueue after operations")

print(queue_exm)