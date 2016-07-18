import turtle
from sys import argv

colors = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange', 'brown']

def draw_triangle(points, color, my_turtle):
    """ use my_turtle.up(), down(), and goto() to draw a triangle.
        You can also use my_turtle.fillcolor(color), begin_fill(), and end_fill() to fill in the triangles with colors.

        points: list of the 3 points which represent the corners of the triangle
        color: which color
        my_turtle: an instance of turtle.Turtle

        Example: points = [[-300, -150], [0, 300], [300, -150]]
    """
    pass

def midpoint(p1, p2):
    """Return the midpoint of two points. A point is an ordered pair of two numbers.

    p1: an ordered pair (tuple or list), representing a Cartesian point
    p2: same as p1
    """
    pass

def sierpinski(points, degree, my_turtle):
    """Recursively draw the Sierpinski triangle.
       Use the above midpoint function and draw_triangle function to implement.

       points: The 3 points of the current triangle
       degree: The 3 points of the current triangle
       """
    pass

def main():
    """ Bootstrap the program.
        We set any configuration parameters here, create some necessary objects, and then run the sierpinski function."""
    my_turtle = turtle.Turtle()
    window = turtle.Screen()
    _, degree = argv
    points = [[-300, -150], [0, 300], [300, -150]]
    sierpinski(points, int(degree), my_turtle)
    window.exitonclick()

if __name__ == '__main__':
    main()
