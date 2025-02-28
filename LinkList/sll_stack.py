#this is my implementation. You can use your doubly linked list implementation instead
#WARNING: YOU MAY NEED TO MODIFY THIS IMPORT
from sll import SinglyLinkedList

#We must use the head of the singly linked list
# as the top the stack in order
#to achieve O(1) runtime
class Stack:
    def __init__(self):
        self.the_stack = SinglyLinkedList()
  
    def push(self, v):
        self.the_stack.add_first(v)

    def pop(self):
        return self.the_stack.remove_first()

    def top(self):
        return self.the_stack.first_value()

    def size(self):
        return self.the_stack.size
    
    def is_empty(self):
        return self.the_stack.is_empty()

class Queue:
    def __init__(self):
        self.the_queue = SinglyLinkedList()
    
    def enqueue(self, v):
        return self.the_queue.add_last(v)
    
    def dequeue(self):
        return self.the_queue.remove_first()
    
    def first(self):
        return self.the_queue.first_value()
    
    def size(self):
        return self.the_queue.size
    
    def is_empty(self):
        return self.the_queue.is_empty()

def main():
    pass

    

if __name__=="__main__":
    main()