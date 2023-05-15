---
title: "Number Bis"
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


#### Number features in Treebanks

![Number features in treebanks](/images/General_Guideline/Features/Number/number_in_treebank.png)

#### Values of Number in treebanks

![Value Number](/images/General_Guideline/Features/Number/value_number_treebanks.png)

## French 

### Overview

Several upos can have the `Number` features in French, with the two values `Sing` or `Plur` : 

![value](/images/General_Guideline/Features/Number/value_french_nb.png)


### Specific Pattern


#### Features Number for ADV

{{<hint warning>}}
Certains ADV sont annotés avec le trait Number dans PS mais pas dans GSD. Problème de cohérence d'annotation -> je ne sais pas quoi écrire encore ici. Dans tous les cas, ici, on peut mettre un lien vers l'upos [ADV](../Upos/ADV.md#specific-features-of-adv) ? 
{{</hint>}}

#### VERB and AUX without Number

The VERB and the AUX with the features VerbForm=Part|Inf and Tense=Pres don't have the features Number. 

Pattern : N [upos=AUX|VERB, VerbForm= Inf|Part , Tense = Pres]. 

You can visualise some exemple [here](https://universal.grew.fr/?custom=644912808f930)


### validateur ? 

{{<hint info>}}
On peut se servir des différents patterns pour construire le validateur
{{</hint>}}


