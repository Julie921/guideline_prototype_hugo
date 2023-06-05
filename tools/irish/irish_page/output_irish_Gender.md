## irish

### Overview

 No it's just a test 

{{<conll>}} 
# text = Crothnófar Pól nó ba úrlabhraí maith é ar Raidió na Gaeltachta agus na meáin eile ag cosaint na n-oifigí poist tuaithe, gné am-tábhachtach de shaol sóisialta na ndaoine.
1	Crothnófar	cronaigh	VERB	VTI	Mood=Ind|Person=0|Tense=Fut	0	root	_	_
2	Pól	Pól	PROPN	Noun	Case=Nom|Definite=Def|Gender=Masc|Number=Sing	1	comp:obj	_	_
3	nó	nó	SCONJ	Subord	_	1	mod	_	_
4	ba	is	AUX	Cop	Tense=Past|VerbForm=Cop	3	comp:obj	_	_
5	úrlabhraí	urlabhraí	NOUN	Noun	Case=Nom|Gender=Masc|Number=Sing|Typo=Yes	4	comp:pred	_	_
6	maith	maith	ADJ	Adj	Case=Nom|Gender=Masc|Number=Sing	5	mod	_	_
7	é	é	PRON	Pers	Gender=Masc|Number=Sing|Person=3	4	subj	_	_
8	ar	ar	ADP	Simp	_	5	udep	_	_
9	Raidió	raidió	PROPN	Noun	Case=Nom|Definite=Def|Gender=Masc|Number=Sing	8	comp:obj	_	NamedEntity=Yes
10	na	an	DET	Art	Case=Gen|Definite=Def|Gender=Fem|Number=Sing|PronType=Art	11	det	_	NamedEntity=Yes
11	Gaeltachta	Gaeltacht	PROPN	Noun	Case=Gen|Definite=Def|Gender=Fem|Number=Sing	9	mod	_	NamedEntity=Yes
12	agus	agus	CCONJ	Coord	_	14	cc	_	_
13	na	an	DET	Art	Definite=Def|Number=Plur|PronType=Art	14	det	_	_
14	meáin	meán	NOUN	Noun	Case=Nom|Definite=Def|Gender=Masc|Number=Plur	9	conj	_	_
15	eile	eile	DET	Det	PronType=Dem|Shared=No	14	det	_	_
16	ag	ag	ADP	Simp	_	1	comp:pred	_	_
17	cosaint	cosaint	NOUN	Noun	VerbForm=Vnoun	16	comp:obj	_	_
18	na	an	DET	Art	Case=Gen|Definite=Def|Number=Plur|PronType=Art	19	det	_	_
19	n-oifigí	oifig	NOUN	Noun	Case=Gen|Definite=Def|Form=Ecl|Gender=Fem|NounType=Strong|Number=Plur	16	comp:obj	_	_
20	poist	post	NOUN	Noun	Case=Gen|Gender=Masc|Number=Sing	19	compound	_	_
21	tuaithe	tuath	NOUN	Noun	Case=Gen|Gender=Fem|Number=Sing	19	mod	_	SpaceAfter=No
22	,	,	PUNCT	Punct	_	23	punct	_	_
23	gné	gné	NOUN	Noun	Case=Nom|Gender=Fem|Number=Sing	19	appos	_	_
24	am-tábhachtach	an-tábhachtach	ADJ	Adj	Case=Nom|Gender=Fem|Number=Sing|Typo=Yes	23	mod	_	_
25	de	de	ADP	Simp	_	23	udep	_	_
26	shaol	saol	NOUN	Noun	Case=Nom|Definite=Def|Form=Len|Gender=Masc|Number=Sing	25	comp:obj	_	_
27	sóisialta	sóisialta	ADJ	Adj	Case=Nom|Gender=Masc|Number=Sing	26	mod	_	_
28	na	an	DET	Art	Case=Gen|Definite=Def|Number=Plur|PronType=Art	29	det	_	_
29	ndaoine	duine	NOUN	Noun	Case=Gen|Definite=Def|Form=Ecl|Gender=Masc|NounType=Strong|Number=Plur	26	mod	_	SpaceAfter=No
30	.	.	PUNCT	.	_	1	punct	_	_
{{</conll>}}

 The upos [ADV](docs/general_guideline/Upos/ADV.md) has the values : ['Masc', 'Fem']


