# YouTube: https://www.youtube.com/watch?v=TB1p93msBFQ&list=PLtbC5OfOR8apSTahYrGIeEcp3nAB2o_CM&index=7
# Book: https://runestone.academy/runestone/books/published/pythonds/Recursion/ExploringaMaze.html
import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


class Maze:
    def __init__(self, maze_file_name):
        self.maze_list = []
        self.start_row = None
        self.start_col = None
        self.columns_in_maze = None
        self.turtle = turtle.Turtle()
        self.window = turtle.Screen()

        self.init_maze_from_file(maze_file_name)
        self.rows_in_maze = len(self.maze_list)
        self.x_translate = -self.columns_in_maze / 2
        self.y_translate = self.rows_in_maze / 2

        self.init_turtle_with_world()

    def init_turtle_with_world(self):
        self.turtle.shape('turtle')
        lower_left_x = -(self.columns_in_maze - 1) / 2 - 0.5
        lower_left_y = -(self.rows_in_maze - 1) / 2 - 0.5
        upper_right_x = (self.columns_in_maze - 1) / 2 + 0.5
        upper_right_y = (self.rows_in_maze - 1) / 2 + 0.5
        self.window.setworldcoordinates(lower_left_x, lower_left_y,
                                        upper_right_x, upper_right_y)

    def destroy_world(self):
        self.window.exitonclick()

    def init_maze_from_file(self, maze_file_name):
        with open(maze_file_name, 'r') as f:
            for line_index, line in enumerate(f):
                rows = []
                current_row = line.rstrip('\r\n')
                for col_index, char in enumerate(current_row):
                    rows.append(char)
                    if char == 'S':
                        self.start_row = line_index
                        self.start_col = col_index

                self.maze_list.append(rows)
                self.columns_in_maze = len(rows)

    def draw_maze(self):
        self.turtle.speed(10)
        self.window.tracer(0)
        for x, row in enumerate(self.maze_list):
            for y, col in enumerate(row):
                if col == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate,
                                           -y + self.y_translate, 'orange')
        self.turtle.color('black')
        self.turtle.fillcolor('blue')
        self.window.tracer()
        self.window.tracer(1)

    def draw_centered_box(self, x, y, color):
        self.turtle.up()
        self.turtle.goto(x - 0.5, y - 0.5)
        self.turtle.color(color)
        self.turtle.fillcolor(color)
        self.turtle.setheading(90)
        self.turtle.down()
        self.turtle.begin_fill()

        for i in range(4):
            self.turtle.forward(1)
            self.turtle.right(90)
        self.turtle.end_fill()


def main():
    my_maze = Maze('maze_input.txt')
    my_maze.draw_maze()
    my_maze.destroy_world()


if __name__ == '__main__':
    main()
