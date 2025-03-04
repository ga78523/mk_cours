# Diviser pour régner

## Principe

Le diviser pour régner est une méthode algorithmique basée sur le principe suivant. On prend un problème (généralement complexe à résoudre), on divise ce problème en une multitude de petits problèmes, l’idée étant que les "petits problèmes" seront plus simples à résoudre que le problème original. Une fois les petits problèmes résolus, on recombine les "petits problèmes résolus" afin d’obtenir la solution du problème de départ.

Le paradigme "diviser pour régner" repose donc sur 3 étapes :

* DIVISER : le problème d’origine est divisé en un certain nombre de sous-problèmes
* RÉGNER : on résout les sous-problèmes (les sous-problèmes sont plus faciles à résoudre que le problème d’origine)
* COMBINER : les solutions des sous-problèmes sont combinées afin d’obtenir la solution du problème d’origine.

Les algorithmes basés sur le paradigme "diviser pour régner" sont très souvent des algorithmes récursifs.

## Tris fusion

### Présentation

Le tri fusion est un tri récursif basé sur le principe "diviser pour régner". Cet algorithme repose donc sur une fonction auxiliaire, la fonction de fusion, qui prendra en argument deux listes triées et renverra la liste fusionnée.

Voici le principe de la fonction auxiliaire de fusion ordonnée de deux listes `L1` et `L2` de longueurs respectives `k` et `l` dans une liste `M`.

* On initialise `i` et `j` à 0. On initialise `M` à `[]`.
* Tant que `i < k` et `j < l`, on compare `L1[i]` à `L2[j]`.
  
  * Si `L1[i] < L2[j]` alors :
  
    * On ajoute L1[i] à la fin de M.
    * On incrémente i
  
  * Sinon :

    * On ajoute L2[j] à la fin de M ;
    * On incrémente j

* Une fois la liste M de la façon suivante :
  
  * Si i = k et j < l, on ajoute les éléments L2[j], ....., L2[l − 1] dans cet ordre à la fin de la liste M.
  * Si i < k et j = l, on ajoute les éléments L1[i], ......, L1[k − 1] dans cet ordre à la fin de la liste M.
  
```example "Exercice n°1 :"
    Suivons l’algorithme précédent pour réaliser à la main la fusion ordonnée des listes `L1 = [2, 5, 12]` et `L2 = [1, 6, 11, 15]` dans une liste `M`. Recopiez et complétez le tableau suivant :

    | i   | j   | M   | L1[i] | L2[j] |
    |:---:|:---:|:---:|:-----:|:-----:|
    |     |     |     |       |       |
    |     |     |     |       |       |
    |     |     |     |       |       |
    |     |     |     |       |       |
    |     |     |     |       |       |


** Exemple :**
Voici dans la figure ci-dessou une représentation de l’algorithme de tri fusion appliqué à la liste `A = [23, 12, 4, 56, 35, 32,42, 57, 3]`. Étudiez attentivement le schéma ci-dessous afin de mieux comprendre le principe du tri-fusion (identifiez bien les phases "DIVISER" et "COMBINER").

### Implémentation en Python

On définit d’abord une fonction permettant de fusionner deux listes triées au préalable en une seule liste triée.

!!! example "Exercice 2 :"

    Écrire la fonction fusion. On utilisera le découpage (ou slicing) pour la deuxième partie de l’algorithme.

    ``` py linenums="1"
        def triFusion(L):
        """tri fusion d'une liste en récursif"""
        if len(L)<2:
            return L
        return fusion(triFusion(L[:len(L)//2]),triFusion(L[len(L)//2:]))
    ```

Cette fonction renvoie une copie triée de la liste passée en argument, sans la modifier.

!!! example "Exercice 3 :"
    Tester cette fonction avec la liste `L=[23,12,4,56,35,57,3,11,6]`

### Complexité

Nous avons vu que le tri par insertion et tri par sélection ont tous les deux une complexité $O(n^2)$. Qu’en est-il pour le tri-fusion ?

Le calcul rigoureux de la complexité de cet algorithme sort du cadre de ce cours.
Mais, la première phase (DIVISER) consiste à "couper" les tableaux en deux plusieurs fois de suite,la complexité de cette phase est en logarithme base 2. Si il y a n éléments dans le tableau, la complexité est donc en O(log2(n)).

La deuxième phase consiste à faire des comparaisons entre les premiers éléments de chaque tableau à fusionner, on peut donc supposer que pour un tableau de n éléments, on aura n comparaisons.

En combinant ces 2 constations on peut donc dire que la complexité du tri-fusion est en $O(n.log_2(n))$ (encore une fois la "démonstration" proposée ici n’a rien de rigoureux).

La comparaison des courbes de la fonction $n^2$ (en rouge) et n.log2(n) (en bleu).