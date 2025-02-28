"""
Create A Snake Game: movement using "w" "a" "s" "d" for up, left, down, right. 
Every time snakes eat food increase in size, and game lose when move out bound.
File Name: tran_project1.py
Author: Anh Tran
Date: 4/12/24
Course: COMP1353 - Data Structures and Algorithms I
Assignment: Project 1 - Snake Game
Collaborators: Lisette Real Rico, Pluto Hassan, Jonathan Olvera-Duran, Andy Dang.
"""

import random
import dudraw

"""VECTOR METHOD FROM 1352"""
class Vector:
    """Vector use to take two points contains (x, y)"""
    def __init__(self, some_x=0, some_y=0):
        self.x = some_x
        self.y = some_y

    def __add__(self, other_vector):
        #add vector to a point with another point
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector):
        #subtract vector from one another
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __eq__(self, other_vector) -> bool:
        result = False
        if self.x == other_vector.x and self.y == other_vector.y:
            result = True
        return result

    def __isub__(self, other_vector):
        #subtract x and y value of self from other vector
        self.x -= other_vector.x
        self.y -= other_vector.y
        return self

    def __iadd__(self, other_vector):
        self.x += other_vector.x
        self.y += other_vector.y
        return self

class Node:
    """Node use to determine list is a DoubleLinkedList contain previous and next Node"""
    def __init__(self, v, p, n):
        self.value = v
        self.prev = p
        self.next = n

    def __str__(self) -> str:
        return str(self.value)

class DoublyLinkedList:
    """DoubleLinkedList take in Vector as (x, y) value asscessible when being called."""
    def __init__(self):
        
        self.header = Node(None, None, None)  
        self.trailer = Node(None, self.header, None) 
        self.header.next = (
            self.trailer
        )  
        self.size = 0

    def __str__(self):
        """Function return all points in the list."""
        if self.size == 0:
            return "[]"
        s = "["
        temp_node = self.header.next
        while temp_node.next is not self.trailer: #
            s += str(temp_node) + ", "
            temp_node = temp_node.next
        return (s + str(self.trailer.prev) + "]")  

    def is_empty(self) -> bool:
        """Return True if list is empty."""
        return self.size == 0

    def get_size(self):
        return self.size

    # adding __ before method name mangles the name so it's "private"
    def __add_between(self, v, n1, n2):
        """Function add an extra node between two node."""
        #error checking, and check if node between n1 and n2 exist
        if n1 is None or n2 is None:
            raise ValueError("n1 and n2 must exist")
        if n1.next is not n2:
            raise ValueError("n1 and n2 should have nothing between them")
        #new node if none exist
        new_node = Node(v, n1, n2)

        n1.next = new_node 
        n2.prev = new_node
        self.size += 1  

    def add_first(self, v):
        """Function add new Node after self.header as new leading value."""
        self.__add_between(v, self.header, self.header.next)

    def add_last(self, v):
        """Function add new Node before self.trailer as new lastest value."""
        self.__add_between(v, self.trailer.prev, self.trailer)

    def remove_between(self, node1, node2):
        if node1 is None or node2 is None:
            raise ValueError("node1 or node2 cannot be none")

        #check another node btw not n2
        if node1.next != node2.prev:
            raise ValueError("A single node must exist between node1 and node2")

        #changing node direction to create connection skipping one node in the middle
        temp = node1.next.value
        node1.next = node2
        node2.prev = node1
        self.size -= 1
        return temp

    def remove_first(self):
        return self.remove_between(self.header, self.header.next.next)

    def remove_last(self):
        return self.remove_between(self.trailer.prev.prev, self.trailer)

    def first(self):
        return self.header.next.value

    def last(self):
        return self.trailer.prev.value

    def search(self, value):
        #find value
        index = 0
        temp_node = self.header.next
        while temp_node is not self.trailer:
            if temp_node.value == value:
                return index

            temp_node = temp_node.next
            index += 1 #plus if temp.next to find value
        return -1

    def get(self, n):
        index = n
        count = 0
        temp = self.header.next

        if self.header == None: 
            raise ValueError("List is Empty")
        if n > self.size - 1: 
            raise IndexError("That index is not in the list")

        while count != index:
            count += 1
            temp = temp.next
        else:
            return temp.value  


