# Results

## Problem Statement

Alice and Bob are given inputs from a set X with |X| = n for some natural number n.
After receiving their input, they cannot communicate with the other player.
They must output values from a set Y with |Y| = k for some natural number k.
They win if their inputs match and their outputs match, or if neither match.
They are given equal inputs with some probability p

## Relation to Other Problems

### Graph Homomorphism

This problem is equivalent to the game of convincing a 

## Classical strategies

- strategies with randomness (even shared randomness) are at best as good as the best outcome
- alice's and bob's optimal strategies are thus both functions X -> Y
- the value of a strategy (a, b) : (X -> Y)^2 is p * |{x : X | a(x) = b(x)}|/n + (1 - p) * |{(x, y) : X^2 | a(x) != b(x) /\ x != y}|/n(n - 1)
- for the k = 2 case, the strategies are just defined by the subsets of X where we output 0.
- we win on (x, x) if x is in A /\ B or A' /\ B'
- we win on (x, y) if x is in A and y is not in B or if x is not in A and y is in B
- value is then (p/n)(|A /\ B| + |A' /\ B'|) + ((1 - p)/n(n-1))(|A|(n - |B|) + |B|(n - |A|) - n + |A /\ B| + |A' /\ B'|)

let |{x : X | a(x) = b(x)}| = c: then |{(x, y) : X^2 | a(x) != b(x) /\ x != y}| = 
- then 

(p/n)d + ((1 - p)/n(n-1))(c(n - d) + d(n - c) - n + d)
removing extraneities, p(n-1)d + (1 - p)(c(n - d) + d(n - c) + d)
simplifying, p(n-1)d + (1 - p)((c + d)n - 2cd + d)
grouping terms, (1 - p)nc - 2(1 - p)cd + (p(n - 1) + (1 - p)(n + 1))d
simplifying, 


