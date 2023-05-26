## french

### Overview

 The [subj](docs/general_guideline/Syntactic_relations/subj/subj.md) in french is usualy between a [VERB](docs/general_guideline/Upos/VERB.md) or an [AUX](docs/general_guideline/Upos/AUX.md) (often the root) and a nominal group ([PRON](docs/general_guideline/Upos/PRON.md), [PROPN](docs/general_guideline/Upos/PROPN.md) or [NOUN](docs/general_guideline/Upos/NOUN.md)). You can see all the pattern in this table. In french, we can have three deep syntactic sub-relations :
- @[pass](docs/general_guideline/Deep/pass.md) : expressing a passiv subject
- @expl : expressing an [expletiv](docs/general_guideline/Deep/expletiv.md) subject
- @[caus](docs/general_guideline/Deep/caus.md) : expressing a causative construction

{{<conll>}} 
# text = Plus de 80 sonates et trios ont été publiés.
1	Plus	plus	ADV	_	_	7	subj@pass	_	ExtPos=PRON|wordform=plus
2	de	de	ADP	_	_	1	comp:obl	_	_
3	80	80	NUM	_	Number=Plur|Shared=Yes	4	det	_	_
4	sonates	sonate	NOUN	_	Gender=Fem|Number=Plur	2	comp:obj	_	_
5	et	et	CCONJ	_	_	6	cc	_	_
6	trios	trio	NOUN	_	Gender=Masc|Number=Plur	4	conj:coord	_	_
7	ont	avoir	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
8	été	être	AUX	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	7	comp:aux@tense	_	_
9	publiés	publier	VERB	_	Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass	8	comp:aux@pass	_	SpaceAfter=No
10	.	.	PUNCT	_	_	7	punct	_	_
{{</conll>}}

 The upos [[AUX](docs/general_guideline/Upos/AUX.md)](docs/general_guideline/Upos/[AUX](docs/general_guideline/Upos/AUX.md).md) has the values : ['[[NUM](docs/general_guideline/Upos/NUM.md)](docs/general_guideline/Upos/[NUM](docs/general_guideline/Upos/NUM.md).md)', '[[NOUN](docs/general_guideline/Upos/NOUN.md)](docs/general_guideline/Upos/[NOUN](docs/general_guideline/Upos/NOUN.md).md)', '[[PROPN](docs/general_guideline/Upos/PROPN.md)](docs/general_guideline/Upos/[PROPN](docs/general_guideline/Upos/PROPN.md).md)', '[[PRON](docs/general_guideline/Upos/PRON.md)](docs/general_guideline/Upos/[PRON](docs/general_guideline/Upos/PRON.md).md)']


 The upos [VERB](docs/general_guideline/Upos/VERB.md) has the values : ['[NUM](docs/general_guideline/Upos/NUM.md)', '[PROPN](docs/general_guideline/Upos/PROPN.md)', '[PRON](docs/general_guideline/Upos/PRON.md)', '[NOUN](docs/general_guideline/Upos/NOUN.md)']


### Specific Pattern

#### passiv construction 

- Description: This deep express a passiv subject.

- Pattern: GOV-[subj@pass]->DEP


{{<conll>}}
# text = Il est fêté le 22 mai.
1	Il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj@pass	_	wordform=il
2	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	fêté	fêter	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	2	comp:aux@pass	_	_
4	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	5	det	_	_
5	22	22	NUM	_	Number=Sing	2	mod	_	_
6	mai	mai	NOUN	_	Gender=Masc|Number=Sing	5	mod	_	SpaceAfter=No
7	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

#### [expletiv](docs/general_guideline/Deep/expletiv.md) construction 

- Description: This deep express a [expletiv](docs/general_guideline/Deep/expletiv.md) subject.

- Pattern: GOV-[subj@expl]->DEP


