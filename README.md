# 🐍 30 Days of Python Challenge

Bienvenue dans mon dépôt **30 Days of Python** — un projet personnel où je relève le défi d’apprendre, pratiquer et documenter mes progrès en **Python** pendant 30 jours. 🚀

---

## 🎯 Objectif

Ce challenge a pour but de renforcer mes compétences en programmation Python à travers des exercices quotidiens couvrant :

* Les bases du langage (variables, types, opérateurs, boucles, conditions)
* Les structures de données (listes, tuples, sets, dictionnaires)
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
| 🔥 **Day 7** | Sets (Ensembles)                | Terminé  |
| 🔜 **Day 8** | Dictionaries                    | En cours |

---

## 🧩 Exemple du jour 7 — Sets (Ensembles)

Aujourd’hui, j’ai exploré les **sets** en Python, des structures de données puissantes permettant de stocker des éléments **uniques** et **non ordonnés**. 🔥

### 📘 Ce que j’ai appris :

* Créer un **set** avec `{}` ou `set()`
* Ajouter des éléments avec `add()` et `update()`
* Supprimer des éléments avec `remove()` et `discard()` (et comprendre leur différence ⚠️)
* Utiliser les principales **opérations d’ensemble** :

  * `union()` → fusionner deux ensembles
  * `intersection()` → trouver les éléments communs
  * `difference()` → trouver les éléments exclusifs
  * `symmetric_difference()` → éléments présents dans un seul des deux ensembles
* Vérifier les relations entre ensembles :

  * `issubset()` / `issuperset()` / `isdisjoint()`
* Convertir une **liste en set** pour supprimer les doublons
* Compter le **nombre de mots uniques** dans une phrase à l’aide de `split()` et `set()`

### ⚙️ Les difficultés rencontrées :

J’ai découvert que `remove()` lève une erreur si l’élément n’existe pas dans l’ensemble, tandis que `discard()` ne le fait pas.
Ce détail m’a aidé à mieux comprendre la **gestion des erreurs** en Python. 🧠

### 🍎 Exemple concret :

J’ai manipulé des ensembles d’entreprises (`it_companies`), de nombres (`A` et `B`) et de valeurs d’âges.
J’ai pu observer comment les sets éliminent automatiquement les doublons et facilitent les comparaisons mathématiques.

Enfin, j’ai analysé la phrase :

> “I am a teacher and I love to inspire and teach people”
> et identifié **le nombre de mots uniques** grâce à la puissance des ensembles. 💬

---

## 🧩 Exemple du jour 6 — Tuples

Lors de cette journée, j’ai découvert les **tuples**, une structure de données immuable en Python. Contrairement aux listes, les tuples ne peuvent pas être modifiés une fois créés. 🔒

### 📘 Ce que j’ai appris :

* Créer des tuples avec `()` et `tuple()`
* Comprendre la différence entre **listes** et **tuples**
* Accéder aux éléments par **indexation positive et négative**
* Utiliser le **slicing** pour extraire une portion d’un tuple
* Convertir un tuple en **liste** pour pouvoir le modifier, puis le reconvertir
* Vérifier la présence d’un élément avec `in`
* Fusionner plusieurs tuples avec l’opérateur `+`
* Supprimer complètement un tuple avec `del`
* Utiliser le **tuple unpacking** pour assigner plusieurs variables d’un seul coup

### ⚙️ Les difficultés rencontrées :

J’ai appris que les tuples sont **immutables** — impossible donc de faire `my_tuple[0] = "new_value"`.
La solution : convertir le tuple en liste, modifier la valeur, puis reconvertir en tuple. ✅

### 🍎 Exemple concret :

J’ai créé plusieurs tuples représentant mes **frères**, **sœurs** et **parents**, puis je les ai fusionnés pour former un tuple `family_members`.
J’ai également combiné des tuples de **fruits**, **légumes** et **produits animaux** pour former `food_stuff_tp`, puis j’ai extrait les premiers et derniers éléments, et vérifié si certains pays appartiennent aux **pays nordiques** 🇩🇰🇸🇪.

---

## 🧩 Exemple du jour 5 — Lists

Lors de cette journée, j’ai exploré en profondeur les **listes Python**, une des structures de données les plus utilisées et puissantes du langage.

### 📘 Ce que j’ai appris :

* Créer et manipuler des listes (`[]`, `list()`)
* Accéder aux éléments (indexation positive et négative)
* Modifier, insérer, ajouter et supprimer des éléments
* Trier, inverser, fusionner et copier des listes
* Utiliser `sort()` et `sorted()` et comprendre la différence entre eux
* Découvrir le concept de **mutabilité** et les effets de référence
* Utiliser la **division entière (`//`)** pour trouver facilement le **milieu** d’une liste

### ⚙️ Les difficultés rencontrées :

Durant mes exercices, j’ai fait face à plusieurs erreurs qui m’ont aidé à mieux comprendre Python :

* ❌ **`TypeError: 'list' object is not callable`** → j’utilisais des `()` au lieu de `[]` pour accéder aux éléments.
* ❌ **`AttributeError: 'list' object has no attribute 'min'`** → j’ai appris qu’il faut utiliser les fonctions **intégrées** `min()` et `max()`.
* ❌ Un `print(ages.sort())` qui retournait `None` → car `.sort()` trie la liste en place et **ne retourne rien**.

Ces erreurs m’ont forcé à mieux comprendre la **logique interne des méthodes de listes** et à faire plus attention aux détails syntaxiques.

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

* Avoir une maîtrise solide des bases et outils du langage Python
* Construire un petit **projet final** pour mettre tout en pratique
* Partager mes progrès et inspirer d’autres étudiants à suivre le même parcours

---

> *“La constance bat le talent quand le talent n’est pas constant.”* 💡
> — 30 Days of Python Challenge

