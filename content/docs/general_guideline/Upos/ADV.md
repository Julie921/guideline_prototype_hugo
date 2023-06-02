---
title: "ADV"
weight: 3
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# ADVERBE

## Universal

*Definition from [UD website](https://universaldependencies.org/u/pos/ADV.html)*

Adverbs are words that typically modify verbs for such categories as time, place, direction or manner. They may also modify adjectives and other adverbs, as in very briefly or arguably wrong.

There is a closed subclass of pronominal adverbs that refer to circumstances in context, rather than naming them directly; similarly to pronouns, these can be categorized as interrogative, relative, demonstrative etc. Pronominal adverbs also get the ADV part-of-speech tag but they are differentiated by additional features.

Note that in Germanic languages, some adverbs may also function as verbal particles, as in write down or end up. They are still tagged ADV and not PART.

Note that there are words that may be traditionally called numerals in some languages (e.g. Czech) but they are treated as adverbs in our universal tagging scheme. In particular, adverbial ordinal numerals ([cs] poprvé “for the first time”) and multiplicative numerals (e.g. once, twice) behave syntactically as adverbs and are tagged ADV.

Note that there are verb forms such as transgressives or adverbial participles that share properties and usage of adverbs and verbs. Depending on language and context, they may be classified as either VERB or ADV.
Examples
- very
- well
- exactly
- tomorrow
- up, down
- interrogative/relative adverbs: where, when, how, why, whenever, wherever (including when used to mark a clause that is circumstantial, not interrogative or relative)
- demonstrative adverbs: here, there, now, then
- indefinite adverbs: somewhere, sometime, anywhere, anytime
- totality adverbs: everywhere, always
- negative adverbs: nowhere, never
- [de] usw. “etc.” (see conj)

## French
{{< hint info >}}
Les données sont obtenus uniquement sur GSD. Peut-être qu'il faudrait pouvoir faire les tables sur tous les treebank du français ? De plus, les tables de relations n'ont pas vraiment de sens ici pour les UPOS (idem pour une features ou un phénomène). 
On pourrait aussi mettre des tables avec des clusters. 

On peut aussi ajouter des exemples de conlls à chaque fois. 

Pour les tables correspondants aux relations, je ne sais pas si elles sont vraiment pertinentes ? Il faudrait peut-être clusteriser mais ça ferait beaucoup d'information, on perdrait peut-être en visibilité. 
{{< /hint >}}

To have an overview of the ADV in french, you can see the table below : 

{{< agg adv_in_french >}}

An adverb can have different [ExtPos](../Misc/ExtPos.md) : 
![ExtPos of ADV](/images/General_Guideline/Upos/ADV/adv_extpos.png)

### ADV as a governer of a relation 

![ADV as GOV](/images/General_Guideline/Upos/ADV/adv_as_gov.png)

### ADV as a dependant of a relation 

![ADV as DEP](/images/General_Guideline/Upos/ADV/adv_as_dep.png)

### Other UPOS that are used as an ADV 

![UPOS as ADV](/images/General_Guideline/Upos/ADV/adv_ext_cluster_upos.png)

#### [upos = ADP , ExtPos = ADV](http://universal.grew.fr/?custom=642d785a507b0)

When we have a composed ADP (such as : " à propos de", "en effet" etc.) we used ExtPos = ADV for the head of the composed ADP, and the features Idiom/InIdiom for the pattern. 

pattern : N [upos=ADP, ExtPos=ADV, Idiom=Yes], N-[comp:obj]->M ; M [InIdiom=Yes] ; GOV|[mod]->N 

#### [upos= ADV, ExtPos = ADV](http://universal.grew.fr/?custom=642d78695e283)

For this specific case, the pattern as the features Idiom/InIdiom, which necessite the use of the features ExtPos. We have for example : 
- plus que 
- bel et bien 
- bien sûr 

#### [upos=ADJ, ExtPos = ADV](http://universal.grew.fr/?custom=642d7bb85b7db)

Two structures have an ADJ annotated as an ADV : 
- **petit** à petit
- bien **sûr**
The two structures have the features Idiom/InIdiom

#### [upos=VERB, ExtPos=ADV](http://universal.grew.fr/?custom=642d7c4d631a0)

The structure "compte **tenu**" as the VERB `tenir` annotated with ExtPos = ADV. 

#### [upos=X, ExtPos=ADV](http://universal.grew.fr/?custom=642d7c8a5c751)

Some latine expression with upos = X are annotated as ExtPos = ADV, for example : 
- in extremis
- de facto
- a contrario 

#### [upos=PRON, ExtPos=ADV](http://universal.grew.fr/?custom=642d7d55a1bde)

`tout` in : 
- tout de même 
- tout au mieux 

and `rien` in : 
- rien que 

are PRON annotated as ExtPos = ADV

#### [upos=SCONJ, ExtPos=ADV](http://universal.grew.fr/?custom=642d7d6810d9b)

`quand` in `quand même` is an SCONJ annotated with ExtPos = ADV

#### [upos=AUX, ExtPos=ADV](http://universal.grew.fr/?custom=642d7dbbc75e4)

The AUX `être` has the ExtPos=ADV in the french structure : "C'**est** pourquoi"

#### [upos= NOUN , ExtPos = ADV](http://universal.grew.fr/?custom=642d78b376f44)

A few noun can be used as ADV ![noun as adv](/images/General_Guideline/Upos/ADV/noun_as_adv.png)

#### [upos=DET, ExtPos = ADV](http://universal.grew.fr/?custom=642d7981a6263)

In this specific pattern : N [lemma=le, upos=DET, ExtPos=ADV, Idiom=Yes] ; M [upos=ADV, InIdiom=Yes], we annotate the DET as ExtPos = ADV. For example : 
- le plus 
- le moins 
- le mieux 
This pattern is a modifier of a node in the sentence. 

#### [upos=SYM, ExtPos=ADV](http://universal.grew.fr/?custom=642d7b177d05e)

Some symbols are annotated as ADV 

{{%expand "à ajouter aux autres sections" %}}
#### upos = ADV, ExtPos = PRON

In this pattern : N [upos = PRON] ; N-[comp:obl]->M ; M [lemma=de], N is annotated as ExtPos=ADV. For example : 
- **combien** de 
- **plus** de 
- **beaucoup** de
- **un peu** de

This pattern also have the feature Idiom/InIdiom

#### upos = ADV, ExtPos = SCONJ

In this pattern : N [upos = PRON] ; N-[unk]->M ; M [lemma=que], N is annotated as ExtPos=ADV. For example : 
- **bien** que
- **tant** que
- **parce** que

This pattern also have the feature Idiom/InIdiom

#### upos = ADV, ExtPos = CCONJ 

In this pattern : N [upos = PRON] ; N-[unk]->M ; M [lemma=que], N is annotated as ExtPos=ADV. For example : 
- **ainsi** que

This pattern also have the feature Idiom/InIdiom

{{% /expand%}}

### Specific features of ADV

In french, the ADV can have the features [`Polarity`](../Features/Polarity.md) with `Polarity=Neg` or `Polarity=Pos`. 

`Neg` is used for the negativ sentences in french. For example :

{{< conll >}}
# text = bon euh on n'a pas gagné malheureusement.
1	bon	bon	INTJ	_	_	5	discourse	_	_
2	euh	euh	INTJ	_	_	5	discourse	_	_
3	on	on	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Ind	5	subj	_	_
4	n'	ne	ADV	_	Polarity=Neg	5	mod	_	SpaceAfter=No
5	a	avoir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
6	pas	pas	ADV	_	Polarity=Neg	5	mod	_	_
7	gagné	gagner	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	5	comp:aux@tense	_	SpaceAfter=No
8	.	.	PUNCT	_	_	5	punct	_	_
{{< /conll >}}

`Pos` is used in this context : 

{{< conll >}}
# text = Si jamais vous lui posez la question, il en rigolera.
1	Si	si	SCONJ	_	_	11	mod	_	wordform=si
2	jamais	jamais	ADV	_	Polarity=Pos	5	mod	_	_
3	vous	vous	PRON	_	Emph=No|Number=Plur|Person=2|PronType=Prs	5	subj	_	_
4	lui	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	5	comp:obl	_	_
5	posez	poser	VERB	_	Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin	1	comp:obj	_	_
6	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	7	det	_	_
7	question	question	NOUN	_	Gender=Fem|Number=Sing	5	comp:obj	_	SpaceAfter=No
8	,	,	PUNCT	_	_	1	punct	_	_
9	il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	11	subj	_	_
10	en	en	PRON	_	Emph=No|Person=3|PronType=Prs	11	comp:obl	_	_
11	rigolera	rigoler	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin	0	root	_	SpaceAfter=No
12	.	.	PUNCT	_	_	11	punct	_	_
{{< /conll >}}

You can find more example in the corpus :

{{< agg adv_neg_french >}}

## Naija ## test 



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

