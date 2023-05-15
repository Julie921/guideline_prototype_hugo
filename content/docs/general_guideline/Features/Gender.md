---
title: "Gender"
weight: 2
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# Gender

## Universal

*Definition from de [UD website](https://universaldependencies.org/u/feat/Gender.html)*
Gender is usually a lexical feature of nouns and inflectional feature of other parts of speech (pronouns, adjectives, determiners, numerals, verbs) that mark agreement with nouns. In English gender affects only the choice of the personal pronoun (he / she / it) and the feature is usually not encoded in English tagsets.

See also the related feature of [Animacy](./Animacy.md).

African languages have an analogous feature of noun classes: there might be separate grammatical categories for flat objects, long thin objects etc.

### Value

[Com](https://universaldependencies.org/u/feat/Gender.html#Com),
[Fem](https://universaldependencies.org/u/feat/Gender.html#Fem),
[Masc](https://universaldependencies.org/u/feat/Gender.html#Masc),
[Neut](https://universaldependencies.org/u/feat/Gender.html#Neut).

#### Number features in Treebanks

![Number features in treebanks](/images/General_Guideline/Features/Gender/tables_feats.png)

#### Values of Number in treebanks

![Value Number](/images/General_Guideline/Features/Gender/tables_feats_value.png)

{{<hint info>}}
La suite est générée depuis un formulaire - page TEST pour la formalisation et l'aide à la rédaction.
{{</hint>}}

## French

### Overview
 The features `[Gender](docs/general_guideline/Features/Gender.md)` in french can be on several upos.

 The upos [AUX](docs/general_guideline/Upos/AUX.md) has the values : ['Fem', 'Masc']


### Specific Pattern

#### Plurial and [Gender](docs/general_guideline/Features/Gender.md) for the [NOUN](docs/general_guideline/Upos/NOUN.md) 

- Pattern: N [upos = [NOUN](docs/general_guideline/Upos/NOUN.md), [Number](docs/general_guideline/Features/Number.md)=Plur, ![Gender](docs/general_guideline/Features/Gender.md)]


- Description: Sometimes, in french, the [NOUN](docs/general_guideline/Upos/NOUN.md) don't have the features `[Gender](docs/general_guideline/Features/Gender.md)` when they have [Number](docs/general_guideline/Features/Number.md)=Plur. It is because we can get the information.

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg Gender >}}



## french

### Overview

 This is a test to create a page from the formular directly 

 The upos [ADV](docs/general_guideline/Upos/ADV.md) has the values : ['Yes', 'No']


### Specific Pattern

#### Explication one 

- Pattern: GOV[[Gender](docs/general_guideline/Features/Gender.md)=Masc]


- Description: This is still a test

{{<conll>}} 
# text = mh.
1	mh	mh	[INTJ](docs/general_guideline/Upos/INTJ.md)	_	_	0	root	_	AlignBegin=13304|AlignEnd=13483|SpaceAfter=No
2	.	.	[PUNCT](docs/general_guideline/Upos/PUNCT.md)	_	_	1	punct	_	AlignBegin=13483|AlignEnd=13483{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_Gender >}}


