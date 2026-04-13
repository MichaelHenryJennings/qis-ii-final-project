from lovasz import lovasz_theta

def wins(v):
    (x, y, a, b) = v
    print(v)
    print((x == y) == (a == b))
    return (x == y) == (a == b)

def is_edge(v, w):
    (xv, yv, av, bv) = v
    (xw, yw, aw, bw) = w
    return ((xv == xw) and (av != aw)) or ((yv == yw) and (bv != bw))

def create_graph(n, k):
    strategies = [(x, y, a, b) for x in range(0, n) for y in range(0, n) for a in range(0, k) for b in range(0, k)]
    vertices = filter(wins, strategies)
    print(list(vertices))
    edges = []
    for v in vertices:
        row = []
        for w in vertices:
            edges.append(1 if is_edge(v, w) else 0)
        edges.append(row)