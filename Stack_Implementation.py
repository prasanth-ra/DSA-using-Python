class Stack:
	def __init__(self, capacity=0):
		self._items=[]

	def isEmpty(self) -> bool:
		if (len(self._items)==0):
			return True
		else:
			return False

	def size(self) -> int:
		return len(self._items)

	def top(self) -> int:
		if (not self.isEmpty()):
			return self._items[-1]
		else:
			return -1
	def push(self, element: int) -> None:
		self._items.append(element)

	def pop(self) -> None:
		self._items.pop()