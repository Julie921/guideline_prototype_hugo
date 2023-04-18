---
title: "Parataxis"
weight: 3
# bookFlatSection: false
# bookToc: true
# bookHidden: false
bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# Parataxis 

## Universal 

The `parataxis` relation is used to analyse two elements that are placed side by side with no explicit marker of coordination, subordination, or argument relation with the head word. 

> pattern { GOV-[parataxis]->DEP }

In the **Spoken Corpora**, we distinguish :

   * [`parataxis:parenth`](./parataxis_parenth.md) for parenthetical clauses (that can form independent sentences)

   * [`parataxis:insert`](./parataxis_insert.md) for inserted clauses (that cannot form an independent sentence)

   * [`parataxis:obj`](./parataxis_obj.md) used before for attaching direct discourse. Now deleted. See [Reported Speech](../../../Particular_construction/reported_speech.md)

In the other corpora, we use the `parataxis` relation. There is no distinction. We there use the relation `parataxis` for incisive proposal indicating who reports.

### Incisive proposal 

> French
{{<conll>}}
# text = Il faudra encore du temps », avait-il déclaré.
1	Il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj@expl	_	wordform=il
2	faudra	falloir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin	0	root	_	_
3	encore	encore	ADV	_	_	2	mod	_	_
4	du	du	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	5	det	_	_
5	temps	temps	NOUN	_	Gender=Masc|Number=Sing	2	comp:obj	_	_
6	»	»	PUNCT	_	_	8	punct	_	SpaceAfter=No
7	,	,	PUNCT	_	_	8	punct	_	_
8	avait	avoir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	2	parataxis	_	SpaceAfter=No
9	-il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	8	subj	_	wordform=il
10	déclaré	déclarer	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	8	comp:aux@tense	_	SpaceAfter=No
11	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

> English
{{<conll>}}
# text = Kim couldn't spend the night, I told you.
1	Kim	Kim	PROPN	NNP	Number=Sing	2	subj	_	Discourse=explanation-evidence:34->32:2|Entity=(16-person-giv:inact-cf5-1-coref)
2-3	couldn't	_	_	_	_	_	_	_	_
2	could	could	AUX	MD	Number=Sing|Person=3|VerbForm=Fin	0	root	_	_
3	n't	not	PART	RB	Polarity=Neg	2	mod	_	_
4	spend	spend	VERB	VB	VerbForm=Inf	2	comp:aux	_	Entity=(17-event-giv:act-cf3-1-disc
5	the	the	DET	DT	Definite=Def|PronType=Art	6	det	_	Entity=(7-time-giv:act-cf2-2-coref
6	night	night	NOUN	NN	Number=Sing	4	comp:obj	_	Entity=7)17)|SpaceAfter=No
7	,	,	PUNCT	,	_	9	punct	_	_
8	I	I	PRON	PRP	Case=Nom|Number=Sing|Person=1|PronType=Prs	9	subj	_	Discourse=attribution-positive:35->34:0|Entity=(4-person-giv:act-cf1*-1-ana)
9	told	tell	VERB	VBD	Mood=Ind|Number=Sing|Person=1|Tense=Past|VerbForm=Fin	2	parataxis	_	_
10	you	you	PRON	PRP	Case=Acc|Number=Sing|Person=2|PronType=Prs	9	comp:obl	_	Entity=(10-person-giv:inact-cf4-1-ana)|SpaceAfter=No
11	.	.	PUNCT	.	_	2	punct	_	_
{{</conll>}}

### **Other example**

{{<conll>}}
# text = Très demandé, vous le connaissez sûrement, Jean M est toujours dévoué, un vrai professionnel qui ne compte pas ses heures pour nous soigner.
1	Très	très	ADV	_	_	2	mod	_	wordform=très
2	demandé	demander	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	11	mod	_	SpaceAfter=No|Subject=Instantiated
3	,	,	PUNCT	_	_	2	punct	_	_
4	vous	il	PRON	_	Number=Plur|Person=2|PronType=Prs	6	subj	_	_
5	le	le	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	6	comp:obj	_	_
6	connaissez	connaître	VERB	_	Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin	11	parataxis	_	_
7	sûrement	sûrement	ADV	_	_	6	mod	_	SpaceAfter=No
8	,	,	PUNCT	_	_	6	punct	_	_
9	Jean	Jean	PROPN	_	Gender=Masc|Number=Sing	11	subj	_	_
10	M	M	SYM	_	_	9	mod	_	ExtPos=PROPN
11	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
12	toujours	toujours	ADV	_	_	11	mod	_	_
13	dévoué	dévoué	ADJ	_	Gender=Masc|Number=Sing	11	comp:pred	_	SpaceAfter=No
14	,	,	PUNCT	_	_	17	punct	_	_
15	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	17	det	_	_
16	vrai	vrai	ADJ	_	Gender=Masc|Number=Sing	17	mod	_	_
17	professionnel	professionnel	NOUN	_	Gender=Masc|Number=Sing	9	appos	_	_
18	qui	qui	PRON	_	PronType=Rel	20	subj	_	_
19	ne	ne	ADV	_	Polarity=Neg	20	mod	_	_
20	compte	compter	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	17	mod@relcl	_	_
21	pas	pas	ADV	_	Polarity=Neg	20	mod	_	_
22	ses	son	DET	_	Number=Plur|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs	23	det	_	_
23	heures	heure	NOUN	_	Gender=Fem|Number=Plur	20	comp:obj	_	_
24	pour	pour	ADP	_	_	20	mod	_	_
25	nous	le	PRON	_	Number=Plur|Person=1|PronType=Prs	26	comp:obj	_	_
26	soigner	soigner	VERB	_	VerbForm=Inf	24	comp:obj	_	SpaceAfter=No|Subject=SubjRaising
27	.	.	PUNCT	_	_	11	punct	_	_
{{</conll>}}