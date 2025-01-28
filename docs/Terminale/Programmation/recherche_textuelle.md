# Recherche textuelle

## Introduction
Les algorithmes qui permettent de trouver une sous-chaîne de caractères dans une chaîne de caractères plus grande sont des grands classiques de l’algorithmique.

Un des secteurs qui utilise le plus cette recherche textuelle est le domaine de la bioinformatique notamment dans l’analyse des informations génétiques. Cette information génétique présente dans nos cellules est portée par les molécules d’ADN et permet la fabrication des protéines. Ces molécules d’ADN sont, entre autres, composées de bases azotées ayant pour noms : Adénine (représenté par un A), Thymine (représenté par un T), Guanine (représenté par un G) et Cytosine (représenté par un C).

<figure markdown>
![adn](img_recherche/Capture%20d’écran%202020-12-06%20à%2022.20.09.png)
</figure>

Il est souvent nécessaire de détecter la présence de certains enchaînements de bases azotées (dans la plupart des cas un triplet de bases azotées code pour 1 acide aminé et la combinaison d’acides aminés forme une protéine).

## Comment fonctionne ces algorithmes ?

L’objectif, ici, est de construire des algorithmes de recherche textuelle, d’en comprendre les principes et de les comparer.

Nous étudierons ici unalgorithme simplifié de Boyer-Moore.

Tout comme la plupart des applications, Python possède sa propre méthode de recherche, ce script affiche la présence ou non d’une occurrence. (mot) dans un texte (phrase).

``` py linenums="1"
phrase="Ceci n'est que la phrase qui nous sert d'exemple"
mot1="qui"
mot2="quiche"
print(mot1 in phrase)
print(mot2 in phrase)
```

Remarque : nous disposons également de la méthode `find()`

Exemple :
``` py linenums="1"
txt = "Bonjour les TNSI"

x = txt.find("TNSI")

print(x) # affiche 12
```

Il y a encore la méthode `index`

``` py linenums="1"
string = "Bonjour les TNSI"
print(string.index("TNSI"))
``` 

Danx ce cours, nous allons étudier comment fonctionnent ces fonctions/méthodes à l'aide d'une approche naïve et d'une approche beaucoup plus efficace.

## Une approche "naïve"

Pour savoir si un mot est dans une phrase, la méthode qui nous vient à l’esprit est la suivante :

    On parcourt le texte d’indice en indice depuis le début du texte en vérifiant à chaque pas si les lettres du mot coïncident comme illustré dans l'[animation](https://boyer-moore.codekodo.net/recherche_naive.php) suivante.



