---
title: "Number"
weight: 2
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false 
---

# Number 

## Universal

*Definition from de [UD website](https://universaldependencies.org/u/feat/Number.html)*
Number is usually an inflectional feature of [nouns](../Upos/NOUN.md) and, depending on language, other parts of speech ([pronouns](../Upos/PRON.md), [adjectives](../Upos/ADJ.md), [determiners](../Upos/DET.md), [numerals](../Upos/NUM.md), [verbs](../Upos/VERB.md)) that mark agreement with [nouns](../Upos/NOUN.md).

In languages where noun phrases are pluralized using a specific function word (pluralizer), this function word is tagged DET and `Number=Plur` is its lexical feature.

It can have severals [values](https://universaldependencies.org/u/feat/all.html#al-u-feat/Number) and [layered features](https://universaldependencies.org/u/overview/feat-layers.html).

### Value

{{<hint info>}}
Est-ce qu'on ré-écrit l'information du UD ou est-ce qu'on renvoie vers le site et la page correspondante ?
{{</hint>}}

[Coll](https://universaldependencies.org/u/feat/Number.html#Coll),
[Count](https://universaldependencies.org/u/feat/Number.html#Count),
[Dual](https://universaldependencies.org/u/feat/Number.html#Dual),
[Grpa](https://universaldependencies.org/u/feat/Number.html#Grpa),
[Grpl](https://universaldependencies.org/u/feat/Number.html#Grpl),
[Inv](https://universaldependencies.org/u/feat/Number.html#Inv),
[Paux](https://universaldependencies.org/u/feat/Number.html#Paux),
[Plur](https://universaldependencies.org/u/feat/Number.html#Plur),
[Ptang](https://universaldependencies.org/u/feat/Number.html#Ptang),
[Sing](https://universaldependencies.org/u/feat/Number.html#Sing), 
[Tri](https://universaldependencies.org/u/feat/Number.html#Tri).

#### Sing : singular number

A singular noun denotes one person, animal or thing.
*Examples* : [en] car

### Examples

{{<hint info>}}
Différents tableaux possibles.
{{</hint>}}

#### Number features in Treebanks

![Number features in treebanks](/images/General_Guideline/Features/Number/number_in_treebank.png)

#### Values of Number in treebanks

![Value Number](/images/General_Guideline/Features/Number/value_number_treebanks.png)

{{< conll >}}
# text = euh, je pense que la chirurgie, c'est pareil, hein.
1	euh	euh	INTJ	_	_	4	discourse	_	SpaceAfter=No
2	,	,	PUNCT	_	_	1	punct	_	_
3	je	il	PRON	_	Number=Sing|Person=1|PronType=Prs	4	subj	_	_
4	pense	penser	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	_
5	que	que	SCONJ	_	_	4	comp:obj	_	_
6	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	7	det	_	_
7	chirurgie	chirurgie	NOUN	_	Gender=Fem|Number=Sing	10	dislocated	_	SpaceAfter=No
8	,	,	PUNCT	_	_	7	punct	_	_
9	c'	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	10	subj	_	SpaceAfter=No
10	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	5	comp:obj	_	_
11	pareil	pareil	ADJ	_	Gender=Masc|Number=Sing	10	comp:pred	_	SpaceAfter=No
12	,	,	PUNCT	_	_	13	punct	_	_
13	hein	hein	INTJ	_	_	11	discourse	_	SpaceAfter=No
14	.	.	PUNCT	_	_	4	punct	_	_
{{< /conll >}}


## french 

### Overview

Several upos can have the `Number` features in French, with the two values ̀`Sing` or ̀`Plur` :  

![value](/images/General_Guideline/Features/Number/value_french_nb.png)

{{<hint info>}}
On peut mettre des liens vers les upos directement (la partie qui décrit le français à chaque fois). Par exemple [AUX](../Upos/AUX.md#specific-features-of-aux) ? 
{{</hint>}}

### Pattern

{{<hint warning>}}
Pour les relations, c'est l'ExtPos qui est importante. Pour les features, c'est l'upos qui est important. Par exemple, les NOUN qui ont une ExtPos=INTJ ont des traits Number, contrairement aux upos=INTJ. 
{{</hint>}}

You can find some examples in the corpus below : 

![Number POS french](/images/General_Guideline/Features/Number/grew_number_upos_value_fr.png)

{{< hint info >}}
Tableau double entrée pour avoir les valeurs de traits ? Il faut un moyen de mettre les trois treebank du français... 
+ Est-ce qu'on décrit les règles d'accord par exemple ? 
+ Les upos qui n'ont pas le trait Number ? 
{{< /hint >}}

#### Features Number for ADV

{{<hint warning>}}
Certains [ADV](docs/general_guideline/Upos/ADV.md) sont annotés avec le trait Number dans PS mais pas dans GSD. Problème de cohérence d'annotation -> je ne sais pas quoi écrire encore ici. Dans tous les cas, ici, on peut mettre un lien vers l'upos [ADV](../Upos/ADV.md#specific-features-of-adv) ? 
{{</hint>}}

#### Upos without Number

But, sometimes these upos don't have the features Number. 
{{<hint info>}}
On peut y inclure ce genre de requête par exemple : 
+ [les adjectifs (ExtPos/upos) qui n'ont pas la features Number (ni Idiom/InIdiom).](https://universal.grew.fr/?custom=64491149c11aa)
+ [les auxiliaires/verbes VerbForm=Part|Inf et Tense=Pres](https://universal.grew.fr/?custom=644912808f930) -> lien vers [AUX](../Upos/AUX.md#specific-features-of-aux)
+ autres exemples 
{{</hint>}}

### validateur ? 

{{<hint info>}}
On peut se servir des différents patterns pour construire le validateur
{{</hint>}}




## french

TODO
### Overview

### Specific Pattern




## haitien

TODO
### Overview

### Specific Pattern


