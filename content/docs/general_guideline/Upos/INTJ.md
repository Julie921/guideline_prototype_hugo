---
title: "INTJ"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Interjection

## Universal 

*Definition from de [UD website](https://universaldependencies.org/u/pos/INTJ.html)*

An interjection is a word that is used most often as an exclamation or part of an exclamation. It typically expresses an emotional reaction, is not syntactically related to other accompanying expressions, and may include a combination of sounds not otherwise found in the language.

Note that words primarily belonging to another part of speech retains their original category when used in exclamations. For example, God is a NOUN even in exclamatory uses.

As a special case of interjections, we recognize feedback particles such as yes, no, uhuh, etc.

*Examples :*
* psst
* ouch
* bravo
* hello


## French

### Overview

 Pure interjections (such as ah, hein, ouais, euh, etc.) are analysed as INTJs.  Except 4 of them which are frequent and are analysed as pure INTJs: bon, ben, quoi, and tiens.

 The upos None has the values : ['None']


### Specific Pattern

#### other POS with [INTJ](docs/general_guideline/Upos/INTJ.md) as [ExtPos](docs/general_guideline/Misc/ExtPos.md) 

- Pattern: GOV[[ExtPos](docs/general_guideline/Misc/ExtPos.md)=[INTJ](docs/general_guideline/Upos/INTJ.md)]


- Description: Discourse markers coming from other POS (such as enfin, chouette, disons, etc.), as well as idioms (such as en fait, tu sais, etc.), keep their original POS but have an additional [ExtPos](docs/general_guideline/Misc/ExtPos.md) = [INTJ](docs/general_guideline/Upos/INTJ.md) feature.

{{<conll>}} 
# text = mais, oui oui oui, bien sûr.
1	mais	mais	[CCONJ](docs/general_guideline/Upos/CCONJ.md)	_	_	3	cc	_	AlignBegin=45190|AlignEnd=45450|SpaceAfter=No
2	,	,	[PUNCT](docs/general_guideline/Upos/PUNCT.md)	_	_	1	punct	_	AlignBegin=45450|AlignEnd=45450
3	oui	oui	[ADV](docs/general_guideline/Upos/ADV.md)	_	_	0	root	_	AlignBegin=45450|AlignEnd=45709|[ExtPos](docs/general_guideline/Misc/ExtPos.md)=[INTJ](docs/general_guideline/Upos/INTJ.md)
4	oui	oui	[ADV](docs/general_guideline/Upos/ADV.md)	_	_	3	conj:coord	_	AlignBegin=45709|AlignEnd=45969|[ExtPos](docs/general_guideline/Misc/ExtPos.md)=[INTJ](docs/general_guideline/Upos/INTJ.md)
5	oui	oui	[ADV](docs/general_guideline/Upos/ADV.md)	_	_	4	conj:coord	_	AlignBegin=45969|AlignEnd=46228|[ExtPos](docs/general_guideline/Misc/ExtPos.md)=[INTJ](docs/general_guideline/Upos/INTJ.md)|SpaceAfter=No
6	,	,	[PUNCT](docs/general_guideline/Upos/PUNCT.md)	_	_	7	punct	_	AlignBegin=46228|AlignEnd=46228
7	bien	bien	[ADV](docs/general_guideline/Upos/ADV.md)	_	_	8	[mod](docs/general_guideline/Syntactic_relations/mod/mod.md)	_	AlignBegin=46228|AlignEnd=46488
8	sûr	sûr	[ADV](docs/general_guideline/Upos/ADV.md)	_	_	3	[mod](docs/general_guideline/Syntactic_relations/mod/mod.md)	_	AlignBegin=46488|AlignEnd=46747|SpaceAfter=No
9	.	.	[PUNCT](docs/general_guideline/Upos/PUNCT.md)	_	_	3	punct	_	AlignBegin=46747|AlignEnd=46747
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg french_INTJ_ExtPos >}}



