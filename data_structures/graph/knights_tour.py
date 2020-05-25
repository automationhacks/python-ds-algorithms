from data_structures.graph.graph import Graph


def build_knights_graph(chess_board_size):
    knights_graph = Graph()

    for row in range(chess_board_size):
        for col in range(chess_board_size):
            node_id = pos_to_node_id(row, col, chess_board_size)
            new_positions = generate_legal_moves(row, col, chess_board_size)

            for pos in new_positions:
                new_node_id = pos_to_node_id(pos[0], pos[1], chess_board_size)
                knights_graph.add_edge(node_id, new_node_id)

    return knights_graph


def pos_to_node_id(row, column, chess_board_size):
    # E.g. Given (1, 2) and size 5
    # (1 * 5) + 2 = 7
    return (row * chess_board_size) + column


def is_legal_coordinate(coordinate, chess_board_size):
    # Coord value should not be negative or greater than the board size
    return 0 <= coordinate < chess_board_size


def generate_legal_moves(x, y, chess_board_size):
    # Look at the 5 by 5 chess board and see the row, col positions from
    # a knight in the center to arrive at below positions
    new_moves = []

    move_offsets = [
        (-1, -2), (-1, 2),
        (-2, -1), (-2, 1),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]

    for move in move_offsets:

        # Get possible move and check the coordinate is not
        # off the chess board
        new_x = x + move[0]
        new_y = y + move[1]
        is_x_legal = is_legal_coordinate(new_x, chess_board_size)
        is_y_legal = is_legal_coordinate(new_y, chess_board_size)

        if is_x_legal and is_y_legal:
            new_moves.append((new_x, new_y))

    return new_moves


def test_build_knights_graph():
    graph = build_knights_graph(5)
    connections = graph.get_vertex(12).get_connections()
    keys = [connection.get_id() for connection in connections]
    assert keys == [5, 9, 1, 3, 15, 19, 21, 23]
