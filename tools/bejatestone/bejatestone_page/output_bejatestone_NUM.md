## bejatestone

### Overview

 just a test

{{<conll>}} 
# text = Trois ans plus tard, il tient un discours sur la crise.
1	Trois	trois	NUM	_	Number=Plur	2	det	_	wordform=trois
2	ans	an	NOUN	_	Gender=Masc|Number=Plur	7	mod	_	_
3	plus	plus	ADV	_	_	4	mod	_	_
4	tard	tard	ADV	_	_	2	mod	_	SpaceAfter=No
5	,	,	PUNCT	_	_	2	punct	_	_
6	il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	7	subj	_	_
7	tient	tenir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
8	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	9	det	_	_
9	discours	discours	NOUN	_	Gender=Masc|Number=Sing	7	comp:obj	_	_
10	sur	sur	ADP	_	_	9	udep	_	_
11	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	12	det	_	_
12	crise	crise	NOUN	_	Gender=Fem|Number=Sing	10	comp:obj	_	SpaceAfter=No
13	.	.	PUNCT	_	_	7	punct	_	_

{{</conll>}}

 The upos [Number](docs/general_guideline/Features/Number.md) has the values : ['Plur', 'Sing']


### Specific Pattern

#### just a test 

- Description: just a test jere

- Pattern: N [upos=NUM]


{{<conll>}}
# text = Trois ans plus tard, il tient un discours sur la crise.
1	Trois	trois	NUM	_	Number=Plur	2	det	_	wordform=trois
2	ans	an	NOUN	_	Gender=Masc|Number=Plur	7	mod	_	_
3	plus	plus	ADV	_	_	4	mod	_	_
4	tard	tard	ADV	_	_	2	mod	_	SpaceAfter=No
5	,	,	PUNCT	_	_	2	punct	_	_
6	il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	7	subj	_	_
7	tient	tenir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
8	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	9	det	_	_
9	discours	discours	NOUN	_	Gender=Masc|Number=Sing	7	comp:obj	_	_
10	sur	sur	ADP	_	_	9	udep	_	_
11	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	12	det	_	_
12	crise	crise	NOUN	_	Gender=Fem|Number=Sing	10	comp:obj	_	SpaceAfter=No
13	.	.	PUNCT	_	_	7	punct	_	_
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_bejatestone_NUM >}}
