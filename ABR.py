from typing import Optional
from binarytree import Node

class ABR(Node):
	def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None) -> None:
		super().__init__(value, left, right)