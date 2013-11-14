# 1) If any clause consists of a single variable, set the variable so
# that this clause is satisfied
#
# 2) If a variable appears just once (and it hasn't been set, see
# below), set it so that the respective clause is satisfied
#
# 3) Remove all clauses that have become satisfied
#
# 4) Remove all variables that evaluate to 'FALSE' (i.e., all variables x
# that are set to FALSE and all variables not(x) where x is set to TRUE).
# If this results in an empty clause, then the input formula has no satisfying
# assignment and the function should return the Boolean formula [[1,-1]]
#
# The challenging part is implementing Rule 2, for your function must
# perform the data reductions exhaustively, that is, until they can no
# further be applied: After rules 2, 3 and 4 have been applied, there
# might be other clauses for which rule 2 now becomes applicable (you
# will have to be careful if a variable that now appears once has
# already been set earlier - if not, then Rule 2 may apply, otherwise
# it doesn't).
#
# If through the pre-processing steps you are able to determine that a
# SAT problem is satisfiable then return []. Likewise, if you
# determine that it is unsatisfiable then return [[1,-1]]. Otherwise,
# return the remaining clauses.

def sat_preprocessing(num_variables, clauses):
    # YOUR CODE HERE
    return [1,-1]

def test():
    assert [] == sat_preprocessing(1, [[1]])
    assert [[1,-1]] == sat_preprocessing(1, [[1], [-1]])

    assert [] == sat_preprocessing(4,[[4], 
                                      [-3, -1], 
                                      [3, -4, 2, 1], 
                                      [1, -3, 4],
                                      [-1, -3, -4, 2], 
                                      [4, 3, 1, 2], 
                                      [4, 3],
                                      [1, 3, -4], 
                                      [3, -4, 1], 
                                      [-1]])

    assert [[1,-1]] == sat_preprocessing(5,[[4, -2], 
                                            [-1, -2], 
                                            [1], 
                                            [-4],
                                            [5, 1, 4, -2, 3], 
                                            [-1, 2, 3, 5],
                                            [-3, -1], 
                                            [-4], 
                                            [4, -1, 2]])
    
    ans = [[5, 6, 2, 4], 
           [3, 5, 2, 4], 
           [-5, 2, 3], 
           [-3, 2, -5, 6, -4]]
    
    assert ans == sat_preprocessing(6, [[-5, 3, 2, 6, 1], 
                                        [5, 6, 2, 4],
                                        [3, 5, 2, -1, 4], 
                                        [1], 
                                        [2, 1, 4, 3, 6],
                                        [-1, -5, 2, 3], 
                                        [-3, 2, -5, 6, -4]])

test()
