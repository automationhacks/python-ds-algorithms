def knights_tour_dfs(cur_depth, path, vertex_to_explore, limit):
    vertex_to_explore.set_color('gray')
    path.append(vertex_to_explore)

    if cur_depth < limit:
        # Uncomment below to perform warnsdoff optimization
        # of visiting corners first than the center
        # neighbours = order_by_avail(vertex_to_explore)
        neighbours = list(vertex_to_explore.get_connections())

        i = 0
        done = False

        while i < len(neighbours) and not done:
            if neighbours[i].get_color() == 'white':
                done = knights_tour_dfs(cur_depth + 1, path, neighbours[i],
                                        limit)
            i += 1

        if not done:
            # prepare to backtrack
            path.pop()
            vertex_to_explore.set_color('white')
    else:
        # If current depth = limit, we have found the solution to
        # knights tour problem (i.e. path with 64 vertices)
        done = True
    return done


def order_by_avail(vertex):
    result = []
    for adjacent_vertex in vertex.get_connections():
        if adjacent_vertex.get_color() == 'white':
            counter = 0
            # For every adjacent, keep a count of no of unvisited
            # vertices in its adjacency list
            for neighbour in adjacent_vertex.get_connections():
                if neighbour.get_color() == 'white':
                    counter += 1

            result.append((counter, adjacent_vertex))

    # Sort the result list based on the no of adjacent vertices
    # to have smaller result first
    result.sort(key=lambda x: x[0])
    return [vertex[1] for vertex in result]
