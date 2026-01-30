import pulp
import pandas as pd

# Le solveur CBC
print(pulp.listSolvers(onlyAvailable=True))

# Les périodes
T = [1, 2, 3] # 21 périodes 

# Les coureurs
P = ["p1", "p2", "p3"] # 184 coureurs

# Variables de décision
v = pulp.LpVariable.dicts("v", (P, T), cat=pulp.LpBinary)    # 0/1
r = pulp.LpVariable.dicts("r", T, lowBound=0) # >=0


pulp.lpSum(v[p][t] for p in P for t in T)


""" Somme ≤ variable doublement indexée
w = pulp.LpVariable.dicts("w", (G, T), lowBound=0) 
for g in G: 
    for t in T: 
        prob += pulp.lpSum(v[p][t] for p in P) <= w[g][t]

for g in G:
    for t in T:
        s = 0
        for p in P:
            s += v[p][t]
        prob += s <= w[g][t]
"""
