from turtle import Turtle , heading 
from random import choice

# sets the global values which can be changed also
color =  [ "red", "blue", "green", "yellow", "purple", "orange", 'cyan' ]
NUM_SEG = 3
DIST_BETWEEN_SPAWN = -20
DIST_MOVE = 20

# sets the angle for the snake to turn
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# snake class is created
class Snake():
    
    def __init__(self):

        """this initiates the segments of body of snake of which first segment is head
         + crates the segments list which will keep the list of segment(objects) created
         + sets the initial co-ordinates
        ===for loop to create the initial segments of snake
            + creates the new object of class turtle
            + sets the position of segment to origin
            + appends the created segment object to segments list for 
              later use 
         + sets the forst segment as head
            """
        self.segments = []
        
        self.x = 0
        self.y = 0

    def create(self):
        for i in range(0,NUM_SEG ):    
            new_segments = Turtle('square')
            new_segments.color('white')
            new_segments.penup()
            new_segments.setposition(self.x , self.y)
            self.segments.append(new_segments)
            self.x += -DIST_BETWEEN_SPAWN
        self.head = self.segments[0] 
           
    
    def add_seg(self):

        """creates the new segment when method is called 
         + appends that segment object to list """

        new_segments = Turtle('square')
        
        x_cor = self.segments[-1].xcor()
        y_cor = self.segments[-1].ycor()

        new_segments.goto(x_cor , y_cor)
        new_segments.color("white")
        new_segments.penup() 
        self.segments.append(new_segments)


    def move (self):

        """when method is called 
        Every segment follows the previous segment  """

        for seg_index in range (len(self.segments)-1,0,-1):
            x_cor = self.segments[seg_index-1].xcor()
            y_cor = self.segments[seg_index-1].ycor()
            self.segments[seg_index].goto(x_cor,y_cor)
        self.head.forward(20)

    def left(self):
       if self.head.heading() != LEFT and self.head.heading()!= RIGHT:
           self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(DOWN)
    
    def clear_snake(self):
        for i in self.segments:
            i.goto(800,800)
        self.segments.clear()    
        

