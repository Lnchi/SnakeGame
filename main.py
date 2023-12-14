import time
# turtle module to create graphics and drawings
import turtle
from food import Food
from scoreBoard import Score
from snake import Snake

# Screen class to create canvas or window
# create a screen object: x=300, -x=-300, y=300, -y=-300, height=600, 1 square=20.
# Create the main turtle screen
screen = turtle.Screen()
# Set up the screen
screen.setup(700, 700)
screen.bgcolor('black')
# screen.tracer(0) to turn off automatic updating of the turtle graphics screen.
screen.tracer(0)
screen.title('Welcome to The Snake Game')
# create a new object snake/food from that class
snake = Snake()
food = Food()
score = Score()

# Set up key event handling / turtle.listen() method to set up event handling
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Function to quit the game
def quit_game():
    screen.bye()

# turtle.onkey() function to specify a function to call when a specific key is pressed.
# terminating the loop and closing the graphics window when it exits.
screen.onkey(quit_game, 'q')

# Main game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()
    # Detect collision with wall
    if snake.head.xcor() > 350 or snake.head.xcor() < -350 or snake.head.ycor() > 350 or snake.head.ycor() < -350:
        score.game_over()
        game_on = False
    # Detect collision with tail
    for seg in snake.segment_turtles[1:]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            game_on = False

# Keep the window open after the loop
turtle.done()

