import turtle



def draw_spiral(origin, size, reps, my_turtle):
    """
    Draw a spiral recursively. There are many approaches, but I one suggest to start at the bottom left, and execute one lap, to bottom-right, top-right, top-left, and then the new bottom-left.

    origin: where to start
    size: where to start
    reps: where to start
    my_turtle: an instance of turtle.Turtle
    """
    if reps > 0:
        # TODO: Actually perform the drawing

        draw_spiral(new_origin, new_size, reps - 1, my_turtle)

def main():
    my_turtle = turtle.Turtle()
    window = turtle.Screen()
    draw_spiral([-200,-200], 400, 18, my_turtle)
    window.exitonclick()

if __name__ == '__main__':
    main()
