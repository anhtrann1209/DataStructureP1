
"""
Creates grid map consist of trees=1, and concrete=0. Higher density means more trees, 
and lower density means more concretes less likely fire spreading.
Apply Stack() for Depth First Search; fire spread from right. And Queue() for Breadth First Search; fire spread from left.
Calculate density where fire spread critical points

File Name: tran_project3.py
Author: Anh Tran
Date: 01/05/24
Course: COMP1353 - Data Structures and Algorithms I
Assignment: Project 3 - Percolation Part 2
"""

import dudraw
import random
import matplotlib.pyplot as plt

"""CLASSES IMPORT NEEDED FOR PERCULATION"""
class dllNode:
    def __init__(self, v, p, n): 
        #value, previous, and next
        self.value = v
        self.prev = p
        self.next = n

    
    def __str__(self):
        return str(self.value)

class sllNode:
    def __init__(self, v, n):
        self.value = v
        self.next = n
    
    def __str__(self):
        return str(self.value)
    
class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __iter__(self):
        return SLLIterator(self.head)

    def is_empty(self)->bool:
        return self.head is None
    
    '''
    Method adds the value as the first node in the list
    returns nothing
    '''
    def add_first(self, v):
        #step 1: create a new node with value. Set its next
        #        to head reference
        new_node = sllNode(v, self.head)
        #Step 2: change the head to the new node
        self.head = new_node

        #step 3: increment the size
        self.size += 1
    def add_last(self, v):
        #add new node to as last element
        if self.head is None:
            self.add_first(v)
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = sllNode(v, None)            
        self.size += 1

    def min(self):
        minimum_value = 0

        if self.head is None:
            raise ValueError("List is empty!")
        
        temp_node = self.head
        minimum_value = self.head.value

        while temp_node.next is not None:
            if temp_node.value < minimum_value:
                minimum_value = temp_node.value
            temp_node = temp_node.next
        return minimum_value


    '''
    Method removes the first node in the list and returns
    the value removed
    '''
    def remove_first(self):
        #case 1: list is empty
        if self.head is None:
            raise ValueError("List is empty!")
        
        #case 2: list has values
        value_to_return = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value_to_return
    
    def remove_last(self):
        if self.head is None:
            raise ValueError("List is empty!")
        
        temp = self.head

        if temp.next is None:
            removed_value = self.head.value
            self.head = None
            self.size -= 1
            return removed_value
        
        while temp.next is not None:
            temp = temp.next
        
        removed_value = temp.next.value
        temp.next = None
        self.size -= 1
        return removed_value
    
    def remove_at_index(self, index):
        #remove element giving the index
        if self.head is None:
            raise ValueError("List is empty!")
        
        if index == 0:
            return self.remove_first()        

        temp = self.head
        for i in range(index-1):
            if temp.next is None:
                raise IndexError("Index out of range")
            temp = temp.next

        if temp.next is None:
            raise IndexError("Index out of range")

        removed_value = temp.next.value
        temp.next = temp.next.next
        self.size -= 1
        return removed_value
    
    def get(self, index):
        #return value stored at given index
        if self.head is None:
            raise ValueError("List is empty!")
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range!")

        temp = self.head
        for _ in range(index):
            temp = temp.next

        index_value = temp.value
        return index_value

    def __str__(self):
        #if the list is empty return []
        if self.head is None:
            return "[]"
        
        #list is not empty
        s = "["
        #stop the loop when we reach the last node
        temp_node = self.head
        while temp_node.next is not None:
            s += str(temp_node) + ", "
            temp_node = temp_node.next
        
        return s + str(temp_node) + "]"
    def first_value(self):
        if self.head is None:
            return "No value"
        else:
            return self.head.next.value

