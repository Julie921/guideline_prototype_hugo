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

> [!NOTE]
> The relation `comp:aux` can have these features:
> * [@tense](../../deep_features/tense)
> * [@pass](../../deep_features/pass)
> * [@caus](../../deep_features/caus)

>[!tip]
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

### **auxilary expressing a tense**
{{< conll >}}
# text_en = She has disappeared.
1	elle	il	PRON	_	Gender=Fem|Number=Sing|Person=3|PronType=Prs	2	subj	_	Gloss=she
2	a	avoir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=has
3	disparu	disparaître	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	2	comp:aux@tense	_	Gloss=disappeared
{{< /conll >}}

>[!tip] 
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

>[!tip] 
> pattern { GOV-[comp:aux@pass]->DEP }   

### **causative construction**
{{< conll >}}
# text_en = He makes it fall.
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@caus	_	Gloss=he
2	le	le	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	comp:obj@agent	_	Gloss=it
3	fait	faire	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=makes
4	tomber	tomber	VERB	_	VerbForm=Inf	3	comp:aux@caus	_	Gloss=fall
{{< /conll >}}

>[!tip] 
> pattern { GOV-[comp:aux@caus]->DEP }  


### Table of comp:aux


{{< agg aux-french >}}



## Naija copula

