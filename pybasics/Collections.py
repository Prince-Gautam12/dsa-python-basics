from collections import deque


queue = deque([1,23,4,5,56,43,6])
print(queue)

print(queue.popleft())
print(queue)
print(queue.pop())
print(queue.appendleft(234))
print(queue)
print(queue.append(324))
print(queue)