class Snake:
    def __init__(self):
        self.snake = DoublyLinkedList()
        self.radius = 0.5
        # Starting RGB values
        self.r = 255
        self.x_pos = 10 - self.radius
        self.y_pos = 10 - self.radius

        for i in range(6):
            self.pos = Vector(self.x_pos, self.y_pos)
            # Append last assist draw from beginning x,y to end.
            self.snake.add_last(self.pos)
            self.y_pos -= (self.radius * 2)

    def draw(self):
        """Function loop through snake doublelinkedlist and draw base on coordinates given."""
        if self.snake.size != 0:  # if there is >= 1 node
            # Calculate initial RGB values for each segment
            #divide by how much element in the list for color division
            r = self.r / self.snake.size
            
            r_value = self.r
            
            # Draw each segment of the snake
            for section in range(self.snake.size):
                # Set color based on current RGB values
                dudraw.set_pen_color_rgb(int(r_value), int(r_value), int(r_value))
                dudraw.filled_square(self.snake.get(section).x, self.snake.get(section).y, self.radius)
                dudraw.set_pen_color(dudraw.BLACK)
                dudraw.square(self.snake.get(section).x, self.snake.get(section).y, self.radius)
                # Decrement RGB values for the next segment
                #max function give the largest value that r can keep taken away
                r_value = max(0, r_value - r)

    def move(self, key: str):
        """Based on key letter passed in, determine next move of snakes if valid."""
        if key == "w":  #move_up
            self.move_up()
        elif key == "a":  #move_left
            self.move_left()
        elif key == "s":  #move_down
            self.move_down()
        elif key == "d":  #move_right
            self.move_right()

    def move_up(self):
        """Function check for valid y increment only if not exceed upper bound."""
        #w key snakes move up only y-axis changing.
        if (self.snake.get(0).y + 1 <= 19.5):
            #shifted y value +1, and increase snakes by move last node to self.header.next
            self.snake.add_first(Vector(self.snake.get(0).x, self.snake.get(0).y + 1)) 
            self.snake.remove_last()
        else:
            #add new node to beginning
            self.snake.add_first(Vector(self.snake.get(0).x, self.snake.get(0).y))  

    def move_down(self):
        """Function check for valid y increment only if not exceed lower bound."""

        if (self.snake.get(0).y - 1 >= 0.5): 
            #only y-axis change which increment y -= 1.
            self.snake.add_first(Vector(self.snake.get(0).x, self.snake.get(0).y - 1))
            #replacement movement last to first method.
            self.snake.remove_last()
        else:
            self.snake.add_first(Vector(self.snake.get(0).x, self.snake.get(0).y))  

    def move_right(self):
        """Function check for valid x increment only if not exceed upper x bound."""

        #when the bound at 19.5 is valid, which only make beyond 19.5 unvalid by + 1.
        if (self.snake.get(0).x + 1 <= 19.5): 
            self.snake.add_first(Vector(self.snake.get(0).x + 1, self.snake.get(0).y))
            #after add new stored element, remove last element in the list calling remove_last
            self.snake.remove_last()
        else:
            self.snake.add_first(Vector(self.snake.get(0).x, self.snake.get(0).y))

    def move_left(self):
        """Function check for valid x increment only if not exceed lower x bound."""

        #value of x cannot be less than 0
        if (self.snake.get(0).x - 1 >= 0.5): 
            #continue shifting element to the left if valid.
            self.snake.add_first(Vector(self.snake.get(0).x - 1, self.snake.get(0).y))
            self.snake.remove_last()
        else:
            self.snake.add_first(Vector(self.snake.get(0).x, self.snake.get(0).y))

    def self_crash(self) -> bool:
        """Function compare head.next , first value (x,y) to others (x, y) in the body"""
        #temp node is get(1) the second value in the list.
        temp_node = (self.snake.header.next.next)  
        #compare get(0) (x,y) values compare it against all other values in the list.
        while (temp_node.next != self.snake.trailer):  
            if (self.snake.get(0) == temp_node.value): 
                return True
            temp_node = temp_node.next
        return False

    def bound_crash(self) -> bool:
        """Function check snakes points exceed limit bound of x,y return True, else False"""
        #Return false if bound x, y go beyond of canvas scale.
        if (self.snake.get(0).x >= 19.01 + self.radius or self.snake.get(0).x <= 0.99 - self.radius):
            return True
        if (self.snake.get(0).y >= 19.01 + self.radius or self.snake.get(0).y <= 0.99 - self.radius):  
            return True
        return False

    def crash(self):
        """When either function above True, it return True indicates end of the game."""
        result = False
        if self.self_crash() or self.bound_crash():
            result = True
        return result

    def valid_direction(self, prev, next):
        """Snakes have limits movement choice if move in a certain direction."""
        result = False
        #can't go up and down
        if prev != "s" and next == "w": 
            result = True
        #can't go down and up
        elif (prev != "w" and next == "s"):  
            result = True
        #can't go left or right
        elif prev != "a" and next == "d":  
            result = True
        #can't go right to left
        elif prev != "d" and next == "a":  
            result = True
        return result

    def eaten(self, food: object) -> bool:
        """Check if fruit coordinates is same as header.next first element coordinate."""
        #function return True or False assist 
        eaten = False
        #when head in same position as food, return True add new Node
        #food.pos consider as vector random x,y of snake food item.
        if (self.snake.first() == food.pos):  
            eaten = True  
        return eaten

    def growth(self):
        """If eaten is true this function will be called to add addition Node to the end."""
        #taking the last node value in the list to add new node.
        last_node = (self.snake.get_size() - 1)
        #adding new node to the end of the list.
        self.snake.add_last(Vector(self.snake.get(last_node).x, self.snake.get(last_node).y))