class DoublyLinkedList:
    def __init__(self):
        self.header = dllNode(None, None, None)
        self.trailer = dllNode(None,self.header, None)
        self.header.next = self.trailer
        self.size = 0

    def __iter__(self):
        return DLLIterator(self.header.next, self.trailer)

    #mangles the name so it make class private
    def __add_between(self,v,  n1, n2):
        # error checking both notes exist
        if n1 is None or n2 is None:
            raise ValueError("n1 and n2 must exist.")
        if n1.next is not n2:
            raise ValueError("There is something between")
        
        new_node = dllNode(v, n1, n2)
        n1.next = new_node
        n2.prev = new_node
        self.size += 1
    
    def add_first(self, v):
        self.__add_between(v, self.header, self.header.next)
    def add_last(self, v):
        self.__add_between(v, self.trailer.prev, self.trailer)
    def is_empty(self)->bool:
        return self.size == 0
    
    def __str__(self):
        temp_node = self.header.next
        list_value = '['
        if temp_node.next is None:
            raise ValueError("List is empty!")
        
        while temp_node.next is not self.trailer:
            list_value += str(temp_node) + ", "
            temp_node = temp_node.next
        return list_value + str(temp_node) + "]"
    
    def remove_between(self, node1, node2):

        if node1 is None or node2 is None:
            raise ValueError("node1 and node2 must exist.")
        if node1.next.next != node2:
            raise ValueError("More than 1 node between them")
        
        remove_value = node1.next.value
        #remove value in the middle of 2 node
        node1.next = node2
        node2.prev = node1
        self.size -= 1
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
        self.current = head
        self.trailor = tail
    def __next__(self):

        if self.current is not None and self.current.next is not None:
            value = self.current.value
            self.current = self.current.next
            return value
        raise StopIteration
    
    def __iter__(self):
        return self
    
class SLLIterator:
    #passing in the head
    def __init__(self, head):
        self.current = head
    
    def __next__(self):
        #advance pointer or next value
        if self.current is not None:
            value = self.current.value
            self.current = self.current.next
            return value
        #when value reach None
        raise StopIteration
    
    #why we need iterable method
    def __iter__(self):
        return self

"""FIRST IN LAST OUT"""
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

"""FIRST IN FIRST OUT"""
class Queue:
    def __init__(self):
        self.the_queue = DoublyLinkedList()
    
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


class Cell:
    def __init__(self, row, col):
        #create 2D dimension list giving row as width and height as column
        self.row = row
        self.col = col

