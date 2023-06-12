## french

### Overview

 Test

{{<conll>}} 
# text = On ne peut éviter de penser à l'actualité caractérisée par l'enlèvement des otages au Niger--dont cinq Français.
1	On	on	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Ind	3	subj	_	wordform=on
2	ne	ne	ADV	_	Polarity=Neg	3	mod	_	_
3	peut	pouvoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	éviter	éviter	VERB	_	VerbForm=Inf	3	comp:obj	_	Subject=SubjRaising
5	de	de	ADP	_	_	4	comp:obj	_	_
6	penser	penser	VERB	_	VerbForm=Inf	5	comp:obj	_	Subject=SubjRaising
7	à	à	ADP	_	_	6	comp:obl	_	_
8	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	9	det	_	SpaceAfter=No
9	actualité	actualité	NOUN	_	Gender=Fem|Number=Sing	7	comp:obj	_	_
10	caractérisée	caractériser	VERB	_	Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	9	mod	_	_
11	par	par	ADP	_	_	10	comp:obl@agent	_	_
12	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	13	det	_	SpaceAfter=No
13	enlèvement	enlèvement	NOUN	_	Gender=Masc|Number=Sing	11	comp:obj	_	_
14-15	des	_	_	_	_	_	_	_	_
14	de	de	ADP	_	_	13	udep	_	_
15	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	16	det	_	_
16	otages	otage	NOUN	_	Gender=Masc|Number=Plur	14	comp:obj	_	_
17-18	au	_	_	_	_	_	_	_	_
17	à	à	ADP	_	_	13	udep	_	_
18	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	19	det	_	_
19	Niger	Niger	PROPN	_	Gender=Masc|Number=Sing	17	comp:obj	_	SpaceAfter=No
20	--	--	PUNCT	_	_	23	punct	_	SpaceAfter=No
21	dont	dont	PRON	_	PronType=Rel	23	udep	_	_
22	cinq	cinq	NUM	_	Number=Plur	23	det	_	_
23	Français	français	NOUN	_	Gender=Masc|Number=Plur	16	mod@relcl	_	SpaceAfter=No|wordform=français
24	.	.	PUNCT	_	_	3	punct	_	_
{{</conll>}}

### Specific Pattern

#### a specific test 

- Description: Just a test

- Pattern: GOV-[subj]->DEP


{{<conll>}}
# text = On ne peut éviter de penser à l'actualité caractérisée par l'enlèvement des otages au Niger--dont cinq Français.
1	On	on	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Ind	3	subj	_	wordform=on
2	ne	ne	ADV	_	Polarity=Neg	3	mod	_	_
3	peut	pouvoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	éviter	éviter	VERB	_	VerbForm=Inf	3	comp:obj	_	Subject=SubjRaising
5	de	de	ADP	_	_	4	comp:obj	_	_
6	penser	penser	VERB	_	VerbForm=Inf	5	comp:obj	_	Subject=SubjRaising
7	à	à	ADP	_	_	6	comp:obl	_	_
8	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	9	det	_	SpaceAfter=No
9	actualité	actualité	NOUN	_	Gender=Fem|Number=Sing	7	comp:obj	_	_
10	caractérisée	caractériser	VERB	_	Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	9	mod	_	_
11	par	par	ADP	_	_	10	comp:obl@agent	_	_
12	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	13	det	_	SpaceAfter=No
13	enlèvement	enlèvement	NOUN	_	Gender=Masc|Number=Sing	11	comp:obj	_	_
14-15	des	_	_	_	_	_	_	_	_
14	de	de	ADP	_	_	13	udep	_	_
15	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	16	det	_	_
16	otages	otage	NOUN	_	Gender=Masc|Number=Plur	14	comp:obj	_	_
17-18	au	_	_	_	_	_	_	_	_
17	à	à	ADP	_	_	13	udep	_	_
18	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	19	det	_	_
19	Niger	Niger	PROPN	_	Gender=Masc|Number=Sing	17	comp:obj	_	SpaceAfter=No
20	--	--	PUNCT	_	_	23	punct	_	SpaceAfter=No
21	dont	dont	PRON	_	PronType=Rel	23	udep	_	_
22	cinq	cinq	NUM	_	Number=Plur	23	det	_	_
23	Français	français	NOUN	_	Gender=Masc|Number=Plur	16	mod@relcl	_	SpaceAfter=No|wordform=français
24	.	.	PUNCT	_	_	3	punct	_	_
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_another_test >}}
