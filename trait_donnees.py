import pandas as pd

df = pd.read_csv(r"C:\ROOT\M1_IA_Sorbonne\AI2D Projet\PAI2D\tdf_rankings\valeurs.csv")

# print(df.head())
# print(df.info())
# print(df["Rider"][0])
# print(df["poids"][0])

c = {}
c.update({df["Rider"][i] : df["poids"][i] for i in range(len(df))})
cle = list(c.keys())
valeur = list(c.values())

# print(c["Bauhaus Phil"])


# -----------------------------------------------------------------------------------

points = {}
# points.update({df["Rider"][i] : 0 for i in range(len(df))})

points_top_20 = [30, 20, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

e = 0
for k in range(3):
    for j in range(1, 9):
        if k == 2 and j == 2:
            break
        e += 1  # étape courante = 1..21
        df_stage = pd.read_csv(r"C:\ROOT\M1_IA_Sorbonne\AI2D Projet\PAI2D\tdf_rankings\stage_" + str(k) + str(j) + "_2025.csv")
        for i in range(min(len(df_stage), 20)):
            coureur = df_stage.loc[i, "Rider"]
            points[(coureur, e)] = points.get((coureur, e), 0) + points_top_20[i]
            # points.get((coureur, e), 0), récupère la valeur actuelle, retourne 0 si la clé n’existe pas

# print(points)
# print(coureur)

# -----------------------------------------------------------------------------------

df_bonus = pd.read_csv(r"C:\ROOT\M1_IA_Sorbonne\AI2D Projet\PAI2D\tdf_rankings\maillots.csv")
bonus_jaune = 8
bonus_vert = 5
bonus_pois = 5
bonus_blanc = 5
bonus_combatif1 = 5
bonus_combatif2 = 5

for i in range(len(df_bonus)): 
    e = i + 1

    for col, b in [("Jaune", bonus_jaune),
                   ("Vert", bonus_vert),
                   ("Pois", bonus_pois),
                   ("Blanc", bonus_blanc),
                   ("Combatif1", bonus_combatif1)]:
        coureur = df_bonus.loc[i, col]
        if pd.notna(coureur) and coureur != "":
            points[(coureur, e)] = points.get((coureur, e), 0) + b
    coureur2 = df_bonus.loc[i, "Combatif2"]
    if pd.notna(coureur2) and coureur2 != "":
        points[(coureur2, e)] = points.get((coureur2, e), 0) + bonus_combatif2

"""
for i in range(23) : # i+1 jouera le rôle de e
    # Jaune,Vert,Pois,Blanc,Combatif1,Combatif2
    points[(df_bonus["Jaune"][i],i+1)] += bonus_jaune
    points[(df_bonus["Vert"][i],i+1)] += bonus_vert
    points[(df_bonus["Pois"][i],i+1)] += bonus_pois
    points[(df_bonus["Blanc"][i],i+1)] += bonus_blanc
    points[(df_bonus["Combatif1"][i],i+1)] += bonus_combatif1
    if df_bonus["Combatif2"][i] != "" and pd.notna(df_bonus["Combatif2"][i]):
        points[(df_bonus["Combatif2"][i],i+1)] += bonus_combatif2
"""

# -----------------------------------------------------------------------------------

df_final = pd.read_csv(r"C:\ROOT\M1_IA_Sorbonne\AI2D Projet\PAI2D\tdf_rankings\final.csv")

for i in range(min(len(df_final), 185)):
    coureur = df_final.loc[i, "Rider"]
    if pd.notna(coureur) and coureur != "":
        # points[(coureur, e)] = points.get((coureur, e), 0) + b