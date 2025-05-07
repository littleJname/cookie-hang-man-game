
import turtle

# Set up the turtle
t = turtle.Turtle()
t.pensize(2)
t.color("blue")

# Function to draw hexagon
def draw_hexagon(size):
    for _ in range(6):
        t.forward(size)
        t.right(60)

# Draw the hexagon
draw_hexagon(100)

# Keep the window open
turtle.done()
