---
title: "comp:aux"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# comp:aux

{{< expand >}}
{{< hint warning >}}
L'idée serait de pouvoir mettre des conll ici par exemple. Ou dans des tables. 
{{< /hint >}}
{{< /expand >}}

## Universal
The `comp:aux` relation is used for the argument of auxiliaries, and corresponds to the `aux` relationship as defined by UD.


> The relation `comp:aux` can have these features:
> * [@tense](../../Deep/tense.md)
> * [@pass](../../Deep/pass.md)
> * [@caus](../../Deep/caus.md)


> pattern { GOV-[comp:aux]->DEP }

{{< tabs "uniqueid" >}}
{{< tab "English" >}}
{{< hint info >}}
L'idée serait de pouvoir mettre des conll ici par exemple. Ou dans des tables. 
{{< /hint >}}{{< /tab >}}
{{< tab "English" >}}
{{< hint warning >}}
La page serait plus lisible.  
{{< /hint >}}{{< /tab >}}
{{< /tabs >}}
  
> English

{{< conll >}}
1	Do	do	AUX	_	_	0	root	_	_
2	you	you	PRON	_	_	1	subj	_	_
3	remember	remember	VERB	_	_	1	comp:aux	_	_
4	?	?	PUNCT	_	_	1	punct	_	_
{{< /conll >}}


> English

{{< conll >}}
1	It	it	PRON	_	_	2	subj	_	_
2	had	had	AUX	_	_	0	root	_	_
3	nearly	nearly	ADV	_	_	4	mod	_	_
4	stopped	stop	VERB	_	_	2	comp:aux	_	_
5	raining	rain	VERB	_	_	4	comp:pred	_	_
6	.	.	PUNCT	_	_	2	punct	_	_
{{< /conll >}}


