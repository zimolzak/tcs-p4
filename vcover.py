# This and the next problem are mainly concerned with implementing the
# improved search tree for vertex cover. But before we do any
# improvements, let's implement the brute-force algorithm (the one
# with size 2^n) first before doing further optimizations.
#
# Write code in recursive_vertex_cover where specified.

# This function initializes and calls the search tree
def vertex_cover_tree(input_graph):
    n = len(input_graph)
    assignment = [None]*n
    # for row in input_graph:
    #    print row
    size = recursive_vertex_cover(input_graph, assignment)
    # print "size", size
    return size

# My function - AJZ
# True if a valid cover.
# False if invalid--IE if any edge has 0 on each side.
# None if not yet valid but still possible.
# COVER can have [0, 1, None]
def validity_check(graph, cover):
    covered = 0
    edges = 0
    for i in range(0, len(graph)):
        for j in range(i+1, len(graph[i])):
            edges = edges + graph[i][j]
            covered = covered + graph[i][j] * ((cover[i]==1) or (cover[j]==1)) #NB x==1. Be prepared for None values.
    # print "cov", covered, "of", edges, "with..."
    if None in cover:
        # print "indeter", cover
        return None
    elif covered < edges:
        # print "INV_ins", cover
        return False
    elif covered == edges:
        # print "  valid", cover
        return True
    else:
        raise #fixme How do I do this correctly?

# This function recursively builds the search tree
def recursive_vertex_cover(input_graph, assignment):
    ############
    # YOUR CODE GOES HERE
    #
    # - Check if it's still possible to construct a valid vertex cover,
    # if not, return float("inf") (the Python expression for infinity)
    # - If the assignment is a valid vertex cover, return the size of
    # that cover
    # - Otherwise, Find a vertex v that does not have an assignment
    validity = validity_check(input_graph, assignment)
    # Assignment can have [0, 1, None]
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
    ##############
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
    # vertex_cover_tree(g4)
    assert 3 == vertex_cover_tree(g4)

test()
