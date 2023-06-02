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


- Description: Sometimes, in french, the [NOUN](docs/general_guideline/Upos/NOUN.md) don't have the features `[Gender](docs/general_guideline/Features/Gender.md)` when they have [Number](docs/general_guideline/Features/Number.md)=Plur. It is because we can't get the information.

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg Gender >}}


## test 



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



## beja2

TODO 



## beja3



  ## beja3

### Overview

 Nope, it's just a test !

{{<conll>}} 
# text_en = "Girl! chase the donkey away!" he said, he said.
1	t=	_	DET	DET	Definite=Def|Gender=Fem	2	det	_	AlignBegin=13911|AlignEnd=13996|GE=[DEF].[F]=|RX=[DET]=|TokenType=Clit
2	ʔoːrej	_	NOUN	N	_	5	vocative	_	AlignBegin=13996|AlignEnd=14167|GE=child-[VOC]|Gloss=child|MGloss=child-VOC|MSeg=ʔoːr-ej|RX=[N]-[CASE]|TokenType=Stem
3	oː=	_	DET	DET	Case=Acc|Definite=Def|Gender=Masc|Number=Sing	4	det	_	AlignBegin=14167|AlignEnd=14295|GE=[DEF].[SG].[M].[ACC]=|RX=[DET]=|TokenType=Clit
4	meːk	_	NOUN	N	_	5	comp:obj	_	AlignBegin=14295|AlignEnd=14424|GE=donkey|Gloss=donkey|RX=[N]|TokenType=Stem
5	fidini	_	VERB	V1	Gender=Fem|Number=Sing|VerbClass=1	7	compound:svc	_	AlignBegin=14424|AlignEnd=14681|GE=move_away-[IMP].[SG].[F]|Gloss=move_away|MGloss=move_away-IMP.SG.F|MSeg=fidin-i|RX=[V1]-[TAM].[PNG]|TokenType=Stem
6	/	_	PUNCT	PUNCT	_	5	punct	_	AlignBegin=14681|AlignEnd=14938|TokenType=Break
7	galeːlin	_	VERB	V2	Gender=Fem|Number=Sing|VerbClass=2	8	parataxis:obj	_	AlignBegin=14938|AlignEnd=15244|GE=drive_cattle-[IMP].[SG].[F]-[EMPH]|Gloss=drive_cattle|MGloss=drive_cattle-IMP.SG.F-EMPH|MSeg=galeːl-i-n|ReportedSpeech=Yes|RX=[V2]-[TAM].[PNG]-[SUFX]|TokenType=Stem
8	idi	_	VERB	V1, IRG	Aspect=Pfv|Gender=Masc|Number=Sing|VerbClass=1	0	root	_	AlignBegin=15244|AlignEnd=15551|GE=[3SG].[M]-say\[PFV]|Gloss=say|MGloss=3SG.M-say\PFV|MSeg=i-di|RX=[PNG]-[V1].[IRG]|TokenType=Stem
9	ini	_	VERB	V1, IRG	Aspect=Pfv|Gender=Masc|Number=Sing|VerbClass=1	8	discourse	_	AlignBegin=15551|AlignEnd=15857|GE=[3SG].[M]-say\[PFV]|Gloss=say|MGloss=3SG.M-say\PFV|MSeg=i-ni|RX=[PNG]-[V1].[IRG]|TokenType=Stem
10	//	_	PUNCT	PUNCT	_	8	punct	_	AlignBegin=15857|AlignEnd=16164|TokenType=Break
{{</conll>}}

 The upos [DET](docs/general_guideline/Upos/DET.md) has the values : ['Masc', 'Fem']


### Specific Pattern

#### gender in beja test 

- Description: Nope, again, just a test here

- Pattern: N [Gender]


{{<conll>}}
# text_en = "Girl! chase the donkey away!" he said, he said.
1	t=	_	DET	DET	Definite=Def|Gender=Fem	2	det	_	AlignBegin=13911|AlignEnd=13996|GE=[DEF].[F]=|RX=[DET]=|TokenType=Clit
2	ʔoːrej	_	NOUN	N	_	5	vocative	_	AlignBegin=13996|AlignEnd=14167|GE=child-[VOC]|Gloss=child|MGloss=child-VOC|MSeg=ʔoːr-ej|RX=[N]-[CASE]|TokenType=Stem
3	oː=	_	DET	DET	Case=Acc|Definite=Def|Gender=Masc|Number=Sing	4	det	_	AlignBegin=14167|AlignEnd=14295|GE=[DEF].[SG].[M].[ACC]=|RX=[DET]=|TokenType=Clit
4	meːk	_	NOUN	N	_	5	comp:obj	_	AlignBegin=14295|AlignEnd=14424|GE=donkey|Gloss=donkey|RX=[N]|TokenType=Stem
5	fidini	_	VERB	V1	Gender=Fem|Number=Sing|VerbClass=1	7	compound:svc	_	AlignBegin=14424|AlignEnd=14681|GE=move_away-[IMP].[SG].[F]|Gloss=move_away|MGloss=move_away-IMP.SG.F|MSeg=fidin-i|RX=[V1]-[TAM].[PNG]|TokenType=Stem
6	/	_	PUNCT	PUNCT	_	5	punct	_	AlignBegin=14681|AlignEnd=14938|TokenType=Break
7	galeːlin	_	VERB	V2	Gender=Fem|Number=Sing|VerbClass=2	8	parataxis:obj	_	AlignBegin=14938|AlignEnd=15244|GE=drive_cattle-[IMP].[SG].[F]-[EMPH]|Gloss=drive_cattle|MGloss=drive_cattle-IMP.SG.F-EMPH|MSeg=galeːl-i-n|ReportedSpeech=Yes|RX=[V2]-[TAM].[PNG]-[SUFX]|TokenType=Stem
8	idi	_	VERB	V1, IRG	Aspect=Pfv|Gender=Masc|Number=Sing|VerbClass=1	0	root	_	AlignBegin=15244|AlignEnd=15551|GE=[3SG].[M]-say\[PFV]|Gloss=say|MGloss=3SG.M-say\PFV|MSeg=i-di|RX=[PNG]-[V1].[IRG]|TokenType=Stem
9	ini	_	VERB	V1, IRG	Aspect=Pfv|Gender=Masc|Number=Sing|VerbClass=1	8	discourse	_	AlignBegin=15551|AlignEnd=15857|GE=[3SG].[M]-say\[PFV]|Gloss=say|MGloss=3SG.M-say\PFV|MSeg=i-ni|RX=[PNG]-[V1].[IRG]|TokenType=Stem
10	//	_	PUNCT	PUNCT	_	8	punct	_	AlignBegin=15857|AlignEnd=16164|TokenType=Break
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_beja3_Gender >}}
 


