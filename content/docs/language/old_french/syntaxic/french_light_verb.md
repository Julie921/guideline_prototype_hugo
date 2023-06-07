# Complement of light verb construction

The complement of a `VERB -[comp:obj@lvc]-> OBJ` construction is attached to **OBJ** if it can be considered independently of VERB, otherwise it is attached to **VERB**.

Examples : 
- j'ai peur de mourir (I'm afraid to die) - la peur de mourir me hante (the fear of dying haunts me)
peur -[comp:obl]-> de

{{< conll >}}
# text = j'avais la réputation d'être très doué.
1	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	SpaceAfter=No
2	avais	avoir	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin	0	root	_	_
3	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	4	det	_	_
4	réputation	réputation	NOUN	_	Gender=Fem|Number=Sing	2	comp:obj@lvc	_	_
5	d'	de	ADP	_	_	4	comp:obl	_	SpaceAfter=No
6	être	être	AUX	_	VerbForm=Inf	5	comp:obj	_	Subject=SubjRaising
7	très	très	ADV	_	_	8	mod	_	_
8	doué	doué	ADJ	_	Gender=Masc|Number=Sing	6	comp:pred	_	SpaceAfter=No
9	.	.	PUNCT	_	_	2	punct	_	_
{{< /conll >}}

- Je me rends compte de mon erreur (I realize my mistake )
rends -[comp:obl]-> de

{{< conll >}}
# text = Il fait partie de la section de Nobressart.
1	Il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj	_	wordform=il
2	fait	faire	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	partie	partie	NOUN	_	Gender=Fem|Number=Sing	2	comp:obj@lvc	_	_
4	de	de	ADP	_	_	2	comp:obl	_	_
5	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	6	det	_	_
6	section	section	NOUN	_	Gender=Fem|Number=Sing	4	comp:obj	_	_
7	de	de	ADP	_	_	6	udep	_	_
8	Nobressart	Nobressart	PROPN	_	_	7	comp:obj	_	SpaceAfter=No
9	.	.	PUNCT	_	_	2	punct	_	_
{{< /conll >}}

{{< hint info >}}
You can find more information about this decisions [here](https://github.com/surfacesyntacticud/guidelines/issues/5)
{{< /hint >}}