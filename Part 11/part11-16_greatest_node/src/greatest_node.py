# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


def greatest_node(tree: Node) -> int:
    # First attempt
    value = tree.value

    if tree.left_child is not None:
        left_value = greatest_node(tree.left_child)

        if left_value > value:
            value = left_value

    if tree.right_child is not None:
        right_value = greatest_node(tree.right_child)

        if right_value > value:
            value = right_value

    return value

    # Second attempt
    # value = tree.value

    # if tree.left_child:
    #     left_value = greatest_node(tree.left_child)
    # else:
    #     left_value = value

    # if tree.right_child:
    #     right_value = greatest_node(tree.right_child)
    # else:
    #     right_value = value

    # return max(value, left_value, right_value)


if __name__ == '__main__':
    # Create the root of the tree
    tree = Node(2)

    # Create the left subtree
    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    # Create the right subtree
    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))
