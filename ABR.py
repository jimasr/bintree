from binarytree import Node

class ABR(Node):
	def __init__(self, *values: int):
		super().__init__(values[0])

		self.plants(values[1:])

	def plant(self, value: int) -> bool:
		node = self

		while node is not None:
			if value <= node.value:
				if node.left is None:
					node.left = Node(value)
					return True
				else:
					node = node.left
			else:
				if node.right is None:
					node.right = Node(value)
					return True
				else:
					node = node.right

		return False

	def plants(self, values: list[int]) -> bool:
		for value in values:
			if not self.plant(value):
				return False

		return True

	def height(self, node: Node | None = None) -> int:
		if node is None:
			return -1

		leftHeight = self.height(node.left)
		rightHeight = self.height(node.right)
		return max(leftHeight, rightHeight) + 1

	def size(self, node: Node | None = None) -> int:
		if node is None:
			return 0

		return self.size(node.left) + self.size(node.right) + 1

	def minimum(self, node: Node | None = None) -> int:
		if node is None:
			node = self

		while node is not None:
			if node.left is None:
				return node.value
			else:
				node = node.left

		return node.value

	def maximum(self, node: Node | None = None) -> int:
		if node is None:
			node = self

		while node is not None:
			if node.right is None:
				return node.value
			else:
				node = node.right

		return node.value

	def search(self, value: int) -> bool:
		node = self

		while node is not None:
			if value == node.value:
				return True
			elif value < node.value:
				node = node.left
			else:
				node = node.right

		return False

	def sort(self, node: Node | None = None, tab: list[int] = []) -> list[int]:
		if node is None:
			node = self

		if node.left is not None:
			tab = self.sort(node.left, tab)

		tab.append(node.value)

		if node.right is not None:
			tab = self.sort(node.right, tab)

		return tab

	def delete(self, value: int) -> bool:
		node = self
		parent = None

		while node is not None:
			if value == node.value:
				if node.left is None and node.right is None:
					if parent is None:
						self.value = None
					elif parent.left == node:
						parent.left = None
					else:
						parent.right = None
				elif node.left is None:
					if parent is None:
						self.value = node.right.value
						self.left = node.right.left
						self.right = node.right.right
					elif parent.left == node:
						parent.left = node.right
					else:
						parent.right = node.right
				elif node.right is None:
					if parent is None:
						self.value = node.left.value
						self.left = node.left.left
						self.right = node.left.right
					elif parent.left == node:
						parent.left = node.left
					else:
						parent.right = node.left
				else:
					minimum = self.minimum(node.right)
					self.delete(minimum)
					node.value = minimum

				return True
			elif value < node.value:
				parent = node
				node = node.left
			else:
				parent = node
				node = node.right

		return False

	def balance(self, start : int, end : int) -> Node:

		if start > end:
			return None

		sorted_values = self.sort()
		middle = (start + end) // 2

		node = ABR(sorted_values[middle])

		node.left = self.balance(start, middle	- 1)
		node.right = self.balance(middle + 1, end)

		return node