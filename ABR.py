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