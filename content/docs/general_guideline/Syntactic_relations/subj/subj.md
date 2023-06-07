---
title: "subj"
weight: 3
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# The `subj` relation 


## Universal

The `subj` relation is used for all subjects, regardless of their form (nominal or verbal). This relationship encompasses both the `nsubj` and `csubj` relationships as defined by UD, as the following examples show.

> English

{{< conll >}}
      1	A	a	DET	_	_	2	det	_	_
      2	man	man	NOUN	_	_	3	subj	_	_
      3	walks	walk	VERB	_	_	0	root	_	_
{{< /conll >}}

### Deep syntactic features

The `subj` relation has two deep syntactic sub-relations. The sub-relation `subj@expl` is used to indicate that the subject is present to fill in an obligatory syntactic position and has no semantic value. You can find more information about the expletive constructions on this [page](../../Deep/expletiv.md).

> French

{{< conll >}}
      # sent_fr = Il pleut dans ma maison
      # text_en = It's raining in my house
      1	Il	il	PRON	_	_	2	subj@expl	_	Gloss=it
      2	pleut	pleuvoir	VERB	_	_	0	root	_	Gloss=rains
      3	dans	dans	ADP	_	_	2	mod	_	Gloss=in
      4	ma	son	DET	_	_	5	det	_	Gloss=my
      5	maison	maison	NOUN	_	_	3	comp:obj	_	Gloss=house
{{< /conll >}}

Meanwhile, the sub-relation `subj@pass` is used to indicate a passive construction. This sub-relation can be used for both standard passive constructions, and for mediopassive constructions.
You can find more information about passive constructions on this [page](../../Deep/pass.md).

#### Passive constructions

> English

{{< conll >}}
      # text = This shall be applauded
      1	This	this	PRON	DT	Number=Sing|PronType=Dem	2	subj@pass	_	Entity=(event-70)
      2	shall	shall	AUX	MD	VerbForm=Fin	0	root	_	_
      3	be	be	AUX	VB	VerbForm=Inf	2	comp:aux	_	_
      4	applauded	applaud	VERB	VBD	Mood=Ind|Tense=Past|VerbForm=Fin	3	comp:aux@pass	_	_
{{< /conll >}}


> French

{{< conll >}}
      # text = Il fut bâti en 1998.
      # text_en = It was build in 1998.
      1	Il	il	PRON	_	_	2	subj@pass	_	Gloss=It
      2	fut	être	AUX	_	_	0	root	_	Gloss=was
      3	bâti	bâtir	VERB	_	_	2	comp:aux@pass	_	Gloss=built
      4	en	en	ADP	_	_	2	mod	_	Gloss=in
      5	1998	1998	NUM	_	_	4	comp:obj	_	Gloss=1998
{{< /conll >}}

#### Mediopassive constructions

> Czech

{{< conll >}}
      # text_en = the number of employees decreased
      # text_cs = počet zaměstnanců se snížil
      1	počet	počet	NOUN	_	_	4	subj@pass	_	Gloss=number
      2	zaměstnanců	zaměstnanec	NOUN	_	_	1	mod	_	Gloss=employees.PL.GEN
      3	se	se	PRON	_	_	4	comp@pass	_	Gloss=itself
      4	snížil	snížit	VERB	_	_	0	root	_	Gloss=decrease
{{< /conll >}}

> French

{{< conll >}}
      # text_en = the book is selling well
      # text_cs = le livre se vend bien
      1	le	le	DET	_	_	2	det	_	Gloss=the
      2	livre	livre	NOUN	_	_	4	subj@pass	_	Gloss=book
      3	se	se	PRON	_	_	4	comp@pass	_	Gloss=itself
      4	vend	vendre	VERB	_	_	0	root	_	Gloss=sell
      5	bien	bien	ADV	_	_	4	mod	_	Gloss=well
{{< /conll >}}

> Russian

{{< conll >}}
      # text_en = the book is selling well
      # text_ru = книга хорошо продаётся
      1	книга	книга	NOUN	_	_	3	subj@pass	_	Gloss=book
      2	хорошо	хорошо	ADV	_	_	3	mod	_	Gloss=well
      3	продаётся	продаваться	VERB	_	_	0	root	_	Gloss=is selling
{{< /conll >}}






## french

### Overview

  The [subj](docs/general_guideline/Syntactic_relations/subj/subj.md) in french is usualy between a [VERB](docs/general_guideline/Upos/VERB.md) or anAUX (often the root) and a nominal group ([NOUN](docs/general_guideline/Upos/NOUN.md), [PROPN](docs/general_guideline/Upos/PROPN.md) or [PRON](docs/general_guideline/Upos/PRON.md)). You can see all the pattern in this table. In french, we can have three deep syntactic sub-relations :

@[pass](docs/general_guideline/Deep/pass.md) :  expressing a passiv subject
@expl : expressing an [expletiv](docs/general_guideline/Deep/expletiv.md) subject
@[caus](docs/general_guideline/Deep/caus.md) :: expressing a causative construction

