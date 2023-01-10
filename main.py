from ABR import ABR

if __name__ == '__main__':
	VALUES = [21, 8, 9, 11, 15, 19, 20, 7, 3, 2, 1, 5, 6, 4, 13, 14, 10, 12, 17, 16, 18]

	tree = ABR(VALUES)

	print(tree)

	print(tree.search(4))
	print(tree.search(100))

	print(tree.sort())