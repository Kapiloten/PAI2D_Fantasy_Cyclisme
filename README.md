# Fantasy Cycling Optimizer

Application d'aide à la décision pour optimiser une équipe de fantasy cyclisme avec Python, programmation linéaire entière, Streamlit et analyse de Pareto.

Ce projet optimise la sélection d'une équipe de fantasy cyclisme sous contraintes réalistes : budget limité, taille d'équipe imposée, abandons de coureurs, périodes de transferts et surcoût lors des achats. Il a été développé dans le cadre du Master AI2D à Sorbonne Université.

## Présentation

Les jeux de fantasy cyclisme consistent à composer une équipe de coureurs capable de marquer un maximum de points tout en respectant un budget. Le problème devient plus complexe lorsque certains coureurs abandonnent, que les transferts ne sont autorisés qu'à des périodes précises, et que les nouveaux achats coûtent plus cher pendant ces fenêtres.

Cette application modélise ce problème comme une tâche d'optimisation et propose une interface interactive pour explorer les meilleures compositions d'équipe, les transferts, les analyses de sensibilité et les simulations de scénarios.

## Fonctionnalités

- Optimisation de la sélection d'équipe sous contraintes de budget et de taille.
- Gestion de plusieurs périodes de course.
- Prise en compte des transferts entre les périodes.
- Modélisation d'un surcoût lors de l'achat d'un coureur en transfert.
- Gestion des abandons de coureurs.
- Résolution du problème avec PuLP et le solveur CBC.
- Comparaison entre une stratégie avec transferts et une stratégie sans transfert.
- Analyse de sensibilité pour comprendre pourquoi un coureur est sélectionné ou exclu.
- Simulation de scénarios en perturbant les points, les coûts et la taille d'équipe.
- Visualisation des couches de Pareto et analyses post-optimales.
- Export des tableaux de résultats depuis l'interface Streamlit.

## Stack technique

- Python
- Streamlit
- PuLP / CBC
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Altair

## Structure du projet

```text
.
|-- app_pulp.py              # Application Streamlit principale et modèle PuLP
|-- trait_donnees.py         # Préparation des données et calcul des points fantasy
|-- analyse_budget.py        # Outils d'analyse du budget et des scores
|-- Affichage_Pareto.py      # Expérimentations de visualisation Pareto
|-- tdf_rankings/            # Fichiers CSV d'entrée : étapes, maillots, classement final
|-- Analyse_Pareto/          # Scripts d'exploration Pareto et données enrichies
|-- Graphe_profit_sur_cout/  # Graphiques générés coût / profit
|-- doc/                     # Cahier des charges et contraintes mathématiques
|-- pyproject.toml           # Dépendances du projet
`-- uv.lock                  # Versions verrouillées des dépendances
```

## Installation

### Avec uv

```bash
uv sync
```

Puis lancer l'application :

```bash
uv run streamlit run app_pulp.py
```

### Avec pip

```bash
python -m venv .venv
source .venv/bin/activate
pip install pandas pulp streamlit "altair<5" matplotlib seaborn
streamlit run app_pulp.py
```

Sous Windows PowerShell, activer l'environnement virtuel avec :

```powershell
.\.venv\Scripts\Activate.ps1
```

## Utilisation

1. Lancer l'application Streamlit :

   ```bash
   streamlit run app_pulp.py
   ```

2. Régler les paramètres principaux dans la barre latérale :

   - budget initial
   - taille de l'équipe
   - nombre de scénarios de simulation
   - incertitude sur les points, les coûts et la taille d'équipe

3. Lancer une analyse :

   - optimisation classique avec transferts
   - optimisation sans transfert
   - simulation de scénarios aléatoires

4. Explorer les onglets de résultats :

   - équipes sélectionnées par période
   - transferts entre périodes
   - points et scores
   - histogrammes et analyse de Pareto
   - analyse de sensibilité des points
   - tables exportables

## Modèle d'optimisation

Le problème est formulé comme un programme linéaire en nombres entiers.

Le modèle décide si chaque coureur est sélectionné à chaque période. L'objectif est de maximiser le nombre total de points fantasy tout en respectant plusieurs contraintes :

- une équipe valide à chaque période
- un nombre fixe de coureurs sélectionnés
- une contrainte de budget initial
- une mise à jour du budget après les ventes et les achats
- l'impossibilité de sélectionner un coureur indisponible après abandon
- la cohérence entre sélection, achat et vente de coureurs

Les principales variables de décision sont :

- `x[p][t]` : le coureur `p` est sélectionné à la période `t`
- `achat[p][t]` : le coureur `p` est acheté à la période `t`
- `vente[p][t]` : le coureur `p` est vendu à la période `t`
- `budget[t]` : budget restant à la période `t`

## Données

Le projet utilise des données du Tour de France stockées dans le dossier `tdf_rankings/`.

Le calcul des scores combine :

- les classements d'étapes
- les bonus de maillots
- les bonus de combativité
- les bonus du classement final
- les valeurs des coureurs

La préparation des données et le dictionnaire de points sont centralisés dans `trait_donnees.py`.

## Contexte académique

Ce projet a été développé dans le cadre du Master AI2D à Sorbonne Université. Il combine optimisation, analyse de données et interface d'aide à la décision autour d'un cas d'usage concret en sport analytics.

## Description courte

Application d'aide à la décision pour optimiser une équipe de fantasy cyclisme sous contraintes de budget, transferts et abandons, avec Python, PuLP, Streamlit et analyse de Pareto.