{{<conll>}}
# text = mais il y a trop de gens aussi, euh.
1	mais	mais	CCONJ	_	_	4	cc	_	AlignBegin=94929|AlignEnd=95095
2	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	4	subj@expl	_	AlignBegin=95095|AlignEnd=95261
3	y	y	PRON	_	Person=3|PronType=Prs	4	comp@expl	_	AlignBegin=95261|AlignEnd=95426
4	a	avoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	AlignBegin=95426|AlignEnd=95592
5	trop	trop	ADV	_	_	4	comp:obj	_	AlignBegin=95592|AlignEnd=95758
6	de	de	ADP	_	_	5	comp:obl	_	AlignBegin=95758|AlignEnd=95924
7	gens	gens	NOUN	_	Gender=Masc|Number=Plur	6	comp:obj	_	AlignBegin=95924|AlignEnd=96089
8	aussi	aussi	ADV	_	_	4	mod	_	AlignBegin=96089|AlignEnd=96255|SpaceAfter=No
9	,	,	PUNCT	_	_	10	punct	_	AlignBegin=96255|AlignEnd=96255
10	euh	euh	INTJ	_	_	7	discourse	_	AlignBegin=96255|AlignEnd=96421|SpaceAfter=No
11	.	.	PUNCT	_	_	4	punct	_	AlignBegin=96421|AlignEnd=96421
{{</conll>}}

#### causativ construction 

- Description: This deep express a causativ subject.

- Pattern: GOV-[subj@expl]->DEP


{{<conll>}}
# text = Il fait observer à Pierre le Grand la circulation sanguine.
1	Il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj@caus	_	wordform=il
2	fait	faire	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	observer	observer	VERB	_	VerbForm=Inf	2	comp:aux@caus	_	Subject=Generic
4	à	à	ADP	_	_	3	comp:obl	_	_
5	Pierre	Pierre	PROPN	_	_	4	comp:obj	_	_
6	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	7	det	_	_
7	Grand	Grand	PROPN	_	Gender=Masc|Number=Sing	5	conj:appos	_	_
8	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	9	det	_	_
9	circulation	circulation	NOUN	_	Gender=Fem|Number=Sing	3	comp:obj	_	_
10	sanguine	sanguin	ADJ	_	Gender=Fem|Number=Sing	9	mod	_	_
11	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

#### nominal subject 

- Description: The [subj](docs/general_guideline/Syntactic_relations/subj/subj.md) syntactic relation is usually between a [AUX](docs/general_guideline/Upos/AUX.md) or a [VERB](docs/general_guideline/Upos/VERB.md) (as a governor) and a [NOUN](docs/general_guideline/Upos/NOUN.md), [PRON](docs/general_guideline/Upos/PRON.md), [PROPN](docs/general_guideline/Upos/PROPN.md) or a [NUM](docs/general_guideline/Upos/NUM.md) (as a dependant).

- Pattern: GOV-[1=subj]->DEP; DEP[upos=NOUN|PROPN|PRON|NUM,!Title, !InTitle]; GOV [upos=AUX|VERB]


{{<conll>}}
# text = Elle lutte pour échapper aux tueurs à ses trousses.
1	Elle	lui	PRON	_	Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs	2	subj	_	wordform=elle
2	lutte	lutter	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	pour	pour	ADP	_	_	2	mod	_	_
4	échapper	échapper	VERB	_	VerbForm=Inf	3	comp:obj	_	Subject=SubjRaising
5-6	aux	_	_	_	_	_	_	_	_
5	à	à	ADP	_	_	4	comp:obl	_	_
6	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	7	det	_	_
7	tueurs	tueur	NOUN	_	Gender=Masc|Number=Plur	5	comp:obj	_	_
8	à	à	ADP	_	_	4	mod	_	_
9	ses	son	DET	_	Number=Plur|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs	10	det	_	_
10	trousses	trousses	NOUN	_	Gender=Fem|Number=Plur	8	comp:obj	_	SpaceAfter=No
11	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

#### title as a subject 

