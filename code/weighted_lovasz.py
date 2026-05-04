import cvxpy as cp

def weighted_lovasz_number(adj_matrix, weights):
    """
    Compute the weighted Lovász number of a graph.

    Parameters:
        adj_matrix (np.ndarray): n x n adjacency matrix (0/1, symmetric, no self-loops)
        weights (np.ndarray): length-n array of nonnegative vertex weights

    Returns:
        float: weighted Lovász number
    """
    # formulas due to https://i.cs.hku.hk/~hubert/isit_2009.pdf
    # code written with the assistance of ChatGPT and VSCode copilot
    n = len(adj_matrix)
    
    # Variable: symmetric n x n matrix
    X = cp.Variable((n, n), symmetric=True)

    # Objective: maximize trace of product of outer product of square roots of weights with X
    sqrt_w = cp.sqrt(weights)
    W = cp.outer(sqrt_w, sqrt_w)
    objective = cp.Maximize(cp.trace(cp.multiply(W, X)))
    
    constraints = []
    
    # Positive semidefiniteness constraint
    constraints.append(X >> 0)
    
    # Trace normalization constraint
    constraints.append(cp.trace(X) == 1)
    
    # Edge constraints: X_ij = 0 if (i,j) is an edge
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i][j] == 1:
                constraints.append(X[i, j] == 0)
                constraints.append(X[j, i] == 0)
    
    # Solve SDP
    prob = cp.Problem(objective, constraints)
    prob.solve(solver=cp.SCS)  # You can also try MOSEK if available
    
    return prob.value