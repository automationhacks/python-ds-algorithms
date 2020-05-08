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
        self.window.setup(width=600, height=600)
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

        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate,
                                           -y + self.y_translate,
                                           'orange')

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

    def move_turtle(self, x, y):
        self.turtle.up()
        self.turtle.setheading(self.turtle.towards(x + self.x_translate,
                                                   -y + self.y_translate))
        self.turtle.goto(x + self.x_translate, -y + self.y_translate)

    def drop_breadcrumb(self, color):
        self.turtle.dot(10, color)

    def update_position(self, row, col, val=None):
        if val:
            self.maze_list[row][col] = val

        self.move_turtle(col, row)
        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == 'TRIED':
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.drop_breadcrumb(color)

    def is_exit(self, row, col):
        return (
                row == 0 or
                row == self.rows_in_maze - 1 or
                col == 0 or
                col == self.columns_in_maze - 1)

    def __getitem__(self, idx):
        return self.maze_list[idx]


def search_from(maze, start_row, start_column):
    maze.update_position(start_row, start_column)

    pos = maze[start_row][start_column]

    # Return false for all base cases
    if pos in (OBSTACLE, TRIED, DEAD_END):
        return False

    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_column, TRIED)

    # Use logical short circuiting to search in each direction
    found = search_from(maze, start_row - 1, start_column) or \
            search_from(maze, start_row + 1, start_column) or \
            search_from(maze, start_row, start_column - 1) or \
            search_from(maze, start_row, start_column + 1)

    if found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return found


def main():
    my_maze = Maze('maze_input.txt')
    my_maze.draw_maze()
    my_maze.update_position(my_maze.start_row, my_maze.start_col)
    search_from(my_maze, my_maze.start_row, my_maze.start_col)
    my_maze.destroy_world()


if __name__ == '__main__':
    main()
