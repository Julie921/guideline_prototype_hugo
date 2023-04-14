---
title: "Aux"
weight: 3
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Auxiliaire

## Universal 
*Definition from [UD website](https://universaldependencies.org/u/dep/aux_.html)*

An aux (auxiliary) of a clause is a function word associated with a verbal predicate that expresses categories such as tense, mood, aspect, voice or evidentiality. It is often a verb (which may have non-auxiliary uses as well) but many languages have nonverbal TAME markers and these are also treated as instances of aux. Auxiliares used to construct the passive voice are now also labeled aux.

## French auxiliaires 

In French, only four verbs are considered auxiliaries: **être**, **avoir**, **faire** (also ***refaire***) and **se voir**.

{{< hint info >}}
pattern { N [upos=AUX] } % and clustering N.lemma for example
{{< /hint >}}

{{< hint info >}}
You can find a discussion about the french auxiliaires [here](https://github.com/surfacesyntacticud/guidelines/issues/13)
{{< /hint >}}
The french auxiliaire can have an ExtPos=`ADP` only in one context, the idiom "étant donné". You can find more information [here](./ADP.md)

{{< hint danger >}}
La colonne du lemmes être n'est pas cliquable -> problème d'encodage du "ê". 
{{< /hint >}}
{{< agg diff_aux >}}

### AUX as governor of a relation 

The `AUX` can be the head of différent syntactic relation : 

![AUX as GOV](/images/aux_as_gov.png)

### AUX as dependant of a relation

The `AUX` can be the dependant of différent syntactic relation : 

![AUX as DEP](/images/aux_as_dep.png)

### Other upos that are used as an AUX 

In spoken french treebank, there is only the disfluencies (which are annotated `upos=X`) that can be used as an `AUX`. 

{{< conll >}}
# text = et euh c'est vraiment ce que j'ai~ j'ai vraiment adoré ce côté là.
1	et	et	CCONJ	_	_	4	cc	_	_
2	euh	euh	INTJ	_	_	1	discourse	_	_
3	c'	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	4	subj	_	SpaceAfter=No
4	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
5	vraiment	vraiment	ADV	_	_	4	mod	_	_
6	ce	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	4	comp:pred	_	_
7	que	que	PRON	_	PronType=Rel	13	comp:obj	_	_
8	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	9	subj	_	SpaceAfter=No
9	ai~	avoir	X	_	_	6	mod@relcl	_	ExtPos=AUX
10	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	11	subj	_	SpaceAfter=No
11	ai	avoir	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	9	conj:dicto	_	_
12	vraiment	vraiment	ADV	_	_	13	mod	_	_
13	adoré	adorer	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	11	comp:aux@tense	_	_
14	ce	ce	DET	_	Gender=Masc|Number=Sing|PronType=Dem	15	det	_	_
15	côté	côté	NOUN	_	Gender=Masc|Number=Sing	4	dislocated	_	_
16	là	là	ADV	_	_	15	mod	_	SpaceAfter=No
17	.	.	PUNCT	_	_	4	punct	_	_
{{< /conll >}}

{{< agg extpos_aux_fr >}}

### Specific features of AUX 

Auxiliary have specific features. A portion of these features can be hierarchized as shown in the diagram below. You can explore various examples in the GSD corpus of French through the links provided in the diagram

{{< hint info >}}
A revoir ? Pas de hierarchie ici entre Person/Number/Tense une fois que le Mood et le VerbForm sont déterminés. Est-ce qu'on en met une ? Si oui, dans quel ordre ?
{{< /hint >}}

- [VerbForm](../Features/VerbForm.md) 
    - [Part](http://universal.grew.fr/?custom=64392c994592f) 
        - [Tense](../Features/Tense.md) 
            - [Past](http://universal.grew.fr/?custom=64392cb36a9c5)
                - [Number](../Features/Number.md)
                    - [Sing](http://universal.grew.fr/?custom=64392efc41cec)
                    - Plur
                - Gender
                    - Fem
                    - Masc
            - [Pres](http://universal.grew.fr/?custom=64392cd5284e9) 
                - rien
    - [Inf](http://universal.grew.fr/?custom=64392cf1df13a) 
        - rien
    - [Fin](http://universal.grew.fr/?custom=64392d048da0b)
        - [Mood](../Features/Mood.md)
            - [Ind](http://universal.grew.fr/?custom=64392d1d1b64c)
                - Tense
                    - [Imp](http://universal.grew.fr/?custom=64392d35629bf)
                    - Fut
                    - Past
                    - Pres
                - Person
                    - [1](http://universal.grew.fr/?custom=64392e60d322e)
                    - [2](http://universal.grew.fr/?custom=64392dbb60fb4)
                    - 3
                - Number
                    - [Sing](http://universal.grew.fr/?custom=64392e48df82a)
                    - [Plur](http://universal.grew.fr/?custom=64392dcd061cd)
            - Subj and Cnd
                - Tense
                    - Pres
                - Person
                    - 1
                    - 2
                    - 3
                - Number
                    - Sing
                    - Plur
            - Imp
                - Tense
                    - Pres
                - Person
                    - 1
                    - 2
                - Number
                    - Plur
                    - Sing
    
### AUX or VERB ?

It is sometimes not trivial to chose between the part of speech `AUX` and `VERB` for **être**. We propose this distinction : 
- when **être** has a predicative complement, it is always considered as a copula and it has the POS `AUX` 

**Example**


- when **être** has an existensial meaning (*je pense donc je suis* -***I think therefore I am***) or has a locative argument or another argument, which is not a predicative argument (*je suis pour la dépénalisation du cannabis* -***I am for the decriminalization of cannabis***), it has the POS `VERB`.

**Locative argument**
{{< conll >}}
# text = Ils sont sur Cherbourg depuis 2007.
1	Ils	eux	PRON	_	Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs	2	subj	_	wordform=ils
2	sont	être	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	sur	sur	ADP	_	_	2	comp:obl	_	_
4	Cherbourg	Cherbourg	PROPN	_	_	3	comp:obj	_	_
5	depuis	depuis	ADP	_	_	2	mod	_	_
6	2007	2007	NUM	_	Number=Plur	5	comp:obj	_	SpaceAfter=No
7	.	.	PUNCT	_	_	2	punct	_	_
{{< /conll >}}

**Existensial meaning** 
{{< conll >}}
# text = Pourquoi en serait-il autrement cette fois-ci ?
1	Pourquoi	pourquoi	ADV	_	_	3	mod	_	wordform=pourquoi
2	en	en	PRON	_	Emph=No|Person=3|PronType=Prs	3	comp@expl	_	_
3	serait	être	VERB	_	Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	SpaceAfter=No
4	-il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj	_	wordform=il
5	autrement	autrement	ADV	_	_	3	mod	_	_
9	?	?	PUNCT	_	_	3	punct	_	_
{{< /conll >}}

>[!NOTE]
> you can find the discussion about the distinction between `AUX` and `VERB` [here](https://github.com/surfacesyntacticud/guidelines/issues/11)

#### Table 

{{< hint danger >}}

WARNING : cette table ne renvoie pas vers les requêtes grew car j'utilise le lemme "être" et il y a un problème d'encodage.

{{< /hint >}}

{{< agg etre_aux_verb >}}

## Naija 