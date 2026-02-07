import pulp
import pandas as pd


def period(e):
    if e <= 10:
        return 0
    elif e <= 15:
        return 10
    else:
        return 15


# Le solveur CBC
print(pulp.listSolvers(onlyAvailable=True))

# Le prob est à Maximiser
prob = pulp.LpProblem("Z", pulp.LpMaximize)

# Les constantes du problèmes
# Le Budget initial
B = 140
# Les périodes
T = [0, 10, 15] # 3 périodes (0 est pour l'équipe initiale)
# Les événements
E = list(range(1, 22)) # 21 événements
# Les coureurs
P = ["p1", "p2", "p3"] # 184 coureurs
# Les prix de chaque coureurs
c = {
    "p1" : 100
}

## Variables de décision
# le budget restant r à la période t
r = pulp.LpVariable.dicts("r", T, lowBound=0) # >=0
# le choix d'un coureur p à la période t
x = pulp.LpVariable.dicts("x", (P, T), cat=pulp.LpBinary)
# le coureur p entre en jeu à la période t (Transfert) # à implémenter plus tard !
z = pulp.LpVariable.dicts("z", (P, T), cat=pulp.LpBinary)
# le coureur p a marqué des points à l'événement e
y = pulp.LpVariable.dicts("y", (P, E), cat=pulp.LpBinary)

# Le prob à maximiser
# prob += pulp.lpSum(v[p][e] * y[p][e] for p in P for e in E) # à implémenter plus tard !
"""
t_fin = 15  
prob += (
    pulp.lpSum(points.get((p, e), 0) * x[p][period(e)] for p in P for e in E)
    + pulp.lpSum(points_final.get(p, 0) * x[p][t_fin] for p in P)
)
"""


# Listes de contraintes
# Budget Dyn # Les coûts ne changent pas ?
for i in range(1, len(T)):
    t_1 = T[i-1]
    t = T[i]
    prob += (pulp.lpSum(c[p] * (x[p][t] - x[p][t_1]) for p in P) == r[t_1] - r[t]), f"Budget_de_{t_1}_à_{t}"

# Attributions des points
for e in E:
    t = period(e)
    for p in P:
        prob += y[p][e] <= x[p][t], f"{p}_A_marque_à_{e}"

# Budget Initial
prob += pulp.lpSum(c[p] * x[p][0] for p in P) + r[0] == B, "Budget_Initial"

# Nombre de coureurs à chaque période
for t in T:
    prob += pulp.lpSum(x[p][t] for p in P) == 14



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
