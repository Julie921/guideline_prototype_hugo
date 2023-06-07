## french

### Overview

 The [subj](docs/general_guideline/Syntactic_relations/subj/subj.md) in french is usualy between a [VERB](docs/general_guideline/Upos/VERB.md) or an [AUX](docs/general_guideline/Upos/AUX.md) (often the root) and a nominal group ( [PRON](docs/general_guideline/Upos/PRON.md), [PROPN](docs/general_guideline/Upos/PROPN.md) or [NOUN](docs/general_guideline/Upos/NOUN.md)). You can see all the pattern in this table. In french, we can have three deep syntactic sub-relations :

@ [pass](docs/general_guideline/Deep/pass.md) : expressing a passiv subject
@expl : expressing an [expletiv](docs/general_guideline/Deep/expletiv.md) subject
@ [caus](docs/general_guideline/Deep/caus.md) : expressing a causative construction

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

 The upos [[AUX](docs/general_guideline/Upos/AUX.md)](docs/general_guideline/Upos/[AUX](docs/general_guideline/Upos/AUX.md).md) has the values : ['[[PROPN](docs/general_guideline/Upos/PROPN.md)](docs/general_guideline/Upos/[PROPN](docs/general_guideline/Upos/PROPN.md).md)', '[[NOUN](docs/general_guideline/Upos/NOUN.md)](docs/general_guideline/Upos/[NOUN](docs/general_guideline/Upos/NOUN.md).md)', '[[NUM](docs/general_guideline/Upos/NUM.md)](docs/general_guideline/Upos/[NUM](docs/general_guideline/Upos/NUM.md).md)', '[[PRON](docs/general_guideline/Upos/PRON.md)](docs/general_guideline/Upos/[PRON](docs/general_guideline/Upos/PRON.md).md)']


 The upos [VERB](docs/general_guideline/Upos/VERB.md) has the values : ['[PROPN](docs/general_guideline/Upos/PROPN.md)', '[PRON](docs/general_guideline/Upos/PRON.md)', '[NOUN](docs/general_guideline/Upos/NOUN.md)', '[NUM](docs/general_guideline/Upos/NUM.md)']


### Specific Pattern

#### causative construction 

- Description: The deep tag @[caus](docs/general_guideline/Deep/caus.md) express an causativ subject here. 

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

#### passive construction 

- Description: The deep tag @[pass](docs/general_guideline/Deep/pass.md) express a passiv subject here. 

- Pattern: GOV-[subj@pass]->DEP


{{<conll>}}
# text = ça a été organisé par le prof.
1	ça	ça	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	2	subj@pass	_	AlignBegin=49795|AlignEnd=49995
2	a	avoir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	AlignBegin=49995|AlignEnd=50194
3	été	être	AUX	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	2	comp:aux@tense	_	AlignBegin=50194|AlignEnd=50394
4	organisé	organiser	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	3	comp:aux@pass	_	AlignBegin=50394|AlignEnd=50593
5	par	par	ADP	_	_	4	comp:obl@agent	_	AlignBegin=50593|AlignEnd=50793
6	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	7	det	_	AlignBegin=50793|AlignEnd=50992
7	prof	prof	NOUN	_	Gender=Masc|Number=Sing	5	comp:obj	_	AlignBegin=50992|AlignEnd=51192|CorrectForm=profs|CorrectNumber=Plur|SpaceAfter=No
8	.	.	PUNCT	_	_	2	punct	_	AlignBegin=51192|AlignEnd=5119
{{</conll>}}

#### expletive construction 

- Description: The deep tag @expl express an expletive subject here. 

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
