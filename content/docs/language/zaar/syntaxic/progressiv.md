_J'avais finalement une question concernant le point (1) ordre Verbe-Complément différent pour le progressif % aux autres TAM; ordre qui se retrouve dans les syntagmes nominaux ayant un nom verbal comme tête. Je pensais avoir compris sur le coup, mais en écrivant cette requête_

_pattern { GOV -[comp:aux]-> DEP ; GOV[Aspect="Prog"]; DEP[VerbForm="Vnoun"]}_

_et en comparant avec les autres auxiliaires non progressifs je n'ai finalement pas réussi à voir de différence. J'avais pourtant noté quelque chose comme suit : le progressif suivi d'un nom verbal peut prendre un complément avant ou après le verbe, tandis qu'il est toujours après le verbe en temps normal. J'ai l'impression d'avoir loupé quelque chose._

Ta requête récupère les verbes à l’aspect progressif (i.e. suivant un AUX progressif). 

Pour avoir des résultats exploitables, il vaut mieux restreindre les requêtes aux 3 premiers fichiers du corpus, qui ont été corrigés manuellement, avec la ligne suivante, que je te conseille de mettre en tête de toutes tes requêtes : 

% Limite la recherche aux phrases contenant la suite CONV dans leur identifiant. 

global { sent_id = re".*CONV.*" }

##### [http://universal.grew.fr/?custom=63e411a973293](http://universal.grew.fr/?custom=63e411a973293)

Ta requête donne maintenant ceci : (14 phrases)

global { sent_id = re".*CONV.*" }

pattern { GOV -[comp:aux]-> DEP ; GOV[Aspect="Prog"]; DEP[VerbForm="Vnoun"]}

##### [http://universal.grew.fr/?custom=63e412c2e988a](http://universal.grew.fr/?custom=63e412c2e988a)

En fait tous les verbes au progressif devraient être des noms verbaux. On devrait avoir le même résultat en donnant l’UPOS VERB  uniquement

global { sent_id = re".*CONV.*" }

pattern { GOV -[comp:aux]-> DEP ; GOV[Aspect="Prog"]; DEP[upos=VERB]}

On a bien les mêmes résultats (14). 

                (NB : il y avait des différences par rapport à tes résultats, dues à des erreurs d’annotations, que j’ai pu corriger depuis.  

D’autre part, la construction progressive peut être suivie aussi d’un nom, généralement des emprunts, ou d’une prédication locative. 

Cf : [http://universal.grew.fr/?custom=63e6239ac73eb](http://universal.grew.fr/?custom=63e6239ac73eb) Mais c’est pas ça qui nous intéresse ici. En mettant upos=VERB, on élimine ces constructions)

Ce qui nous intéresse, c’est l’ordre dans la relation VERB-COD, en fonction de la forme du verbe. 

Si on recherche la suite AUX –>  Vnoun –>  X, on a très peu d’exemples (12) : 

##### [http://universal.grew.fr/?custom=63e62ca2dfe78](http://universal.grew.fr/?custom=63e62ca2dfe78)

Si on trie sur la relation entre le Vnoun et son dépendant, on obtient : 

##### [http://universal.grew.fr/?custom=63e62cfc73ccf](http://universal.grew.fr/?custom=63e62cfc73ccf)

La relation qui nous intéresse est la relation [udep]. 

(J’ai annoté la relation Verbe-Complément différemment selon la forme des verbes : [comp:obj] quand le verbe est fini, et une autre [udep] que j’ai utilisée pour les noms verbaux (Vnoun). )

On n’en a que 3. Si on se limite à la relation [udep] et qu’on trie sur l’ordre des mots, on obtient : 

##### [http://universal.grew.fr/?custom=63e62dd795402](http://universal.grew.fr/?custom=63e62dd795402)

C’est trop limité pour qu’on puisse en dire quelque chose. J’élargis alors la recherche à toutes les constructions des Vnoun, en ne se limitant pas aux cas où ils dépendent d’un AUX, car ces formes non-finies peuvent être compléments de Verbes, Noms, ADP…

Les constructions avec Vnoun –[udep]-> X sont les suivantes : 

##### [http://universal.grew.fr/?custom=63e61cc80541d](http://universal.grew.fr/?custom=63e61cc80541d)

On peut ensuite étudier l’ordre des mots dans les constructions dépendant d’un Vnoun: 

##### [http://universal.grew.fr/?custom=63e6205771eee](http://universal.grew.fr/?custom=63e6205771eee)

C’est pas écrasant, mais on a une  majorité de constructions avec l’ordre inversé ( Dépendant < --- Vnoun au lieu de Vnoun à dépendant)

(NB : Autre particularité des Vnouns : les compléments obliques se font par un ADP spécifique, /ɓas/, qui n’apparaît que dans cette construction. Voir les 2 exemples du corpus, chacun avec un ordre des mots différents : 

##### [http://universal.grew.fr/?custom=63e615a51b164](http://universal.grew.fr/?custom=63e615a51b164))

L’ordre de la relation comp:obj est, lui, très clair : 

##### [http://universal.grew.fr/?custom=63e620e911da3](http://universal.grew.fr/?custom=63e620e911da3)

Voilà le genre de travail qu’on pourra faire quand on aura recensé les relations syntaxiques.
