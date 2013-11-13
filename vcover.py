def vertex_cover_tree(input_graph):
    n = len(input_graph)
    assignment = [None]*n
    return recursive_vertex_cover(input_graph, assignment)

def validity_check(graph, cover):
    covered = 0
    edges = 0
    for i in range(0, len(graph)):
        for j in range(i+1, len(graph[i])):
            edges = edges + graph[i][j]
            covered = covered + graph[i][j] * ((cover[i]==1) or (cover[j]==1)) #NB x==1. Be prepared for None values.
    if None in cover:
        return None
    elif covered < edges:
        return False
    elif covered == edges:
        return True
    else:
        raise

def recursive_vertex_cover(input_graph, assignment):
    # - Check if it's still possible to construct a valid vertex cover,
    # if not, return float("inf") (the Python expression for infinity)
    # MORE COMPLEX CRUD
    validity = validity_check(input_graph, assignment)
    if validity == True:
        return sum(assignment)
    elif validity == False:
        return float("inf")
    elif validity == None:
        v = assignment.index(None)
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
