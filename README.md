# 🐍 30 Days of Python Challenge

Bienvenue dans mon dépôt **30 Days of Python** — un projet personnel où je relève le défi d’apprendre, pratiquer et documenter mes progrès en **Python** pendant 30 jours. 🚀

---

## 🎯 Objectif

Ce challenge a pour but de renforcer mes compétences en programmation Python à travers des exercices quotidiens couvrant :

* Les bases du langage (variables, types, opérateurs, boucles, conditions)
* Les structures de données (listes, tuples, ensembles, dictionnaires)
* Les fonctions et modules
* Les notions avancées : fichiers, classes, exceptions, librairies, etc.
* Et surtout, la **pratique quotidienne** 💪

Chaque dossier (`Day_01`, `Day_02`, etc.) contient :

* Le code source (`.py`) des exercices du jour

---

## 📚 Progression actuelle

| Jour         | Thème                           | Statut   |
| ------------ | ------------------------------- | -------- |
| ✅ **Day 1**  | Introduction à Python           | Terminé  |
| ✅ **Day 2**  | Variables et types              | Terminé  |
| ✅ **Day 3**  | Opérateurs                      | Terminé  |
| ✅ **Day 4**  | Strings (chaînes de caractères) | Terminé  |
| ✅ **Day 5**  | Lists (Listes)                  | Terminé  |
| ✅ **Day 6**  | Tuples                          | Terminé  |
| ✅ **Day 7**  | Sets (Ensembles)                | Terminé  |
| 🔥 **Day 8** | Dictionaries (Dictionnaires)    | Terminé  |
| 🔜 **Day 9** | Conditionals (Conditions)       | En cours |

---

## 🧩 Exemple du jour 8 — Dictionaries (Dictionnaires)

Aujourd’hui, j’ai exploré les **dictionnaires**, une structure de données essentielle en Python pour stocker des informations sous forme de **paires clé–valeur**. 🔑

### 📘 Ce que j’ai appris :

* Créer un dictionnaire avec `{}` ou `dict()`
* Accéder aux valeurs via les clés (`student['skills']` ou `student.get('skills')`)
* Ajouter, modifier et supprimer des éléments
* Vérifier la présence d’une clé avec l’opérateur `in`
* Obtenir toutes les **clés**, **valeurs** ou **paires clé–valeur** avec `.keys()`, `.values()` et `.items()`
* Copier un dictionnaire sans affecter l’original avec `.copy()`
* Vider ou supprimer complètement un dictionnaire avec `.clear()` et `del`

### ⚙️ Les difficultés rencontrées :

Au début, j’ai confondu les méthodes `.values()` et l’accès direct à une clé.
Par exemple, `student.values('skills')` provoque une erreur car `.values()` ne prend aucun argument.
La bonne syntaxe est : `student['skills']` ✅

J’ai aussi retenu qu’on ne peut pas faire `student.append('Django')`, car `.append()` s’applique uniquement aux **listes**, pas aux **dictionnaires**.

### 🍎 Exemple concret :

J’ai créé deux dictionnaires :

* 🐶 **`dog`** → contenant le nom, la race et la couleur
* 👨‍🎓 **`student`** → contenant des informations personnelles (nom, âge, pays, compétences...)

Puis j’ai :

* Vérifié la longueur du dictionnaire
* Accédé et modifié la liste de compétences
* Ajouté de nouvelles compétences (`Django`)
* Listé les clés et valeurs
* Supprimé la clé `address`
* Supprimé entièrement le dictionnaire `dog`

### 💻 Extrait de code :

```python
student['skills'].append('Django')
del student['address']
print(student.keys())
```

---

## 🧩 Exemple du jour 7 — Sets (Ensembles)

Lors de cette journée, j’ai exploré les **sets**, des structures permettant de stocker des éléments **uniques** et **non ordonnés**. 🔥

### 📘 Ce que j’ai appris :

* Créer un **set** avec `{}` ou `set()`
* Ajouter ou supprimer des éléments (`add()`, `update()`, `remove()`, `discard()`)
* Réaliser des **opérations d’ensemble** : `union()`, `intersection()`, `difference()`, `symmetric_difference()`
* Vérifier les relations entre ensembles : `issubset()`, `issuperset()`, `isdisjoint()`
* Convertir une liste en set pour supprimer les doublons
* Compter les mots uniques dans une phrase grâce à `set()`

---

## 🧩 Exemple du jour 6 — Tuples

Les **tuples** sont des structures de données **immuables** — une fois créés, ils ne peuvent plus être modifiés. 🔒

### 📘 Ce que j’ai appris :

* Créer des tuples avec `()` ou `tuple()`
* Accéder aux éléments avec indexation positive/négative
* Extraire des sous-parties avec le slicing
* Convertir un tuple en liste pour le modifier
* Fusionner et supprimer des tuples
* Utiliser le **tuple unpacking**

---

## 🧩 Exemple du jour 5 — Lists

Les **listes** sont des structures de données **mutables** très utilisées en Python.

### 📘 Ce que j’ai appris :

* Créer et modifier des listes
* Ajouter, insérer et supprimer des éléments
* Trier et fusionner des listes
* Comprendre la mutabilité et la différence entre `sort()` et `sorted()`

---

## 🔗 Liens utiles

* 🐙 **Repo GitHub** : [https://github.com/ralphgabriel04/30DaysOfPython](https://github.com/ralphgabriel04/30DaysOfPython)
* 💼 **Mon LinkedIn** : [linkedin.com/in/ralph-christian-gabriel-45092021b](https://www.linkedin.com/in/ralph-christian-gabriel-45092021b/)

---

## 🧠 À propos

👨‍💻 **Auteur** : Ralph Christian Gabriel
🎓 Étudiant en **Génie Logiciel à l’ÉTS**
💬 Passionné par l’apprentissage continu, la pratique et le partage de connaissances.

---

## 🏁 Objectif final

À la fin des 30 jours, je vise à :

* Avoir une maîtrise solide des bases du langage Python
* Construire un petit **projet final** pour mettre en pratique les notions apprises
* Partager mes progrès et inspirer d’autres étudiants à suivre le même parcours

---

> *“La constance bat le talent quand le talent n’est pas constant.”* 💡
> — *30 Days of Python Challenge*