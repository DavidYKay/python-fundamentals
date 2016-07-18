import turtle
import numpy as np

COLORS = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange', 'brown']

def draw_rectangle(corners, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(*corners[0])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(*corners[1])
    my_turtle.goto(*corners[2])
    my_turtle.goto(*corners[3])
    my_turtle.goto(*corners[0])
    my_turtle.end_fill()

def recursive_squares():
    pass

def main():
    my_turtle = turtle.Turtle()
    window = turtle.Screen()
    draw_rectangle(
            [[50,50],
             [50,-50],
             [-50,-50],
             [-50,50]], "red", my_turtle)
    window.exitonclick()

if __name__ == '__main__':
    main()
