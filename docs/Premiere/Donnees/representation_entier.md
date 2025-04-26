# Représentation des entiers

## Représentation binaire de l'information

### Les bases de calcul

!!! example "Exercice 1"
    Reproduire et compléter le tableau ci-dessous :

    <figure markdown>

    | Base | Système | Utilisation|
    |:----:|:-------:|:----------:|
    |2     |         |            |
    |8     |         |            |
    |10    |         |            |
    |12    |         |            | 
    |16    |         |            |
    |20    |         |            |
    |60    |         |            |  
    </figure>

### Pourquoi le bit est-il l’unité de base du codage des informations dans les systèmes informatiques ?

Il est simple de représenter deux états physiques grâce à :

* La lumière (exemple : la fibre) ;
* La tension (exemple : le processeur en 0 ou 5V ou en 3,5V) ;
* Le champ magnétique (exemple : le disque dur).

### Unité élémentaire

L’unité élémentaire utilisée en informatique pour coder l’information est appelée bit, contraction de binary digit.

!!! example "Exercice 2"
    Application au codage d’une couleur : Supposons que l’on souhaite coder des couleurs en binaire :

    1. Combien de couleurs peut-on coder sur un bit ? 
    2. Si l’on souhaite coder davantage de couleurs, il va falloir utiliser une séquence de plusieurs bits appelée mot binaire (ou nombre binaire). Quelles sont les deux manières de nommer un mot de 8 bits. 
    3. Combien de couleurs peuvent coder des mots de 2 bits, 3 bits ... n bits, 1 octet ? 

## Principe de la numération binaire et hexadécimal

### Principe de la représentation d’un nombre en binaire

Le texte de Leibnitz (en figure 1) datant du début du XVIII siècle nous explique le principe de la numération en binaire (base 2) :

<figure markdown>
![leibniz](img_entiers/entiers1.png)
</figure>

!!! example "Exercice 3"
    A partir de ce texte, recopier et compléter le tableau suivant (ne pas tenir compte de la dernière colonne pour l’instant) :

    <figure markdown>

    |Décimal|Binaire (4 bits)| Hexadécimal|
    |:----:|:-------:|:----------:|
    |0     |         |            |
    |1     |         |            |
    |2    |         |            |
    |3    |         |            | 
    |4    |         |            |
    |5    |         |            |
    |6    |         |            | 
    |7     |         |            |
    |8     |         |            |
    |9    |         |            |
    |10    |         |            | 
    |11   |         |            |
    |12   |         |            |
    |13   |         |            | 
    |14     |         |            |
    |15    |         |            |
    |16   |         |            |
   
    </figure>

### Conversion décimal vers binaire
Pour effectuer cette conversion, on effectue une suite de divisions euclidiennes par 2 jusqu'à obtenir un quotient nul. Il suffit ensuite de lister les restes des diverses divisions en commençant par la dernière effectuée.

Exemple :

$$
\begin{array}{r|l}
14 & 2 \\
\hline
0 &  \begin{array}{r|l}
7 & 2 \\
\hline
1 & \begin{array}{r|l}
3 & 2 \\
\hline
1 &\begin{array}{r|l}
1 & 2 \\
\hline
1 & 0
\end{array}
\end{array}
\end{array}
\end{array}
$$


$(14)_{10} = (1110)_2$

!!! example "Exercice 4"

    1. Convertir (4)10 en base 2 ;
    2. Convertir (35)10 en base 2 ;
    3. Convertir (255)10 en base 2.

### Vers le décimal à partir des autres bases

Pour convertir un nombre $N$ d’une base $b$ dans la base $10$, on décompose ce nombre dans l’ordre des puissances décroissantes de la base. Le nombre $N$ s’écrit de façon unique sous la forme :

$$
N = a_n\times b^{n} + ....+ a_2\times b_2 + a_1\times b_1 + a_0 \times b_0\ avec 
	\begin{cases}
	 n  : \text{ un entier naturel ;}  \\
	 b : \text{la base de numération ;}\\
	 a_i : \text{les chiffres associés à  }\\ \text{la base tels que } 0 \le a_i < b.
	\end{cases}
$$


Exemple : $(1101)_2 = 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 = 1 \times 8 + 1 \times 4 + 0 \times 2 + 1 \times 1$
            $(1101)_2 = 13$

!!! example "Exercice 5"

    1. Convertir (1111)2 en base 10 ;
    2. Convertir (10110)2 en base 10 ;

**Remarque :** afin d'effectuer des conversions binaires vers décimal ou décimal vers binaire, il est également possible d'utiliser le tableau ci-dessous : 

<figure markdown>
|  1 octet  |           |          |          |          |         |         |         |         |
|:---------:|:---------:|:--------:|:--------:|:--------:|:-------:|:-------:|:-------:|:-------:|
| $2^8=256$ | $2^7=128$ | $2^6=64$ | $2^5=32$ | $2^4=16$ | $2^3=8$ | $2^2=4$ | $2^1=2$ | $2^0=1$ |
|           |           |          |          |          |         |         |         |         |
|           |           |          |          |          |         |         |         |         |
|           |           |          |          |          |         |         |         |         |
|           |           |          |          |          |         |         |         |         |
</figure>

!!! example "Exercice 6"
    Coder en utilisant le tableau $(1010100)_2$ en décimal

### L'hexadécimal au secours de la manipulation des nombres binaires

La manipulation de nombres binaire est très laborieuse. Pour cette raison, les informaticiens travaillent en hexadécimal (base 16). Dans cette base, 16 caractères sont nécessaires : 0, 1, 2, 3…9, A, B, C,..., F.

!!! example " Exercice 7"
    Compléter le tableau du paragraphe II. 1.

!!! example " Exercice 8"
    Sur combien de bits peut-on coder un chiffre hexadécimal ?

Afin de convertir un nombre binaire en nombre hexadécimal, il suffit de "découper" ce nombre en paquets de 4 bits en partant du bit de poids faible (bit le plus à droite), puis d'attribuer le chiffre hexadécimal correspondant à chaque paquet de 4 bits. La conversion hexadécimale vers binaire est intuitive et encore plus simple.

!!! example " Exercice 9"
    1. Coder $(11111111)_2$, $(1000101)_2$ et ($1110100011)_2$ en hexadécimal
    2. Coder $(12)_{16}$ et $(1AF)_{16}$ en binaire. 