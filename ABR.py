from binarytree import Node

class ABR(Node):
	def __init__(self, values: list[int]):
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

	def minimum(self) -> int | None:
		node = self

		while node is not None:
			if node.left is None:
				return node.value
			else:
				node = node.left

		return None

	def maximum(self) -> int | None:
		node = self

		while node is not None:
			if node.right is None:
				return node.value
			else:
				node = node.right

		return None

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