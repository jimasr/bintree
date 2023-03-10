from ABR import ABR

def main():
	VALUES = [21, 8, 9, 11, 15, 19, 20, 7, 3, 2, 1, 5, 6, 4, 13, 14, 10, 12, 17, 16, 18]

	tree = ABR(*VALUES)

	print(tree)

	print(f"Height: {tree.height(tree)}")
	print(f"Size: {tree.size(tree)}")

	print(f"Searching for 4: {tree.search(4)}")
	print(f"Searching for 100: {tree.search(100)}")

	print(f"Sorted values: {tree.sort()}")

	print(f"Minimum value: {tree.minimum()}")
	print(f"Maximum value: {tree.maximum()}")

	print(f"Deleting 15: {tree.delete(15)}")
	print(tree)

	print(f"Balancing tree...")
	balancedTree = tree.balance(0, len(VALUES) - 1)
	print(balancedTree)

if __name__ == '__main__':
	main()