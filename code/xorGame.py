import numpy as np
from toqito.nonlocal_games.xor_game import XORGame
# Important Note - This code was written with substantial assistance from AI tools to understand the interface with Toqito
# And to speed up the process of experimentation
for n in range(3, 17):
    # Probability matrix
    prob_mat = np.zeros((n, n))

    diag_prob = 0.5 / n
    off_diag_prob = 0.5 / (n * (n - 1))

    for i in range(n):
        for j in range(n):
            if i == j:
                prob_mat[i, j] = diag_prob
            else:
                prob_mat[i, j] = off_diag_prob

    # XOR predicate matrix
    # 0 iff inputs are equal, 1 otherwise
    pred_mat = np.ones((n, n))
    np.fill_diagonal(pred_mat, 0)

    game = XORGame(prob_mat, pred_mat)

    classical = game.classical_value()
    quantum = game.quantum_value()

    print(f"n = {n}")
    print(f"  classical value = {classical:.6f}")
    print(f"  quantum value   = {quantum:.6f}")

