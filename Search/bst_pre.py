from random import randint
class TreeNode:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
        self.parent = None
    
    def is_external(self):
        return self.left is None and self.right is None
    
    def is_internal(self):
        return not self.is_external()
    
    def __str__(self):
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)
    

class TreeSet:
    #constructor
    def __init__(self):
        self.root = None
        self.size = 0

    
    def get_size(self):
        return self.size 
    
    def is_empty(self):
        return self.size == 0
    
    def _add_recursive(self, r, v):
        """Root, value"""
        if r is None:
            r = TreeNode(v)
            self.size += 1
            return r
        
        #the clone comparing values
        elif v < r.value:
            r.left = self._add_recursive(r.left, v)
            r.left.parent = r

        elif v > r.value:
            r.right = self._add_recursive(r.right, v)
            r.right.parent = r
        
        #return the root of subtree after add is successful
        #or it will return the root of subtree unchanged if r.value == v
        return r
    
    def add(self, v)->None:
        #a new root after added
        self.root = self._add_recursive(self.root, v)

    def _discard_recursive(self, r, v):
        """Return the root of the tree after discard happenned"""
        #theres no value in the subtree
        #when you're deciding what to return, when worker done does the root change?
        if r is None:
            return None
        #recursive step: search
        if v < r.value:
            r.left = self._discard_recursive(r.left, v)
            #check if the value passing back is None.
            #it could remive empty subtree
            if r.left is not None:
                r.left.parent = r
        elif v > r.value:
            r.right = self._discard_recursive(r.right, v)
            if r.right is not None:
                r.right.parent = r
        #you found the value
        else:
            #case 1: r is a leaf
            if r.is_external():
                self.size -= 1
                return None
            #case 2: r has one child
            if r.left is None:
                self.size -= 1
                return r.right
            if r.right is None:
                self.size -= 1
                return r.left
            else:

            #case 3: r have two childrens
            #find precesstor, go left once and go right furthest.
                pred = r.left

                while pred.right is not None:
                    pred = pred.right
            
            #copy the value of the predecessor
                r.value = pred.value
            #remove pred value from left sub tree.
                r.left = self._discard_recursive(r.left, pred.value)
            #we don't remove since we only copy the node.
        return r
        
    def print_sorted(self):
        """print value in order:
        sort the left hand, sort right hand, insert root"""
        self._print_sorted_recursive(self.root)
    
    def _print_sorted_recursive(self, r):

        if r is None:
            return 
        #check on all left child of left tree side
        
        self._print_sorted_recursive(r.left) 
        print(" " + str(r) + " ") 
        self._print_sorted_recursive(r.right)


    def discard(self, v)->None:
        self.root = self._discard_recursive(self.root, v)

    def contains(self, v) -> bool:
        return self._contains_recursive(self.root, v)

    def _contains_recursive(self, r, v) -> bool:
        if r is None:
            return False
        if r.value == v:
            return True
        elif v < r.value:
            return self._contains_recursive(r.left, v)
        else:
            return self._contains_recursive(r.right, v)
        
 
    def min(self):
        if self.is_empty():
            return None
        current = self.root
        while current.left is not None:
            #goes to the most lefted child
            current = current.left
        return current.value

    def max(self):
        if self.is_empty():
            return None
        current = self.root
        while current.right is not None:
            #goes to most righted child greatest value
            current = current.right
        return current.value

    def union(self, other):
        pass

    def intersection(self, other):
        pass

    def difference(self, other):
        pass

    def _recursive_str(self, r, level):
        if r is None:
            return ""
        
        return level * "   " + str(r) + "\n" + self._recursive_str(r.left, level+1) + self._recursive_str(r.right, level+1)
    
    def __str__(self):
        return self._recursive_str(self.root, 0)

tree = TreeSet()

for i in range(0, 100, 10):
    tree.add(i)

print(tree.print_sorted())

print(tree.min())
print(tree.max())

while True:
    value = int(input("What value you want to remove: "))
    tree.discard(value)
    print(tree)
    print(tree.get_size())
    

