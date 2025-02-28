import random
import time
class Node:
    def __init__(self, v, p, n): 
        #value, previous, and next
        self.value = v
        self.prev = p
        self.next = n

    
    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None,self.header, None)
        self.header.next = self.trailer
        self.size = 0

    def __iter__(self):
        return DLLIterator(self.header, self.trailer)

    #mangles the name so it make class private
    def __add_between(self,v,  n1, n2):
        # error checking both notes exist
        if n1 is None or n2 is None:
            raise ValueError("n1 and n2 must exist.")
        if n1.next is not n2:
            raise ValueError("There is something between")
        
        new_node = Node(v, n1, n2)
        n1.next = new_node
        n2.prev = new_node
        self.size += 1
    
    def is_empty(self)->bool:
        return self.size == 0
    
    def add_first(self, v):
        self.__add_between(v, self.header, self.header.next)
    def add_last(self, v):
        self.__add_between(v, self.trailer.prev, self.trailer)
    
    def __str__(self):
        temp_node = self.header.next
        list_value = '['
        if temp_node is self.trailer:
            return '[]'
        
        while temp_node.next is not self.trailer:
            list_value += str(temp_node) + ", "
            temp_node = temp_node.next
        return list_value + str(temp_node) + "]"
    
    "REMOVE A VALUE"
    def remove_value(self, value):
        temp = self.header.next
        while temp.value != value and temp is not self.trailer:
            temp = temp.next
        
        if temp is self.trailer:
            return None
        
        return self.remove_between(temp.prev, temp.next)
    
    def remove_between(self, node1, node2):

        if node1 is None or node2 is None:
            raise ValueError("node1 and node2 must exist.")
        if node1.next != node2.prev:
            raise ValueError("More than 1 node between them")
        
        remove_value = node1.next.value
        #remove value in the middle of 2 node
        node1.next = node2
        node2.prev = node1
        return remove_value
    
    def remove_first(self):
        return self.remove_between(self.header, self.header.next.next)

    def remove_last(self):
        return self.remove_between(self.trailer.prev.prev, self.trailer)
    
    def search(self, value):
        #takes in a value, returns the index of first occurence of that values.
        #if not found: return -1
        #header can be change
        index = -1
        temp = self.header.next
        while temp is not None and temp.value != value:
            temp = temp.next
            index += 1
        
        if temp is None:
            return -1
        else:
            return f"Index of the value: {index}"

class DLLIterator:
    def __init__(self, head, tail):
        self.current = head.next
        self.trailor = tail

    def __next__(self):

        if self.current is self.trailor:
            raise StopIteration

        value = self.current.value
        self.current = self.current.next
        return value
    
    def __iter__(self):
        return self

def main():

    dll = DoublyLinkedList()
    for i in range(10):
        dll.add_first(i+1)
    
    iterator = iter(dll)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


if __name__ == "__main__":
    main()