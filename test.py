import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
spiral = turtle.Turtle()
spiral.speed(0)
spiral.pensize(2)

# Golden ratio approximation using Fibonacci numbers
fib = [1, 1]
for _ in range(20):  # Generate more Fibonacci numbers
    fib.append(fib[-1] + fib[-2])

# Scale factor for display
scale = 5

# Draw squares and spiral
def draw_fibonacci_spiral():
    spiral.penup()
    spiral.goto(0, 0)
    spiral.setheading(0)
    spiral.pendown()

    for i in range(len(fib) - 1):
        # Draw square
        for _ in range(4):
            spiral.forward(fib[i] * scale)
            spiral.left(90)

        # Draw quarter circle (arc) inside the square
        spiral.circle(-fib[i] * scale, 90)

# Run the function
draw_fibonacci_spiral()

# Finish
spiral.hideturtle()
turtle.done()
