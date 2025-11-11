# 🐍 30 Days of Python Challenge

Bienvenue dans mon dépôt **30 Days of Python** — un projet personnel où je relève le défi d’apprendre, pratiquer et documenter mes progrès en **Python** pendant 30 jours. 🚀

---

## 🎯 Objectif

L’objectif de ce challenge est de **renforcer mes compétences en programmation Python** à travers des exercices quotidiens, du code pratique et des projets concrets.

Les thématiques abordées couvrent :

* Les **bases du langage** (variables, types, opérateurs, boucles, conditions)
* Les **structures de données** (listes, tuples, ensembles, dictionnaires)
* Les **fonctions et modules**
* Les **concepts avancés** : exceptions, fichiers, POO, décorateurs, etc.
* Et surtout, la **pratique quotidienne** 💪

Chaque dossier (`Day_01`, `Day_02`, etc.) contient :

* Le code source (`.py`) des exercices du jour
* Des notes d’apprentissage et des exemples d’application

---

## 📚 Progression actuelle

| Jour          | Thème                           | Statut  |
| ------------- | ------------------------------- | ------- |
| ✅ **Day 1**   | Introduction à Python           | Terminé |
| ✅ **Day 2**   | Variables et types de données   | Terminé |
| ✅ **Day 3**   | Opérateurs                      | Terminé |
| ✅ **Day 4**   | Strings (chaînes de caractères) | Terminé |
| ✅ **Day 5**   | Lists (listes)                  | Terminé |
| ✅ **Day 6**   | Tuples                          | Terminé |
| ✅ **Day 7**   | Sets (ensembles)                | Terminé |
| ✅ **Day 8**   | Dictionaries (dictionnaires)    | Terminé |
| ✅ **Day 9**   | Conditionals (conditions)       | Terminé |
| ✅ **Day 10**  | Loops (boucles)                 | Terminé |
| ✅ **Day 11**  | Functions (fonctions)           | Terminé |
| ✅ **Day 12**  | Modules                         | Terminé |
| ✅ **Day 13**  | List Comprehension              | Terminé |
| ✅ **Day 14**  | Higher Order Functions          | Terminé |
| 🔜 **Day 15** | Type Errors & Debugging         | À venir |

---

## 🧩 Aperçu des journées terminées

---

### 🗓️ **Day 9 – Conditionals (Conditions)**

**Ce que j’ai appris :**

* Utiliser les structures conditionnelles `if`, `elif`, `else`
* Gérer des conditions combinées avec `and`, `or`, `not`
* Comprendre l’importance de l’indentation et des blocs logiques
* Comparer plusieurs valeurs et gérer des cas multiples

**Exemple :**

```python
age = 18
if age >= 18:
    print("Adulte")
else:
    print("Mineur")
```

---

### 🔁 **Day 10 – Loops (Boucles)**

**Ce que j’ai appris :**

* Utiliser les boucles `for` et `while`
* Parcourir des listes, tuples et dictionnaires
* Utiliser `break`, `continue` et `else` dans les boucles
* Créer des boucles imbriquées et des compteurs

**Exemple :**

```python
for i in range(1, 6):
    print(f"Compteur : {i}")
```

---

### 🧮 **Day 11 – Functions (Fonctions)**

**Ce que j’ai appris :**

* Définir et appeler des fonctions avec `def`
* Passer des arguments et retourner des valeurs
* Gérer des arguments par défaut et des fonctions anonymes (`lambda`)
* Comprendre la portée des variables (locale / globale)

**Exemple :**

```python
def add(a, b):
    return a + b

print(add(3, 5))  # 8
```

---

### 📦 **Day 12 – Modules**

**Ce que j’ai appris :**

* Créer et importer des modules personnalisés
* Utiliser les **modules intégrés** : `math`, `os`, `random`, `statistics`, `sys`
* Comprendre la différence entre `import`, `from ... import ...`, et `as`
* Générer des identifiants, des couleurs et des nombres aléatoires

**Exemple :**

```python
from math import pi, sqrt
print(pi)       # 3.141592653589793
print(sqrt(16)) # 4.0
```

---

### ⚙️ **Day 13 – List Comprehension & Lambda**

**Ce que j’ai appris :**

* Créer des listes en une seule ligne avec des conditions
* Appliquer des transformations rapides sur des collections
* Créer des fonctions anonymes avec `lambda`
* Combiner `for`, `if` et expressions dans une seule syntaxe élégante

**Exemple :**

```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
double = lambda x: x * 2
print(double(5))  # 10
```

---

### 🧠 **Day 14 – Higher Order Functions, Closures & Decorators**

**Ce que j’ai appris :**

* Comprendre les **higher-order functions** (fonctions qui prennent ou retournent d’autres fonctions)
* Créer des **closures** pour garder en mémoire des variables locales
* Construire des **décorateurs** pour modifier le comportement d’une fonction
* Utiliser les fonctions intégrées : `map()`, `filter()`, `reduce()`

**Exemple :**

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda x, y: x + y, numbers)

print(squared, evens, total)  # [1, 4, 9, 16, 25] [2, 4] 15
```

---

## 🔗 Liens utiles

* 🐙 **Repo GitHub** : [github.com/ralphgabriel04/30DaysOfPython](https://github.com/ralphgabriel04/30DaysOfPython)
* 💼 **LinkedIn** : [Ralph Christian Gabriel](https://www.linkedin.com/in/ralph-christian-gabriel-45092021b/)

---

## 👨‍💻 À propos

**Auteur :** Ralph Christian Gabriel
🎓 Étudiant en **Génie Logiciel à l’ÉTS**
💬 Passionné par le **développement logiciel**, l’**intelligence artificielle**, et la **création de projets éducatifs**.

---

## 🏁 Objectif final

À la fin de ces **30 jours**, je vise à :

* Maîtriser les **fondamentaux de Python**
* Développer un **projet final complet** (backend + logique métier)
* Partager mes apprentissages pour inspirer d’autres étudiants

---

> 🧩 *"La constance bat le talent quand le talent n’est pas constant."*
> — *30 Days of Python Challenge*

---
