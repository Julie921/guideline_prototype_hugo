---
title: "AUX"
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

## French

### Overview 

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
    

### Specific Pattern

### AUX as governor of a relation 

The `AUX` can be the head of différent syntactic relation : 

![AUX as GOV](/images/General_Guideline/Upos/AUX/aux_as_gov.png)

### AUX as dependant of a relation

The `AUX` can be the dependant of différent syntactic relation : 

![AUX as DEP](/images/General_Guideline/Upos/AUX/aux_as_dep.png)

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
9	ai~	avoir	X	_	_	6	mod@rlà je suis en train de créer un formulaire pour que les linguistes elcl	_	ExtPos=AUX
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


## Naija ## test 



## breton 



## testeone 



## testetwo 



## testthree 



## testfour 



## testfive 



## testsix 



## breton

 TODO 


## test

 TODO 


## maintenant

 TODO 


## la

 TODO 


## julie

TODO 



## ok

TODO 



## gbaya

TODO 

