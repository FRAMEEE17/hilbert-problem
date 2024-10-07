class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, key, value):
        def _insert(node, key, value):
            if not node:
                self.size += 1
                return AVLNode(key, value)
            if key < node.key:
                node.left = _insert(node.left, key, value)
            elif key > node.key:
                node.right = _insert(node.right, key, value)
            else:
                node.value = value
                return node

            self.update_height(node)
            balance = self.balance_factor(node)

            if balance > 1:
                if key < node.left.key:
                    return self.rotate_right(node)
                else:
                    node.left = self.rotate_left(node.left)
                    return self.rotate_right(node)
            if balance < -1:
                if key > node.right.key:
                    return self.rotate_left(node)
                else:
                    node.right = self.rotate_right(node.right)
                    return self.rotate_left(node)
            return node

        self.root = _insert(self.root, key, value)

    def delete(self, key):
        def _delete(node, key):
            if not node:
                return node
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = self.get_min_value_node(node.right)
                node.key = temp.key
                node.value = temp.value
                node.right = _delete(node.right, temp.key)
            
            if not node:
                return node

            self.update_height(node)
            balance = self.balance_factor(node)

            if balance > 1:
                if self.balance_factor(node.left) >= 0:
                    return self.rotate_right(node)
                else:
                    node.left = self.rotate_left(node.left)
                    return self.rotate_right(node)
            if balance < -1:
                if self.balance_factor(node.right) <= 0:
                    return self.rotate_left(node)
                else:
                    node.right = self.rotate_right(node.right)
                    return self.rotate_left(node)
            return node

        self.root = _delete(self.root, key)
        self.size -= 1

    def get(self, key):
        current = self.root
        while current:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def get_max_key(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.key

    def __len__(self):
        return self.size

    def __iter__(self):
        def inorder_traversal(node):
            if node:
                yield from inorder_traversal(node.left)
                yield node.key, node.value
                yield from inorder_traversal(node.right)
        
        return inorder_traversal(self.root)