# assumes real entries for now

import numpy as np
import random

# generates a random orthogonal matrix 
def generate_random_orthogonal_matrix(m, temperature):
    gaussian = np.random.randn(m, m) * temperature
    q, r = np.linalg.qr(gaussian + np.eye(m))
    return q

def penalty(bases):
    score = 0
    for i in range(len(bases)):
        for j in range(i + 1, len(bases)):
            for k in range(len(bases[i])):
                dot = np.dot(bases[i][k], bases[j][k])
                score += dot * dot
    return score

def find_optimal_bases(n, m, p):
    bases = [np.eye(m) if i == 0 else generate_random_orthogonal_matrix(m, n) for i in range(n)]
    temperature = 1
    score = penalty(bases)
    while temperature >= 0.0001:
        # TODO may need to update multiple indices at once?
        index = random.randint(1, n - 1) # don't mess with basis 1
        matrix = generate_random_orthogonal_matrix(m, temperature) @ bases[index]
        update = [matrix if i == index else bases[i] for i in range(len(bases))]
        if penalty(update) < penalty(bases):
            bases = update
        else:
            temperature *= 0.999 # TODO mess with temperature update schemes
    print(1 - p * penalty(bases) / ((n * (n - 1) / 2) * m)) 
    print(bases) # TODO print in a more readable format