---
title: "Adv"
weight: 3
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

## ADVERBE


### Universal

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

### French
{{< hint info >}}
Les données sont obtenus uniquement sur GSD. Peut-être qu'il faudrait pouvoir faire les tables sur tous les treebank du français ? De plus, les tables de relations n'ont pas vraiment de sens ici pour les UPOS (idem pour une features ou un phénomène). 
On pourrait aussi mettre des tables avec des clusters. 

On peut aussi ajouter des exemples de conlls à chaque fois. 

Pour les tables correspondants aux relations, je ne sais pas si elles sont vraiment pertinentes ? Il faudrait peut-être clusteriser mais ça ferait beaucoup d'information, on perdrait peut-être en visibilité. 
{{< /hint >}}

An adverb can have different [ExtPos](ExtPos.md) : 
![ExtPos of ADV](/images/adv_extpos.png)

#### ADV as a governer of a relation 

![ADV as GOV](/images/adv_as_gov.png)

#### ADV as a dependant of a relation 

![ADV as DEP](/images/adv_as_dep.png)

#### Other UPOS that are used as an ADV 

![UPOS as ADV](/images/adv_ext_cluster_upos.png)

##### [upos = ADP , ExtPos = ADV](http://universal.grew.fr/?custom=642d785a507b0)

When we have a composed ADP (such as : " à propos de", "en effet" etc.) we used ExtPos = ADV for the head of the composed ADP, and the features Idiom/InIdiom for the pattern. 

pattern : N [upos=ADP, ExtPos=ADV, Idiom=Yes], N-[comp:obj]->M ; M [InIdiom=Yes] ; GOV|[mod]->N 

##### [upos= ADV, ExtPos = ADV](http://universal.grew.fr/?custom=642d78695e283)

For this specific case, the pattern as the features Idiom/InIdiom, which necessite the use of the features ExtPos. We have for example : 
- plus que 
- bel et bien 
- bien sûr 

##### [upos=ADJ, ExtPos = ADV](http://universal.grew.fr/?custom=642d7bb85b7db)

Two structures have an ADJ annotated as an ADV : 
- **petit** à petit
- bien **sûr**
The two structures have the features Idiom/InIdiom

##### [upos=VERB, ExtPos=ADV](http://universal.grew.fr/?custom=642d7c4d631a0)

The structure "compte **tenu**" as the VERB `tenir` annotated with ExtPos = ADV. 

##### [upos=X, ExtPos=ADV](http://universal.grew.fr/?custom=642d7c8a5c751)

Some latine expression with upos = X are annotated as ExtPos = ADV, for example : 
- in extremis
- de facto
- a contrario 

##### [upos=PRON, ExtPos=ADV](http://universal.grew.fr/?custom=642d7d55a1bde)

`tout` in : 
- tout de même 
- tout au mieux 

and `rien` in : 
- rien que 

are PRON annotated as ExtPos = ADV

##### [upos=SCONJ, ExtPos=ADV](http://universal.grew.fr/?custom=642d7d6810d9b)

`quand` in `quand même` is an SCONJ annotated with ExtPos = ADV

##### [upos=AUX, ExtPos=ADV](http://universal.grew.fr/?custom=642d7dbbc75e4)

The AUX `être` has the ExtPos=ADV in the french structure : "C'**est** pourquoi"

##### [upos= NOUN , ExtPos = ADV](http://universal.grew.fr/?custom=642d78b376f44)

A few noun can be used as ADV ![noun as adv](/images/noun_as_adv.png)

##### [upos=DET, ExtPos = ADV](http://universal.grew.fr/?custom=642d7981a6263)

In this specific pattern : N [lemma=le, upos=DET, ExtPos=ADV, Idiom=Yes] ; M [upos=ADV, InIdiom=Yes], we annotate the DET as ExtPos = ADV. For example : 
- le plus 
- le moins 
- le mieux 
This pattern is a modifier of a node in the sentence. 

##### [upos=SYM, ExtPos=ADV](http://universal.grew.fr/?custom=642d7b177d05e)

Some symbols are annotated as ADV 

{{%expand "à ajouter aux autres sections" %}}
##### upos = ADV, ExtPos = PRON

In this pattern : N [upos = PRON] ; N-[comp:obl]->M ; M [lemma=de], N is annotated as ExtPos=ADV. For example : 
- **combien** de 
- **plus** de 
- **beaucoup** de
- **un peu** de

This pattern also have the feature Idiom/InIdiom

##### upos = ADV, ExtPos = SCONJ

In this pattern : N [upos = PRON] ; N-[unk]->M ; M [lemma=que], N is annotated as ExtPos=ADV. For example : 
- **bien** que
- **tant** que
- **parce** que

This pattern also have the feature Idiom/InIdiom

##### upos = ADV, ExtPos = CCONJ 

In this pattern : N [upos = PRON] ; N-[unk]->M ; M [lemma=que], N is annotated as ExtPos=ADV. For example : 
- **ainsi** que

This pattern also have the feature Idiom/InIdiom

{{% /expand%}}