from BinaryTree import BinaryTree
class ExpressionTree(BinaryTree):
    def __str__(self)->str:
        return self._str_helper(self.root)
    
    def _str_helper(self, node)->str:
        
        if node.is_external():
            return str(node)
        return "(" + self._str_helper(node.left) + str(node) +  self._str_helper(node.right) + ")"
       
        
    def evaluate(self, node)->float:
        if str(node) == "+":
            return float(self.evaluate(node.left)) + float(self.evaluate(node.right))
        
        elif str(node) == "-":
            return float(self.evaluate(node.left)) - float(self.evaluate(node.right))
        
        elif str(node) == "*":
            return float(self.evaluate(node.left)) * float(self.evaluate(node.right))
        
        elif str(node) == "/":
            return float(self.evaluate(node.left)) / float(self.evaluate(node.right))
        
        else:
            return float(node.value)


def _main():
    tree = ExpressionTree()

    r = tree.add_root("+")
    rl = tree.add_left(r, "-")
    rll = tree.add_left(rl, "*")
    rlll = tree.add_left(rll, "-")
    rllll = tree.add_left(rlll, "11")
    rlllr = tree.add_right(rlll, "2")
    rllr = tree.add_right(rll, "3")
    rlr = tree.add_right(rl, "+")
    rlrl = tree.add_left(rlr, "-")
    rlrll = tree.add_left(rlrl, "8")
    rlrlr = tree.add_right(rlrl, "15")
    rlrr = tree.add_right(rlr, "2")
    rr = tree.add_right(r, "-")
    rrl = tree.add_left(rr, "+")
    rrll = tree.add_left(rrl, "42")
    rrlr = tree.add_right(rrl, "*")
    rrlrl = tree.add_left(rrlr, "+")
    rrlrll = tree.add_left(rrlrl, "3")
    rrlrlr = tree.add_right(rrlrl, "9")
    rrlrr = tree.add_right(rrlr, "+")
    rrlrrr = tree.add_right(rrlrr, "7")
    rrlrrl = tree.add_left(rrlrr, "3")
    rrr = tree.add_right(rr, "6")

    print(tree, end='')
    print('=',tree.evaluate(tree.root))


if __name__ == '__main__':
    _main()