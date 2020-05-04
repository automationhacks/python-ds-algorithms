# https://runestone.academy/runestone/books/published/pythonds/Recursion/pythondsSierpinskiTriangle.html

import turtle
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0].x, points[0].y)
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1].x, points[1].y)
    my_turtle.goto(points[2].x, points[2].y)
    my_turtle.goto(points[0].x, points[0].y)
    my_turtle.end_fill()


def get_mid(point1, point2):
    x = (point1.x + point2.x) / 2
    y = (point1.y + point2.y) / 2
    return Point(x, y)


def sierpinski(points, degree, my_turtle):
    color_map = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    draw_triangle(points, color_map[degree], my_turtle)

    if degree > 0:
        sub_triangle = [points[0], get_mid(points[0], points[1]),
                        get_mid(points[0], points[2])]
        sierpinski(sub_triangle, degree - 1, my_turtle)

        sub_triangle = [points[1], get_mid(points[0], points[1]),
                        get_mid(points[1], points[2])]
        sierpinski(sub_triangle, degree - 1, my_turtle)

        sub_triangle = [points[2], get_mid(points[2], points[1]),
                        get_mid(points[0], points[2])]
        sierpinski(sub_triangle, degree - 1, my_turtle)


def main():
    my_turtle = turtle.Turtle()
    win = turtle.Screen()
    my_turtle.speed(10)
    points = [Point(-300, -150), Point(0, 300), Point(300, -150)]
    sierpinski(points, 3, my_turtle)
    win.exitonclick()


if __name__ == '__main__':
    main()