{{<conll>}} 
# text = L'œuvre est située dans la galerie des batailles, dans le château de Versailles.
1	L'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	2	det	_	SpaceAfter=No|wordform=l'
2	œuvre	œuvre	NOUN	_	Gender=Fem|Number=Sing	3	subj	_	_
3	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	située	situer	VERB	_	Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	3	comp:pred	_	_
5	dans	dans	ADP	_	_	4	comp:obl	_	_
6	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	7	det	_	_
7	galerie	galerie	NOUN	_	Gender=Fem|Number=Sing	5	comp:obj	_	_
8-9	des	_	_	_	_	_	_	_	_
8	de	de	ADP	_	_	7	udep	_	_
9	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	10	det	_	_
10	batailles	bataille	NOUN	_	Gender=Fem|Number=Plur	8	comp:obj	_	SpaceAfter=No
11	,	,	PUNCT	_	_	12	punct	_	_
12	dans	dans	ADP	_	_	4	comp:obl	_	_
13	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	14	det	_	_
14	château	château	NOUN	_	Gender=Masc|Number=Sing	12	comp:obj	_	_
15	de	de	ADP	_	_	14	udep	_	_
16	Versailles	Versailles	PROPN	_	_	15	comp:obj	_	SpaceAfter=No
17	.	.	PUNCT	_	_	3	punct	_	_
{{</conll>}}

 The upos [[VERB](docs/general_guideline/Upos/VERB.md)](docs/general_guideline/Upos/[VERB](docs/general_guideline/Upos/VERB.md).md) has the values : ['[[NUM](docs/general_guideline/Upos/NUM.md)](docs/general_guideline/Upos/[NUM](docs/general_guideline/Upos/NUM.md).md)', '[[PROPN](docs/general_guideline/Upos/PROPN.md)](docs/general_guideline/Upos/[PROPN](docs/general_guideline/Upos/PROPN.md).md)', '[[PRON](docs/general_guideline/Upos/PRON.md)](docs/general_guideline/Upos/[PRON](docs/general_guideline/Upos/PRON.md).md)', '[[NOUN](docs/general_guideline/Upos/NOUN.md)](docs/general_guideline/Upos/[NOUN](docs/general_guideline/Upos/NOUN.md).md)']


 The upos [AUX](docs/general_guideline/Upos/AUX.md) has the values : ['[NUM](docs/general_guideline/Upos/NUM.md)', '[NOUN](docs/general_guideline/Upos/NOUN.md)', '[PROPN](docs/general_guideline/Upos/PROPN.md)', '[PRON](docs/general_guideline/Upos/PRON.md)']


### Specific Pattern

#### passive subject 

- Description: Exemple of a passiv subject in french.

- Pattern: GOV-[subj@pass]->DEP


{{<conll>}}
1	Le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	2	det	_	wordform=le
2	château	château	NOUN	_	Gender=Masc|Number=Sing	3	subj@pass	_	_
3	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	ensuite	ensuite	ADV	_	_	3	mod	_	_
5	vendu	vendre	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	3	comp:aux@pass	_	_
6	plusieurs	plusieurs	DET	_	Number=Plur|PronType=Ind	7	det	_	_
7	fois	fois	NOUN	_	Gender=Fem|Number=Plur	3	mod	_	_
8	;	;	PUNCT	_	_	3	punct	_	_

{{</conll>}}

#### causativ subject 

- Description: Exemple of a causativ subject in french.

- Pattern: GOV-[subj@caus]->DEP


{{<conll>}}
# text = et donc, je le fais même rentrer dans la maison.
1	et	et	CCONJ	_	_	6	cc	_	AlignBegin=60484|AlignEnd=60615
2	donc	donc	ADV	_	_	6	mod	_	AlignBegin=60615|AlignEnd=60745|SpaceAfter=No
3	,	,	PUNCT	_	_	2	punct	_	AlignBegin=60745|AlignEnd=60745
4	je	moi	PRON	_	Number=Sing|Person=1|PronType=Prs	6	subj@caus	_	AlignBegin=61067|AlignEnd=61234
5	le	lui	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	6	comp:obj@agent	_	AlignBegin=61234|AlignEnd=61402
6	fais	faire	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	AlignBegin=61402|AlignEnd=61569
7	même	même	ADV	_	_	6	mod	_	AlignBegin=61569|AlignEnd=61737
8	rentrer	rentrer	VERB	_	VerbForm=Inf	6	comp:aux@caus	_	AlignBegin=61737|AlignEnd=61904|Subject=ObjRaising
9	dans	dans	ADP	_	_	8	comp:obl	_	AlignBegin=61904|AlignEnd=62071
10	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	11	det	_	AlignBegin=62071|AlignEnd=62239
11	maison	maison	NOUN	_	Gender=Fem|Number=Sing	9	comp:obj	_	AlignBegin=62239|AlignEnd=62406|SpaceAfter=No
12	.	.	PUNCT	_	_	6	punct	_	AlignBegin=62406|AlignEnd=62406
{{</conll>}}

#### [expletiv](docs/general_guideline/Deep/expletiv.md) subject 

- Description: Exemple of an [expletiv](docs/general_guideline/Deep/expletiv.md) subject in french.

- Pattern: GOV-[subj@expl]->DEP


{{<conll>}}
# text = il y avait Maxime aussi, pas mal.
1	il	lui	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@expl	_	AlignBegin=12306|AlignEnd=12621
2	y	y	PRON	_	Person=3|PronType=Prs	3	comp@expl	_	AlignBegin=12621|AlignEnd=12935
3	avait	avoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	AlignBegin=12935|AlignEnd=13249
4	Maxime	Maxime	PROPN	_	_	3	comp:obj	_	AlignBegin=13249|AlignEnd=13563
5	aussi	aussi	ADV	_	_	4	mod	_	AlignBegin=13563|AlignEnd=13878|SpaceAfter=No
6	,	,	PUNCT	_	_	8	punct	_	AlignBegin=13878|AlignEnd=13878
7	pas	pas	ADV	_	_	8	mod	_	AlignBegin=13878|AlignEnd=14192
8	mal	mal	ADV	_	Gender=Masc|Number=Sing	4	mod	_	AlignBegin=14192|AlignEnd=14506|SpaceAfter=No
9	.	.	PUNCT	_	_	3	punct	_	AlignBegin=14506|AlignEnd=14506
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_subj >}}
 