class Forest:
    """
    Purpose: Create 2D-dimension grid consist of tree if float < density, else 0 for concrete no fire access.
    Parameter: width-column, height-row, density
    Return: Base on called function, a grid made with tree and concrete.
    """
    def __init__(self, width, height, density):
        self.width = width 
        self.height = height
        #generate random float 0-1 less than density qualify 1 as tree, else 0 if greater than 0.75
        self.grid = [[1 if random.random() < density else 0 for col in range(width)] for row in range(height)]

    "Iterate through every element in each row of self.grid"
    def print_grid(self):
        #for every row in grid access
        #for number representation in row
        for row in self.grid:
            #for every number in each row
            print(''.join(['{:3}'.format(cell) for cell in row]))


    def depth_first_search(self)->bool:
        """
        Purpose: Fire spread start from first row, last element, and spread around it neighbor top, bottom, left, right.
        Parameter: Stack() class uses SingleLinkedList() class and sllNode() class.
        Return: return True if fire forest spreads and False otherwise.
        """
        stack = Stack()
        #iterator only loop through row 1 where the fire start
        for col in range(self.width):
            #for every element in first row, changes from tree to fire 1 = 2.
            if self.grid[0][col] == 1:
                #travel down to each colunm
                self.grid[0][col] = 2
                #add object cell with 0 as row and changes in column
                #cell append col the value at the place where fire spread
                stack.push(Cell(0, col))

        #check the list is not empty, and not empty proceed fire spread
        while stack.is_empty() == False:
            #remove the last cell object from stack
            """ACTIVATE DUDRAW HERE"""
            # self.draw()
            cell = stack.pop()
            #if reaches the bottom row
            if cell.row == self.height-1:
                return True

            #checking for open space on top which row above current_row
            #must not surpass 0 as first row.
            if cell.row-1 >= 0:
                #for every value at grid is 1 as tree, changes to fire
                if self.grid[cell.row-1][cell.col] == 1:
                    self.grid[cell.row-1][cell.col] = 2
                    stack.push(Cell(cell.row-1, cell.col))
            #changes in col, checking for element on the left which cannot exceed first value index 0.
            if cell.col-1 >= 0:
                if self.grid[cell.row][cell.col-1] == 1:
                    self.grid[cell.row][cell.col-1] = 2
                    #cell represent location of the object
                    stack.push(Cell(cell.row, cell.col-1))
            #checking for value to the right of the fire, current forest position
            if cell.col+1 <= self.height-1:
                if self.grid[cell.row][cell.col+1] == 1:
                    self.grid[cell.row][cell.col+1] = 2
                    stack.push(Cell(cell.row, cell.col+1))
            #checking for space below current forest position
            if cell.row+1 <= self.height-1:
                #for space occupy with tree, change to fire
                if self.grid[cell.row+1][cell.col] == 1:
                    self.grid[cell.row+1][cell.col] = 2
                    #push add cell object to the top of the sll
                    stack.push(Cell(cell.row+1, cell.col))
        #return False if fire did not reach the bottom
        #self.grid of stack return to 0

        return False  

    def breadth_first_search(self)->bool:
        """
        Purpose: Fire Spread from left to rigth follow FIFO (First In First Out) rule using queue data structure.
        Parameter: Queue() class, DoubleLinkedList() class, dllNode() class
        Return: return True if fire forest spreads and False otherwise.
        """
        queue = Queue()

        #for number in column changes in first row, if tree, changes to fire
        for col in range(self.width):
            if self.grid[0][col] == 1:
                #make tree to fire
                self.grid[0][col] = 2
                #add cell object to the last element using add_last()
                queue.enqueue(Cell(0, col))

        #loop run when there is elements in Queue()
        while queue.is_empty() == False:
            # self.draw()
            #dequeue() remove the first object
            cell = queue.dequeue()
            #check if the fire reaches last row
            if cell.row == self.height-1:
                #Fire has spreads to the bottom row
                return True 
            
            """Same algorithms checking for neighbor available fire spreading space."""
            #checking for open space on top which row above current_row
            #must not surpass 0 as first row.            
            if cell.row-1 >= 0:
                #for every value at grid is 1 as tree, changes to fire
                if self.grid[cell.row-1][cell.col] == 1:
                    self.grid[cell.row-1][cell.col] = 2
                    queue.enqueue(Cell(cell.row-1, cell.col))

            #changes in col, checking for element on the left which cannot exceed first value index 0.
            if cell.col-1 >= 0:
                if self.grid[cell.row][cell.col-1] == 1:
                    self.grid[cell.row][cell.col-1] = 2
                    queue.enqueue(Cell(cell.row, cell.col-1))

            #checking for value to the right of the fire, current forest position
            if cell.col+1 <= self.height-1:
                if self.grid[cell.row][cell.col+1] == 1:
                    self.grid[cell.row][cell.col+1] = 2
                    #cell add to last element of the line, represent location of the object
                    queue.enqueue(Cell(cell.row, cell.col+1))
            
            #checking for space below current forest position
            if cell.row+1 <= self.height-1:
                if self.grid[cell.row+1][cell.col] == 1:
                    self.grid[cell.row+1][cell.col] = 2
                    queue.enqueue(Cell(cell.row+1, cell.col))

        #return False if fire did not reach the bottom
        #self.grid of Queue return to 0
        return False  
    
    def draw(self):
        """
        Purpose: draw on dudraw grid using i and j as paramater for squares.
        Parameter: None
        Return: import dudraw and draw.
        """
        #say x is 10
        #say y is 10
        square_size = 1
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                #x corresponding to column
                #y corresponde to row
                if self.grid[i][j] == 1:
                    dudraw.set_pen_color(dudraw.GREEN)
                elif self.grid[i][j] == 2:
                    dudraw.set_pen_color(dudraw.RED)
                else:
                    dudraw.set_pen_color(dudraw.GRAY)
                #add 0.5 shift row and column to the right and top once.
                dudraw.filled_square(j+0.5, i+0.5, 0.5)
        dudraw.show(100)

