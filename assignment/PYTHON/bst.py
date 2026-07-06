class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def delete(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # No Left Child.
        if root.left is None:
            return root.right
        #  No Right Child.
        elif root.right is None:
            return root.left
        # Two Children.
        temp = root.right
        while temp.left:
            temp = temp.left
        root.data = temp.data
        root.right = delete(root.right,temp.data)
    return root