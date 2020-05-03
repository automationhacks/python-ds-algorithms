import turtle


def spiral(t, line_len):
    if line_len > 0:
        t.forward(line_len)
        t.right(90)
        spiral(t, line_len - 5)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    spiral(t, 100)
    win.exitonclick()


if __name__ == '__main__':
    main()
