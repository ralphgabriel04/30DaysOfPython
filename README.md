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
| ✅ **Day 15**  | Type Errors & Debugging         | Terminé |
| ✅ **Day 16**  | Date & Time                     | Terminé |
| ✅ **Day 17**  | Exception Handling              | Terminé |
| 🔜 **Day 18** | Regular Expressions             | À venir |

---

## 🧩 Aperçu des journées terminées

---

### 🧠 **Day 15 – Type Errors & Debugging**

**Ce que j’ai appris :**

* Identifier et corriger les erreurs courantes en Python
* Lire et comprendre les messages d’erreur du terminal
* Distinguer les différents types d’erreurs :

  * `SyntaxError`, `NameError`, `IndexError`, `ModuleNotFoundError`
  * `AttributeError`, `KeyError`, `TypeError`, `ImportError`, `ValueError`, `ZeroDivisionError`

**Exemple :**

```python
# Exemple : TypeError
print(4 + '3')      # ❌ Erreur : int + str impossible
print(4 + int('3')) # ✅ Solution : conversion en entier
```

🧩 **En résumé :**

> Savoir déboguer efficacement, c’est comprendre que **chaque erreur est un indice**.
> Le message d’erreur est ton meilleur allié, pas ton ennemi !

---

### ⏰ **Day 16 – Python Date & Time**

**Ce que j’ai appris :**

* Manipuler les dates et heures avec `datetime`
* Formater des dates avec `strftime()` et `strptime()`
* Calculer des différences entre deux dates avec `timedelta`
* Travailler avec `date`, `time`, `datetime`

**Exemple :**

```python
from datetime import datetime, date

now = datetime.now()
print(now.strftime("%m/%d/%Y, %H:%M:%S"))

today = date.today()
new_year = date(today.year + 1, 1, 1)
print("Time left until New Year:", new_year - today)
```

💡 *Le temps est une donnée : apprendre à le manipuler, c’est maîtriser le flux logique d’une application.*

---

### ⚙️ **Day 17 – Exception Handling, Packing & Unpacking**

**Ce que j’ai appris :**

* Gérer les erreurs avec `try`, `except`, `else`, `finally`
* Identifier les erreurs spécifiques (`TypeError`, `ValueError`, `ZeroDivisionError`)
* Simplifier le code avec `Exception as e` pour capturer le message d’erreur
* Comprendre les concepts de **packing** (`*args`, `**kwargs`) et **unpacking**
* Utiliser `enumerate()` pour obtenir l’index et `zip()` pour combiner plusieurs listes

---

**Exemple – Gestion d’erreur simple :**

```python
try:
    name = input("Enter your name: ")
    year = int(input("Enter your birth year: "))
    print(f"Hello {name}, you are {2025 - year} years old.")
except ValueError:
    print("Veuillez entrer une année valide.")
finally:
    print("Execution terminée.")
```

---

**Exemple – Unpacking :**

```python
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

*nordic_countries, ic, es, ru = names

print("Nordic Countries:", nordic_countries)
print("Iceland:", ic)
print("Estonia:", es)
print("Russia:", ru)
```

🖥️ **Résultat :**

```
Nordic Countries: ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
Iceland: Iceland
Estonia: Estonia
Russia: Russia
```

---

💡 **En résumé :**

> Les exceptions rendent ton code plus **fiable**,
> le dépaquetage le rend plus **lisible**,
> et leur combinaison te rend **Pythonic** 🐍✨

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