### Specific Pattern

#### an irish test 

- Description: No again just a test

- Pattern: N [Gender]


{{<conll>}}
# text = Crothnófar Pól nó ba úrlabhraí maith é ar Raidió na Gaeltachta agus na meáin eile ag cosaint na n-oifigí poist tuaithe, gné am-tábhachtach de shaol sóisialta na ndaoine.
1	Crothnófar	cronaigh	VERB	VTI	Mood=Ind|Person=0|Tense=Fut	0	root	_	_
2	Pól	Pól	PROPN	Noun	Case=Nom|Definite=Def|Gender=Masc|Number=Sing	1	comp:obj	_	_
3	nó	nó	SCONJ	Subord	_	1	mod	_	_
4	ba	is	AUX	Cop	Tense=Past|VerbForm=Cop	3	comp:obj	_	_
5	úrlabhraí	urlabhraí	NOUN	Noun	Case=Nom|Gender=Masc|Number=Sing|Typo=Yes	4	comp:pred	_	_
6	maith	maith	ADJ	Adj	Case=Nom|Gender=Masc|Number=Sing	5	mod	_	_
7	é	é	PRON	Pers	Gender=Masc|Number=Sing|Person=3	4	subj	_	_
8	ar	ar	ADP	Simp	_	5	udep	_	_
9	Raidió	raidió	PROPN	Noun	Case=Nom|Definite=Def|Gender=Masc|Number=Sing	8	comp:obj	_	NamedEntity=Yes
10	na	an	DET	Art	Case=Gen|Definite=Def|Gender=Fem|Number=Sing|PronType=Art	11	det	_	NamedEntity=Yes
11	Gaeltachta	Gaeltacht	PROPN	Noun	Case=Gen|Definite=Def|Gender=Fem|Number=Sing	9	mod	_	NamedEntity=Yes
12	agus	agus	CCONJ	Coord	_	14	cc	_	_
13	na	an	DET	Art	Definite=Def|Number=Plur|PronType=Art	14	det	_	_
14	meáin	meán	NOUN	Noun	Case=Nom|Definite=Def|Gender=Masc|Number=Plur	9	conj	_	_
15	eile	eile	DET	Det	PronType=Dem|Shared=No	14	det	_	_
16	ag	ag	ADP	Simp	_	1	comp:pred	_	_
17	cosaint	cosaint	NOUN	Noun	VerbForm=Vnoun	16	comp:obj	_	_
18	na	an	DET	Art	Case=Gen|Definite=Def|Number=Plur|PronType=Art	19	det	_	_
19	n-oifigí	oifig	NOUN	Noun	Case=Gen|Definite=Def|Form=Ecl|Gender=Fem|NounType=Strong|Number=Plur	16	comp:obj	_	_
20	poist	post	NOUN	Noun	Case=Gen|Gender=Masc|Number=Sing	19	compound	_	_
21	tuaithe	tuath	NOUN	Noun	Case=Gen|Gender=Fem|Number=Sing	19	mod	_	SpaceAfter=No
22	,	,	PUNCT	Punct	_	23	punct	_	_
23	gné	gné	NOUN	Noun	Case=Nom|Gender=Fem|Number=Sing	19	appos	_	_
24	am-tábhachtach	an-tábhachtach	ADJ	Adj	Case=Nom|Gender=Fem|Number=Sing|Typo=Yes	23	mod	_	_
25	de	de	ADP	Simp	_	23	udep	_	_
26	shaol	saol	NOUN	Noun	Case=Nom|Definite=Def|Form=Len|Gender=Masc|Number=Sing	25	comp:obj	_	_
27	sóisialta	sóisialta	ADJ	Adj	Case=Nom|Gender=Masc|Number=Sing	26	mod	_	_
28	na	an	DET	Art	Case=Gen|Definite=Def|Number=Plur|PronType=Art	29	det	_	_
29	ndaoine	duine	NOUN	Noun	Case=Gen|Definite=Def|Form=Ecl|Gender=Masc|NounType=Strong|Number=Plur	26	mod	_	SpaceAfter=No
30	.	.	PUNCT	.	_	1	punct	_	_
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_irish_Gender >}}
