def vertex_cover_tree(input_graph):
    n = len(input_graph)
    assignment = [None]*n
    return recursive_vertex_cover(input_graph, assignment)

def recursive_vertex_cover(input_graph, assignment):
    # - Check if it's still possible to construct a valid vertex cover,
    # if not, return float("inf") (the Python expression for infinity)
    # MORE COMPLEX CRUD
    covered = 0
    edges = 0
    for i in range(0, len(input_graph)):
        for j in range(i+1, len(input_graph[i])):
            edges = edges + input_graph[i][j]
            covered = covered + input_graph[i][j] * ((assignment[i]==1) or (assignment[j]==1)) #NB x==1.
    if None in assignment:
        v = assignment.index(None)
    elif covered < edges:
        return float("inf")
    elif covered == edges:
        return sum(assignment)
    else:
        raise
    # END OF YOUR CODE. The following code takes care of the recursive
    # branching. Do not modify anything below here!
    assignment[v] = 0
    size_v_0 = recursive_vertex_cover(input_graph, assignment)
    assignment[v] = 1
    size_v_1 = recursive_vertex_cover(input_graph, assignment)
    assignment[v] = None
    return min(size_v_0, size_v_1)

def test():
    g1= [[0, 1],
         [1, 0]]
    g2= [[0, 1, 1],
         [1, 0, 0],
         [1, 0, 0]]
    g4= [[0, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [1, 0, 1, 0, 1],
         [1, 1, 1, 1, 0]]
    assert 1 == vertex_cover_tree(g1)
    assert 1 == vertex_cover_tree(g2)
    assert 3 == vertex_cover_tree(g4)

test()
