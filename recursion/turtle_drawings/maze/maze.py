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

        file = open(maze_file_name, 'r')
        for line_index, line in enumerate(file):
            rows = []
            current_row = line.rstrip('\r\n')
            for col_index, char in enumerate(current_row):
                rows.append(char)
                if char == 'S':
                    self.start_row = line_index
                    self.start_col = col_index

            self.maze_list.append(rows)
            self.columns_in_maze = len(rows)

        self.rows_in_maze = len(self.maze_list)

        self.turtle = turtle.Turtle()
        self.turtle.shape('turtle')
        self.window = turtle.Screen()

        lower_left_x = -(self.columns_in_maze - 1) / 2 - 0.5
        lower_left_y = -(self.rows_in_maze - 1) / 2 - 0.5
        upper_right_x = (self.columns_in_maze - 1) / 2 + 0.5
        upper_right_y = (self.rows_in_maze - 1) / 2 + 0.5

        self.window.setworldcoordinates(lower_left_x, lower_left_y,
                                        upper_right_x, upper_right_y)
        self.window.exitonclick()


def main():
    my_maze = Maze('maze_input.txt')


if __name__ == '__main__':
    main()
