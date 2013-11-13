# Write a function, recursive_vertex_cover which implements the
# improved vertex cover search tree of size 1.733^n, where instead
# of a single vertex, you always consider two vertices that are 
# connected by an edge but are both unassigned.
def vertex_cover_tree(input_graph):
    n = len(input_graph)
    assignment = [None]*n
    return recursive_vertex_cover(input_graph, assignment)

def recursive_vertex_cover(input_graph, assignment):
    # Your code goes here:
    # - Check if it's still possible to construct a valid vertex cover,
    # if not, return float("inf") (the Python expression for infinity)
    # - Find two vertices u and v that are still not assigned, and assign
    #   them
    # - If no two such vertices can be found, output the size of the
    #   vertex cover implied by the current assignment (Careful: There
    #   might still be vertices that are unassigned - but, as you learned
    #   in the course, it's straightforward to tell if these should
    #   count as a 1 or a 0.)
    covered = 0
    edges = 0
    for i in range(0, len(input_graph)):
        for j in range(i+1, len(input_graph[i])):
            edges = edges + input_graph[i][j]
            covered = covered + input_graph[i][j] * ((assignment[i]==1) or (assignment[j]==1)) #NB x==1.
    if None in assignment:
        u = assignment.index(None)
        assignment[u] = 666 #temp value so X.index() returns next idx of None
        if None in assignment:
            v = assignment.index(None)
        else:
            v = u
    elif covered < edges:
        return float("inf")
    elif covered == edges:
        return sum(assignment)
    else:
        raise
    # END OF YOUR CODE. The following code takes care of the recursive
    # branching. Do not modify anything below here!
    assignment[u] = 1
    assignment[v] = 0
    size_10 = recursive_vertex_cover(input_graph, assignment)
    assignment[u] = 0
    assignment[v] = 1
    size_01 = recursive_vertex_cover(input_graph, assignment)
    assignment[u] = 1
    assignment[v] = 1
    size_11 = recursive_vertex_cover(input_graph, assignment)
    assignment[u] = None
    assignment[v] = None
    return min(size_10, size_01, size_11)


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
