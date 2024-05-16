import turtle as tu

# Setup turtle and screen
roo = tu.Turtle()
wn = tu.Screen()
wn.bgcolor("black")
wn.title("Fractal Tree Patterns")

# Function to draw a fractal tree
def draw_tree(length, angle, depth):
    if depth == 0:
        return
    else:
        roo.pensize(2)
        roo.pencolor("yellow")
        roo.forward(length)
        roo.left(angle)
        draw_tree(length * 0.75, angle, depth - 1)
        roo.right(60)
        draw_tree(length * 0.75, angle, depth - 1)
        roo.left(angle)
        roo.backward(length)
        roo.pensize(2)

# Draw the fractal trees with varying colors and speeds
colors = ["yellow", "magenta", "red", "#FFF8DC", "lightgreen", "cyan"]
lengths = [20, 40, 60]
angles = [30, 30, 30, 30, 30, 30]

for i, color in enumerate(colors):
    roo.pensize(2)
    roo.pencolor(color)
    roo.speed(500)  # Adjust speed for visibility
    draw_tree(lengths[i], angles[i], 10)  # Adjust depth as needed
    roo.right(90)
    roo.speed(500)  # Reset speed for the next pattern

wn.exitonclick()
