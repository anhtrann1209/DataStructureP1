class TreeNode:
    def __init__(self, v, p):
        self.value = v
        self.left = None
        self.right = None
        self.parent = p
    
    def ancestors(self):
        ancestors_list = []
        current_node = self.parent
        while current_node is not None:
            ancestors_list.append(current_node)
            current_node = current_node.parent
        return ancestors_list

    def node_depth(self):
        depth = 0
        current_node = self
        while current_node.parent is not None:
            depth += 1
            current_node = current_node.parent
        return depth

    def is_external(self):
        return self.left is None and self.right is None
    
    def is_internal(self):
        return not self.is_external()
    
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)
    
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def node_depth(self, node):
        return node.node_depth()

    def recursive_node_depth(self, node):
        if node.parent is None:
            return 0
        else:
            return 1 + self.recursive_node_depth(node.parent)
    
    def add_root(self, v):
        if self.root is not None:
            raise ValueError("Tree is not empty")
        self.root = TreeNode(v, None)
        self.size += 1
        return self.root
    
    def add_left(self, parent, v):
        if parent.left is not None:
            raise ValueError("Left child already exists")
        parent.left = TreeNode(v, parent)
        self.size += 1
        return parent.left
    
    def add_right(self, parent, v):
        if parent.right is not None:
            raise ValueError("Right child already exists")
        parent.right = TreeNode(v, parent)
        self.size += 1
        return parent.right
    
    def __recursive_pretty_print(self, r, level):
        if r is None:
            return
        print("   "*level + str(r.value))
        self.__recursive_pretty_print(r.left, level + 1)
        self.__recursive_pretty_print(r.right, level + 1)
    
    def pretty_print(self):
        self.__recursive_pretty_print(self.root, 0)

    def str_recursive(self, r, level) -> str:
        if r is None:
            return ""
        return ("   "*level + str(r) + "\n" + self.str_recursive(r.left, level + 1) + self.str_recursive(r.right, level + 1))

    def __str__(self):
        return self.str_recursive(self.root, 0)

    def tree_search(self, r, k):
        if r is None or k == r.value:
            return r
        if k < r.value:
            return self.tree_search(r.left, k)
        else:
            return self.tree_search(r.right, k)
    
    def tree_insert(self, r, k):
        if r is None:
            return TreeNode(k, None)
        else:
            if k < r.value:
                if r.left is None:
                    r.left = TreeNode(k, r)
                else:
                    self.tree_insert(r.left, k)
            else:
                if r.right is None:
                    r.right = TreeNode(k, r)
                else:
                    self.tree_insert(r.right, k)

    def remove(self, node):
        # Placeholder for node removal logic
        pass
        
def driver():
    tree = BinaryTree()
    one = tree.add_root(1)
    two = tree.add_left(one, 2)
    three = tree.add_right(one, 3)
    four = tree.add_left(two, 4)
    tree.add_right(two, 5)
    tree.add_left(four, 7)
    tree.add_right(four, 8)
    six = tree.add_left(three, 6)
    tree.add_left(six, 9)
    tree.add_right(six, 10)

    print(preorder_output(tree, tree.root))
    print(tree)

def preorder_output(tree, node):
    if node is None:
        return ""
    return str(node) + " " + preorder_output(tree, node.left) + preorder_output(tree, node.right)

def main():
    driver()

if __name__ == "__main__":
    main()
