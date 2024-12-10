# Les bases en Javascript

## Javascript


Le langage HTML (ou Hypertext Markup Language) permet de créer la structure d’une page internet. Grâce à un jeu de balises, il permet de décomposer la page comme un traitement de texte : titre, sous-titre, section,...

Le CSS (ou Cascade Style Sheets) permet la mise en forme des différents éléments HTML.
On peut ainsi modifier la couleur ou la police des éléments précédents.

Les pages ainsi créées sont statiques c’est-à-dire que l’interaction avec l’utilisateur est réduite à la possibilité de cliquer sur un
lien hypertexte présent dans la page.

On peut dynamiser la page internet de deux manières :

* soit du côté serveur avec PHP (ou Hypertext Preprocessor) qui peut, par exemple, ajouter le
résultat d’une requête à une base de données dans la page qui sera fournie au navigateur ;
* soit du côté client avec JavaScript qui peut, par exemple, faire apparaître des info-bulles contextuelles ou réaliser des animations.

JavaScript est un langage qui a été créé en 1995 par Brendan Eich. Ce dernier a travaillé chez Netscape Communication Corporation principal
concurrent à l’époque d’Internet Explorer.

## Premier Programme

### Code

Ne dérogeons pas à la règle traditionnelle qui veut que tous les tutoriels de programmation
commencent par afficher le texte « Hello World ! »

Voici un code HTML simple contenant une instruction (nous allons y revenir) JavaScript, placée au
sein d’un élément `<script>`:

```html linenums="1"
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
            <title>Hello World!</title>
        </head>
    <body>


    <script>
    alert('Hello world!'); // affichage
    </script>


</body>
```

### Observations et changements par rapport à Python

* Un élément `<script>` est présent dans la page HTML : c’est cet élément qui contient le code
Javascript ;
* Le code Javascript ne contient qu’une seule instruction : l’instruction `alert()`. Cette instruction
permet d’afficher une boîte de dialogue contenant un message. Le message en question est placé
entre apostrophes.
* La sortie avec la fonction `alert()` peut être remplacé par une sortie sur la console grâce à
l’instruction `console.log('Hello world!')`. Il faut se rendre sur la console du navigateur (en
général : menu puis développement web puis console web) ou encore sur le corps de la page
web avec l’instruction `document.write('Hello world!')`
* Chaque instruction doit se terminer par un point virgule ;
* Le Javascript, contrairement au Python n’est sensible ni à l’indentation, ni aux espaces ;
* Les commentaires monolignes commencent par deux slashs `//`(tandis qu’en Python ils commencent par #) et les commentaires multilignes se font par `/*` et se termine par `*/` .

**Remarque :** on peut aussi placer un commentaire multiligne sur une seule ligne

Exemple :
``` html linenums="1"
/* Ce script comporte 3 instructions :
- Instruction 1 qui fait telle chose
- Instruction 2 qui fait autre chose
- Instruction 3 qui termine le script
*/

instruction_1;
instruction_2; /*Commentaire */
instruction_3; // Fin du script
```

!!! exercice "Exercice 1 :"
    Afficher son prénom sur une boite de dialogue puis dans la console. Puis y placer un commentaire monoligne et un commentaire multiligne.

## Où écrire son code

Il est possible, et même conseillé, d’écrire le code JavaScript dans un fichier externe, portant
l’extension .js. Ce fichier est ensuite appelé depuis la page Web au moyen de l’élément `<script>` et
de son attribut src qui contient l’URL du fichier.js. Ce code fichier.js s’insère dans l’HTML de la
manière suivante :

``` html linenums="1"
<script src="fichier.js"></script>
```


Dans votre éditeur web, taper le code suivant :

``` html linenums="1"
<!DOCTYPE html>
<html>
    <body>

        <h1>Mon premier script JavaScript</h1>

            <button type="button" onclick="document.getElementById('demo').innerHTML = 'Bonjour le monde !'"> Clic moi....</button>

            <p id="demo"></p>

    </body>
</html>
```

!!! example "Exercice 1"
    1. Identifier le script et modifier le texte à afficher
    2. Comment le script indentifie-t-il l’élément html à modifier ?
    3. Modifier le script pour changer le t