import turtle


def tree(t, branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(t, branch_len - 15)
        t.left(40)
        tree(t, branch_len - 10)
        t.right(20)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(t, 75)
    win.exitonclick()


if __name__ == '__main__':
    main()
