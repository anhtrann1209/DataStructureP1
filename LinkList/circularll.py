import random

class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)
    
class DoublyCircularLinkedList:
    def __init__(self):
        self.cursor = None
        self.size = 0

    def __str__(self):
        if self.cursor is None:
            return "[]"

        s = "[" + str(self.cursor) + ", "
        temp = self.cursor
        while temp.next is not self.cursor:
            temp = temp.next
            s += str(temp) + ", "
        
        return s[:-2] + "]"

    def add_after_cursor(self, v):
        new_node = Node(v)

        if self.cursor is None:
            self.cursor = Node(v)
            self.cursor.next = self.cursor
            self.cursor.prev = self.cursor.next

        else:
            new_node.next = self.cursor.next
            new_node.prev = self.cursor
            self.cursor.next = new_node
            new_node.next.prev = new_node
        self.size += 1

    def str_backward(self):
        if self.cursor is None:
            return "[]"

        s = "[" + str(self.cursor.prev) + ", "
        temp = self.cursor.prev
        while temp.prev is not self.cursor:
            temp = temp.prev
            s += str(temp) + ", "

        return "[" + f"{str(self.cursor)}" + ", " + s[1:-2] + "]"

    def delete_cursor(self):
        #remove node pointed to the cursor and return its value
        #If list empty thrown an appropriate exception.
        #The cursor should updated point Node after cursor or None if list empty.
        #check if cursor is the only element
        if self.cursor is None:
            raise ValueError("List is empty!")
        #store remove value
        value = self.cursor.value
        
        if self.cursor.next == self.cursor:
            self.cursor = None
        else:
            #change next from previous node to cursor next element
            #change next element to connect with previous Node
            #finally change the main cursor Node
            self.cursor.prev.next = self.cursor.next
            self.cursor.next.prev = self.cursor.prev
            self.cursor = self.cursor.next

        return value
    
    def advance_cursor(self, n):
        """Move the cursor forward by n elements."""
        if self.is_empty():
            raise ValueError("List is empty")
        if n > self.size:
            raise ValueError("Steps exceed list size")
        
        for _ in range(n):
            self.cursor = self.cursor.next
        return self.cursor.value

        

    def get_value(self):
        #return value stored at the cursor
        #if list empty raise an appropriate exception
        if self.cursor is None:
            raise ValueError("List is Empty!")
        else:
            return self.cursor.value
    
    def is_empty(self)->bool:
        if self.cursor is None:
            return True
        return False
    
    def get_size(self):
        return f"Size of the list is {self.size} items."
    

def homework_driver():
    random.seed(1)
    test_list = DoublyCircularLinkedList()

    for i in range(10):
        test_list.add_after_cursor(i)
    while not test_list.is_empty():
        n = random.randint(0,9)
        test_list.advance_cursor(n)
        print(test_list.delete_cursor(), end='')
    print()

def main():
    homework_driver()

if __name__ == "__main__":
    main()