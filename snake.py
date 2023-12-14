import turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:

    def __init__(self):
        self.segment_turtles = []
        self.create_snake()
        self.head = self.segment_turtles[0]
    def create_snake(self):
        # Create segment turtles object using the Turtle class constructor.
        for pos in STARTING_POS:
            self.add_segment(pos)
    def add_segment(self, pos):
        segment = turtle.Turtle(shape='square')
        segment.color('red')
        segment.penup()
        segment.goto(pos)
        self.segment_turtles.append(segment)
    def extend(self):
        # -1 = write a negative number to start counting from the end of the list
        self.add_segment(self.segment_turtles[-1].position())
    def move(self):
        for seg_num in range(len(self.segment_turtles) - 1, 0, -1):
            new_x = self.segment_turtles[seg_num - 1].xcor()
            new_y = self.segment_turtles[seg_num - 1].ycor()
            self.segment_turtles[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