class FireProbability:
    """Contains method to calculate fire spread probability for given density"""
    """FINDING CRITICAL PROBABILITY"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def probability_of_fire_spread_dfs(self, density):
        """
        Purpose: Input different density from 0.01 to 1, and see whether fire_spread() for dfs
        Parameter: density = [0.01, 1]
        Return: 1 if fire_spread and 0 else.
        """
        #use depth first search to determine if fire spreads
        trials = 1000
        fire_spread_count = 0

        for _ in range(trials):
            fire_prob_dfs = Forest(self.width, self.height, density)
            if fire_prob_dfs.depth_first_search():
                fire_spread_count += 1

        probability_spead_dfs = fire_spread_count/1000
        return probability_spead_dfs

    def probability_of_fire_spread_bfs(self, density):
        """
        Purpose: Input different density from 0.01 to 1, and see whether fire_spread() for bfs
        Parameter: density = [0.01, 1]
        Return: 1 if fire_spread and 0 else.
        """
        #use breadth first search to determine if fire spreads

        trials = 1000
        fire_spread_count = 0
        for _ in range(trials):
            fire_prob_bfs = Forest(self.width, self.height, density)
            if fire_prob_bfs.breadth_first_search():
                fire_spread_count += 1

        probability_spead_bfs = fire_spread_count/1000
        return probability_spead_bfs

    def highest_density_dfs(self):
        """Purpose: Computer critical probability results in fire using depth first search.
        Parameter: None
        Return: 1.0 if p > 0.5 else 0"""

        low_density = 0.0
        high_density = 1.0
        for n in range(20):
            #0.5
            density = (high_density + low_density) / 2.0

            #get probability of fire spreading in forest of 'density
            p = self.probability_of_fire_spread_dfs(density)
            
            if p<0.5:
                #low probability: density can be increase
                low_density = density
            else:
                #high probability: density should be decreased
                high_density = density
        #the last value of density is the value we seek
        return density
    
    def highest_density_bfs(self):
        """Critical probability fire spreads using breadth first search.
        Parameter: None
        Return: 1.0 if p > 0.5 else 0"""

        low_density = 0.0
        high_density = 1.0

        for n in range(20):
            #0.5
            density = (high_density + low_density) / 2.0

            #get probability of fire spreading in forest of 'density
            p = self.probability_of_fire_spread_bfs(density)

            if p<0.5:
                #low probability: density can be increase
                low_density = density
            else:
                #high probability: density should be decreased
                high_density = density
        #the last value of density is the value we seek
        return density
    

def main():
    """Main function called tested algorithsm of Depth First Search and Breadth First Search
    Calculate critical points base on density to see where the fire start spreading."""
    width = 30
    height = 30
    dudraw.set_canvas_size(400,400)
    dudraw.set_x_scale(0,width)
    dudraw.set_y_scale(0,height)

    fire_prob = FireProbability(width, height)

    #critical points where the fire start spreading base on density
    critical_dfs = fire_prob.highest_density_dfs()
    print(f"Critical Probability for DFS, {critical_dfs:.2f}")

    critical_bfs = fire_prob.highest_density_bfs()
    print(f"Critical Probability for BFS, {critical_bfs:.2f}")

    #x = tree density
    #y = probability of fire_spreads

    #stored density level from 0.01 to 1
    density_list = []
    #list level either 1 or 0 float
    prob_dfs = []

    #for more or less density points
    for densities in range(0, 101):
        # convert to float between 0 and 1
        densities /= 100.0  
        density_list.append(densities)
        # Compute probability of fire spread for DFS and BFS
        probability_spead_dfs = fire_prob.probability_of_fire_spread_bfs(densities)
        prob_dfs.append(probability_spead_dfs)

    print(density_list)
    print(prob_dfs)
    # #data points
    plt.plot(density_list, prob_dfs, label='DFS & BFS')
    #labels and title
    plt.xlabel('Density')
    plt.ylabel('Probability of Fire Spread')
    plt.title('Probability of Fire Spread vs. Density')
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()