- Description: When the subject is a title, we can have any of the SUD part of speech.

- Pattern: GOV-[1=subj]->DEP; DEP [Title=Yes/InTitle=Yes]; GOV [upos=AUX|VERB]


{{<conll>}}
# text = Prenons comme exemple le syntagme « Vous fumez ?
1	Prenons	prendre	VERB	_	Mood=Imp|Number=Plur|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	wordform=prenons
2	comme	comme	ADP	_	_	1	mod	_	_
3	exemple	exemple	NOUN	_	Gender=Masc|Number=Sing	2	comp:obj	_	_
4	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	5	det	_	_
5	syntagme	syntagme	NOUN	_	Gender=Masc|Number=Sing	1	comp:obj	_	_
6	«	«	PUNCT	_	_	8	punct	_	_
7	Vous	vous	PRON	_	Emph=No|Number=Plur|Person=2|PronType=Prs	8	subj	_	InTitle=Yes|wordform=vous
8	fumez	fumer	VERB	_	Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin	5	conj:appos	_	ExtPos=PROPN|Title=Yes
9	?	?	PUNCT	_	_	8	punct	_	InTitle=Yes
{{</conll>}}

#### VerbInf as a subject 

- Description: In French, a infinitive verb can also be a subject.

- Pattern: GOV-[1=subj]->DEP; GOV [upos=AUX|VERB] ; DEP [upos=VERB|AUX, VerbForm = Inf, !Title, !InTitle]


{{<conll>}}
# text = Manger le poisson pêché dans l'étang est un enchantement.
1	Manger	manger	VERB	_	VerbForm=Inf	8	subj	_	Subject=Generic|wordform=manger
2	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	3	det	_	_
3	poisson	poisson	NOUN	_	Gender=Masc|Number=Sing	1	comp:obj	_	_
4	pêché	pêcher	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	3	mod	_	_
5	dans	dans	ADP	_	_	4	mod	_	_
6	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	7	det	_	SpaceAfter=No
7	étang	étang	NOUN	_	Gender=Masc|Number=Sing	5	comp:obj	_	_
8	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
9	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	10	det	_	_
10	enchantement	enchantement	NOUN	_	Gender=Masc|Number=Sing	8	comp:pred	_	SpaceAfter=No
11	.	.	PUNCT	_	_	8	punct	_	_
{{</conll>}}

#### Adverb used as pronoun in french subject 

- Description: In French, an [ADV](docs/general_guideline/Upos/ADV.md) can be a subject. It is a specific phenomen due to the french language. The [ADV](docs/general_guideline/Upos/ADV.md) have an [ExtPos](docs/general_guideline/Misc/ExtPos.md)=[PRON](docs/general_guideline/Upos/PRON.md).

- Pattern: GOV-[1=subj]->DEP; GOV [upos=AUX|VERB] ; DEP [upos=ADV, ExtPos=PRON, !Title, !InTitle]


{{<conll>}}
# text = Plus de 80 sonates et trios ont été publiés.
1	Plus	plus	ADV	_	_	7	subj@pass	_	ExtPos=PRON|wordform=plus
2	de	de	ADP	_	_	1	comp:obl	_	_
3	80	80	NUM	_	Number=Plur|Shared=Yes	4	det	_	_
4	sonates	sonate	NOUN	_	Gender=Fem|Number=Plur	2	comp:obj	_	_
5	et	et	CCONJ	_	_	6	cc	_	_
6	trios	trio	NOUN	_	Gender=Masc|Number=Plur	4	conj:coord	_	_
7	ont	avoir	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
8	été	être	AUX	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	7	comp:aux@tense	_	_
9	publiés	publier	VERB	_	Gender=Masc|Number=Plur|Tense=Past|VerbForm=Part|Voice=Pass	8	comp:aux@pass	_	SpaceAfter=No
10	.	.	PUNCT	_	_	7	punct	_	_
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_subj >}}
