from weighted_lovasz import weighted_lovasz_number
import itertools
# import cvxopt.solvers


class GameGraph:

    def wins(self, v):
        (x, y, a, b) = v
        return (x == y) == (a == b)

    def is_edge(self, v, w):
        (xv, yv, av, bv) = v
        (xw, yw, aw, bw) = w
        return ((xv == xw) and (av != aw)) or ((yv == yw) and (bv != bw))
    
    # refactor of above commented code
    def __init__(self, n, k):
        self.n = n
        self.k = k
        strategies = [(x, y, a, b) for x in range(0, n) for y in range(0, n) for a in range(0, k) for b in range(0, k)]
        self.vertices = list(filter(self.wins, strategies))
        self.edges = []
        for v in self.vertices:
            row = []
            for w in self.vertices:
                row.append(1 if self.is_edge(v, w) else 0)
            self.edges.append(row)

    def lovasz_upper_bound(self, p):
        weights = [p / self.n if v[0] == v[1] else (1 - p) / (self.n * self.n - self.n) for v in self.vertices]
        return weighted_lovasz_number(self.edges, weights)

p = 0.5
for n in itertools.count(3):
    for k in range(2, 3):
        G = GameGraph(n, k)
        print(f"n={n}, k={k}")
        theta = G.lovasz_upper_bound(p)
        print(f"bound={theta}")