class Food:
    """Create food as an apple random on canvas"""
    def __init__(self):
        #since square is draw in the middle, all choosen x & y + 5 will gives center point.
        self.pos = Vector(random.randint(1,19)+0.5, random.randint(1,19)+0.5) 
        self.size = 0.5 

    def draw(self):
        dudraw.set_pen_width(0.2)
        dudraw.set_pen_color_rgb(88, 57, 39)

        dudraw.line(self.pos.x, self.pos.y, self.pos.x, self.pos.y + 0.7)
        dudraw.set_pen_width(0.1)

        dudraw.set_pen_color(dudraw.RED)
        #food shape manipulation
        dudraw.filled_circle(self.pos.x - 0.1, self.pos.y - 0.1, self.size)
      

    def generate_new_position(self, snake_holder: object):
        """Generate new position if fruit have been eaten, which found similar coordinate to snakes head(x,y)"""
        #new food being made, making first item random with self.pos
        new_pos = self.pos
        #first value in linked list object (x, y)
        temp_node = (snake_holder.snake.header.next) 

        #making new food for every time snake head same position to food coordinate
        while temp_node.next != snake_holder.snake.trailer: 
            if (new_pos == temp_node.value): 
                new_pos = Vector(random.randint(0, 19) + 0.5, random.randint(0, 19) + 0.5)
            #move to next node in snake object
            temp_node = (temp_node.next)  
        #setting new possition will change placement of food item
        self.pos = new_pos  

def main():
    dudraw.set_canvas_size(500, 500)
    dudraw.set_x_scale(0, 20)
    dudraw.set_y_scale(0, 20)
    dudraw.clear_rgb(79, 121, 66)
    snakes_holder = Snake()  
    food = Food()  
    snakes_holder.draw()  
    food.draw()  
    limit = 20 
    timer = 0 
    valid_key = ["w", "a", "s", "d"] 
    key = "d" 
    prevkey = key
    score = 0
    n = 0
    while True:
        timer += 1 
        if timer == limit: 
            dudraw.clear_rgb(79, 121, 66)
            timer = 0 

            if dudraw.has_next_key_typed():  
                #save previous and next_key key to detect movement error
                prevkey = key 
                newkey = (dudraw.next_key_typed())  

                if (newkey in valid_key):  
                    if snakes_holder.valid_direction(prevkey, newkey):  
                        key = newkey

            food.draw()
            if (snakes_holder.crash() == False):
                snakes_holder.draw() 
                snakes_holder.move(key)
            else:
                snakes_holder.draw()
                dudraw.set_pen_color(dudraw.WHITE)
                dudraw.set_font_size(20)
                dudraw.text(10, 9.5, "Game Over!")
            
            if snakes_holder.eaten(food) == True:
                #when Eaten function return True add addition Node at the end new trailer
                score += 1
                n += 1
                snakes_holder.growth()
                #new random position for food
                food.generate_new_position(snakes_holder)
                #every time snakes eaten the food, fasten movement
                if n == 4:
                    limit -= 1
                    n = 0
        dudraw.set_font_size(20)
        dudraw.text(18, 19, f"Score: {score}")
        dudraw.show(10)


if __name__ == "__main__":
    main()