Multiple auxiliaries, such as those permitted in [English varieties spoken in the Southeastern United States](https://en.wikipedia.org/wiki/Southern_American_English), are annotated as so.

> Southern American English

{{< conll >}}
# text_en = We might be able to go.
1	We	we	PRON	_	_	2	subj	_	_
2	might	may	AUX	_	_	0	root	_	_
3	could	can	AUX	_	_	2	comp:aux	_	_
4	go	go	VERB	_	_	3	comp:aux	_	_
5	.	.	PUNCT	_	_	2	punct	_	_
{{< /conll >}}


> Naija

{{< conll >}}
# text_en = I can't even sleep.
1	I	I	PRON	_	Case=Nom|Number=Sing|Person=1|PronType=Prs	3	subj	_	Gloss=I
2	no	no	PART	_	Polarity=Neg	3	mod	_	Gloss=not
3	dey	dey	AUX	_	Aspect=Imp	0	root	_	Gloss=IMPV
4	fit	fit	AUX	_	Mood=Pot	3	comp:aux	_	Gloss=can
5	sleep	sleep	VERB	_	_	4	comp:aux	_	Gloss=sleep
{{< /conll >}}


> Slovak

{{< conll >}}
# text_en = If I had a similar chance, I wouldn't waste it
# text_sk = Ak by som mal podobnú šancu, ja ju nepremrhám.
1	Ak	ak	SCONJ	_	_	10	mod	_	Gloss=if
2	by	by	AUX	_	_	1	comp:obj	_	Gloss=AUX.cond
3	som	byť	AUX	_	_	2	comp:aux	_	Gloss=am
4	mal	mať	VERB	_	_	3	comp:aux	_	Gloss=had
5	podobnú	podobný	ADJ	_	_	6	mod	_	Gloss=similar
6	šancu	šanca	NOUN	_	_	4	comp:obj	_	Gloss=chance
7	,	,	PUNCT	_	_	1	punct	_	_
8	ja	ja	PRON	_	_	10	subj	_	Gloss=I
9	ju	on	PRON	_	_	10	comp:obj	_	Gloss=it
10	nepremrhám	premrhať	VERB	_	_	0	root	_	Gloss=not waste
{{< /conll >}}


> Wolof

{{< conll >}}
# text_en = Every man that is missing is punished (for you)
# text_wo = Képp ku wuute dees na la mbugal.
1	Képp	képp	PRON	PRON	NounClass=Wol1|Number=Sing|Person=3|PronType=Tot	5	dislocated	_	Gloss=every_man
2	ku	bu	PRON	PRON	NounClass=Wol1|Number=Sing|Person=3|PronType=Rel	3	subj	_	Gloss=who
3	wuute	wuute	VERB	VERB	Mood=Ind|VerbForm=Fin	1	mod@relcl	_	Gloss=be_missing
4	dees	di	AUX	AUX	Aspect=Imp|Mood=Ind|Person=0|Tense=Pres	5	comp:aux	_	Gloss=IMP.IPRS
5	na	na	AUX	INFL	Aspect=Perf|Mood=Ind|Number=Sing|Person=3	0	root	_	Gloss=VFOC
6	la	ko	PRON	CL	Case=Acc|Number=Sing|Person=2|PronType=Prs	7	comp:obj	_	Gloss=O.2.SG
7	mbugal	mbugal	VERB	VERB	Mood=Ind|VerbForm=Fin	4	comp:aux	_	Gloss=punish
{{< /conll >}}


> German

{{< conll >}}
# text_en = It was agreed with the group of investors not to disclose any information.
1	Mit	Mit	ADP	APPR	AdpType=Prep|Case=Dat	4	udep	_	Gloss=with
2	der	der	DET	ART	Case=Dat|Gender=Fem|Number=Sing|PronType=Art	3	det	_	Gloss=the
3	Investorengruppe	Gruppe	NOUN	NN	Gender=Fem|Number=Sing|Person=3	1	comp:obj	_	Gloss=investors_group
4	sei	sein	AUX	VAFIN	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=was (past)
5	Stillschweigen	Schweigen	NOUN	NN	Gender=Neut|Number=Sing|Person=3	4	subj@pass	_	Gloss=non-disclosure
6	vereinbart	vereinbaren	VERB	VVPP	Aspect=Perf|VerbForm=Part	7	comp:aux@pass	_	Gloss=agreed
7	worden	werden	AUX	VAPP	Aspect=Perf|VerbForm=Part	4	comp:aux	_	Gloss=was (pass.)
8	.	.	PUNCT	.	PunctType=Peri	4	punct	_	Gloss=PUNCT
{{< /conll >}}



## French 

In French, the `comp:aux` relations is always between an `AUX`(the governer) and an other `AUX` or a `VERB`. When there are disfluencies, the relations can be between an `AUX` and an unknown node (upos=`X`). 

The ̀`comp:aux` relation always has a `deep` : 
- `tense` : expressing a tense construction
- `pass` :  expressing a passive construction
- `caus` :  expressing a causative construction

The [`comp:aux`](../../Syntactic_relations/comp/comp_aux.md) relation can be used with one of the three sub-relations [`@tense`](../../Deep/tense.md), [`@pass`](../../Deep/pass.md) or [`@caus`](../../Deep/caus.md), depending on whether the auxiliary is expressing a tense, a passive or a causative construction. In French, the relation [`comp:aux@tense`](../../Syntactic_relations/comp/comp_aux.md#auxilary-expressing-a-tense) is used with both verbs **être** and **avoir** and is the most common sub-relation. The relation [`comp:aux@pass`](../../Syntactic_relations/comp/comp_aux.md#passive-construction) is only used with the verb **être** and **se voir**, while [`comp:aux@caus`](../../Syntactic_relations/comp/comp_aux.md#causative-construction) is only used with the verb **faire**.

### **auxilary expressing a tense**
{{< conll >}}
# text_en = She has disappeared.
1	elle	il	PRON	_	Gender=Fem|Number=Sing|Person=3|PronType=Prs	2	subj	_	Gloss=she
2	a	avoir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=has
3	disparu	disparaître	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	2	comp:aux@tense	_	Gloss=disappeared
{{< /conll >}}

> pattern { GOV-[comp:aux@tense]->DEP }  

### **passive construction**

{{< conll >}}
# text_en = The castle is then sold.
1	Le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	Gloss=the
2	château	château	NOUN	_	Gender=Masc|Number=Sing	3	subj@pass	_	Gloss=castle
3	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=is
4	ensuite	ensuite	ADV	_	_	3	mod	_	Gloss=next
5	vendu	vendre	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	3	comp:aux@pass	_	Gloss=sold
{{< /conll >}}

> pattern { GOV-[comp:aux@pass]->DEP }   

### **causative construction**
{{< conll >}}
# text_en = He makes it fall.
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@caus	_	Gloss=he
2	le	le	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	comp:obj@agent	_	Gloss=it
3	fait	faire	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=makes
4	tomber	tomber	VERB	_	VerbForm=Inf	3	comp:aux@caus	_	Gloss=fall
{{< /conll >}}
 
> pattern { GOV-[comp:aux@caus]->DEP }  


### Table of comp:aux


{{< agg aux-french >}}

## french

### Overview

 In French, the `[comp:aux](docs/general_guideline/Syntactic_relations/comp/comp_aux.md)` relations is always between an `[AUX](docs/general_guideline/Upos/AUX.md)`(the governer) and an other `[AUX](docs/general_guideline/Upos/AUX.md)` or a `[VERB](docs/general_guideline/Upos/VERB.md)`. When there are disfluencies, the relations can be between an `[AUX](docs/general_guideline/Upos/AUX.md)` and an unknown node (upos=`[X](docs/general_guideline/Upos/X.md)`). 

The  [comp:aux](docs/general_guideline/Syntactic_relations/comp/comp_aux.md)  relation always has a `deep` : 
- [tense](docs/general_guideline/Deep/tense.md) : expressing a [tense](docs/general_guideline/Deep/tense.md) construction
- [pass](docs/general_guideline/Deep/pass.md) :  expressing a [pass](docs/general_guideline/Deep/pass.md)ive construction
- [caus](docs/general_guideline/Deep/caus.md) :  expressing a [caus](docs/general_guideline/Deep/caus.md)ative construction

{{< conll >}} 
# text_en = She has disappeared.
1	elle	il	PRON	_	Gender=Fem|Number=Sing|Person=3|PronType=Prs	2	subj	_	Gloss=she
2	a	avoir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=has
3	disparu	disparaître	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	2	comp:aux@tense	_	Gloss=disappeared
{{< /conll >}}

 The upos [AUX](docs/general_guideline/Upos/AUX.md) has the values : ['[AUX](docs/general_guideline/Upos/AUX.md)', '[VERB](docs/general_guideline/Upos/VERB.md)']


### Specific Pattern

#### Auxiliary expressing a [tense](docs/general_guideline/Deep/tense.md) 

- Pattern: GOV-[comp:aux@tense]->DEP


- Description:  In French, the relation [comp:aux](docs/general_guideline/Syntactic_relations/comp/comp_aux.md)@[tense](docs/general_guideline/Deep/tense.md) is used with both verbs **être** and **avoir** and is the most common sub-relation. 

{{< conll >}}
# text_en = She has disappeared.
1	elle	il	PRON	_	Gender=Fem|Number=Sing|Person=3|PronType=Prs	2	subj	_	Gloss=she
2	a	avoir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=has
3	disparu	disparaître	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	2	comp:aux@tense	_	Gloss=disappeared
{{< /conll >}}


#### [pass](docs/general_guideline/Deep/pass.md)ive construction 

- Pattern: GOV-[comp:aux@pass]->DEP


- Description: The relation [comp:aux](docs/general_guideline/Syntactic_relations/comp/comp_aux.md)@[pass](docs/general_guideline/Deep/pass.md) is only used with the verb **être** and **se voir**.

{{< conll >}}
# text_en = The castle is then sold.
1	Le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	Gloss=the
2	château	château	NOUN	_	Gender=Masc|Number=Sing	3	subj@pass	_	Gloss=castle
3	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=is
4	ensuite	ensuite	ADV	_	_	3	mod	_	Gloss=next
5	vendu	vendre	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	3	comp:aux@pass	_	Gloss=sold
{{< /conll >}}

#### [caus](docs/general_guideline/Deep/caus.md)ative construction 

- Pattern: GOV-[comp:aux@caus]->DEP


- Description: The relation [comp:aux](docs/general_guideline/Syntactic_relations/comp/comp_aux.md)@cas is only used with the aux **faire** .

{{< conll >}}
# text_en = He makes it fall.
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@caus	_	Gloss=he
2	le	le	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	comp:obj@agent	_	Gloss=it
3	fait	faire	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=makes
4	tomber	tomber	VERB	_	VerbForm=Inf	3	comp:aux@caus	_	Gloss=fall
{{< /conll >}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_comp_aux >}}




## french

### Overview

 test for conll

{{<conll>}} 
# text_en = He makes it fall.
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@caus	_	Gloss=he
2	le	le	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	comp:obj@agent	_	Gloss=it
3	fait	faire	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=makes
4	tomber	tomber	VERB	_	VerbForm=Inf	3	comp:aux@caus	_	Gloss=fall
{{</conll>}}

### Specific Pattern

#### test one 

- Description: test

- Pattern: GOV[Number]


{{<conll>}}
# text_en = He makes it fall.
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@caus	_	Gloss=he
2	le	le	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	comp:obj@agent	_	Gloss=it
3	fait	faire	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=makes
4	tomber	tomber	VERB	_	VerbForm=Inf	3	comp:aux@caus	_	Gloss=fall
{{</conll>}}

#### causative test two 

- Description: test 2

- Pattern: GOV[Gender]


{{<conll>}}
# text_en = He makes it fall.
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@caus	_	Gloss=he
2	le	le	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	comp:obj@agent	_	Gloss=it
3	fait	faire	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=makes
4	tomber	tomber	VERB	_	VerbForm=Inf	3	comp:aux@caus	_	Gloss=fall
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_comp_aux >}}






## bedja

TODO
### Overview

### Specific Pattern


