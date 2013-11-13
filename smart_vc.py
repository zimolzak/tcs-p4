# Write a function, recursive_vertex_cover which implements the
# improved vertex cover search tree of size 1.733^n, where instead
# of a single vertex, you always consider two vertices that are 
# connected by an edge but are both unassigned.
def vertex_cover_tree(input_graph):
    n = len(input_graph)
    assignment = [None]*n
    # print
    # print
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
    u = None
    v = None
    indent = len(assignment) - assignment.count(None)
    # print " " * indent, assignment
    for i in range(0, len(input_graph)):
        for j in range(i+1, len(input_graph[i])):
            if input_graph[i][j] and assignment[i]==0 and assignment[j]==0:
                # fail fast
                # print " " * indent, "fail"
                return float("inf")
    for i in range(0, len(input_graph)): # second loop because I want to faily REALLY fast, finding ALL invalids.
        for j in range(i+1, len(input_graph[i])):
            if input_graph[i][j] and assignment[i]==None and assignment[j]==None:
                # u and v connect, therefore do 3-way branch
                if not (u==None): # if we found an appropriate pair, don't keep looking
                    continue
                # print " " * indent, "branch"
                u = i
                v = j
    if u==None:
        # do the straightforward remaining assignments, but count ONLY. Don't actually assign.
        # print " " * indent, "straight"
        extra_assign_count = 0
        for i in range(len(assignment)): # i is the index of the Vtx we are checking.
            any_uncov_neigh = 0
            if not (assignment[i]==None): # skip any assigned Vtx.
                continue
            for j in range(len(input_graph)): # j is the index of the neighbor we are checking.
                if input_graph[i][j] == 0 or any_uncov_neigh: # skip if no edge betw Vtx and Neighbor.
                    continue
                if assignment[j] == 0: # There is an edge and it is UNcovered by Neighbor
                    any_uncov_neigh = 1
            extra_assign_count += any_uncov_neigh
        # print " " * indent, "    ==", assignment.count(1) + extra_assign_count
        return assignment.count(1) + extra_assign_count # do not use sum() or else you'll sum up NoneTypes
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

gx = [[0, 1, 0, 0, 1, 0, 0, 1],
      [1, 0, 1, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [1, 0, 0, 1, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 1, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 0, 0]]

print vertex_cover_tree(gx), "(expect 3)"

gy = [[0, 0, 0, 0, 1, 1], 
      [0, 0, 1, 0, 0, 0], 
      [0, 1, 0, 0, 0, 1], 
      [0, 0, 0, 0, 0, 0], 
      [1, 0, 0, 0, 0, 1], 
      [1, 0, 1, 0, 1, 0]]

print vertex_cover_tree(gy), "(expect 3)"

gz = [[0, 0, 0, 0, 1, 0, 1, 0], 
      [0, 0, 0, 0, 0, 0, 0, 0], 
      [0, 0, 0, 0, 1, 0, 0, 0], 
      [0, 0, 0, 0, 1, 0, 0, 0], 
      [1, 0, 1, 1, 0, 0, 1, 0], 
      [0, 0, 0, 0, 0, 0, 0, 1], 
      [1, 0, 0, 0, 1, 0, 0, 0], 
      [0, 0, 0, 0, 0, 1, 0, 0]]

print vertex_cover_tree(gz)
