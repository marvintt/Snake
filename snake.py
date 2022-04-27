from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    
    # Crear cuerpo de serpiente
    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment) 
        
    #Movimiento de la serpiente    
    def move_snake(self):
        for seg_num in range (len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(20)
        #self.segments[0].left(90)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)