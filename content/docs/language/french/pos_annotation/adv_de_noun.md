# `ADV` + **de** + `NOUN`

In order to analyse these expression : 
- **(*un*) peu de** + `NOUN`
- **beaucoup de** + `NOUN`
- **plein de** + `NOUN`
- **nombre de** + `NOUN`
<br><br>
We use the features `Idiom` and `ExtPos` to consider the initial `ADV` as a `PRON` in theses expressions. So we have the following annotation :


> pattern { N1 [upos=ADV]; N2 [form="de"]; N3 [upos=NOUN] ;N1 < N2 ; N2<N3}


#### **un peu de**

{{<conll>}}
# text = Je souligne que les brochettes de poulet sont exquises avec un peu de sauce !
1	Je	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	wordform=je
2	souligne	souligner	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	_
3	que	que	SCONJ	_	_	2	comp:obj	_	_
4	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	5	det	_	_
5	brochettes	brochette	NOUN	_	Gender=Fem|Number=Plur	8	subj	_	_
6	de	de	ADP	_	_	5	udep	_	_
7	poulet	poulet	NOUN	_	Gender=Masc|Number=Sing	6	comp:obj	_	_
8	sont	être	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	3	comp:obj	_	_
9	exquises	exquis	ADJ	_	Gender=Fem|Number=Plur	8	comp:pred	_	_
10	avec	avec	ADP	_	_	8	mod	_	_
11	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	12	det	_	InIdiom=Yes
12	peu	peu	ADV	_	_	10	comp:obj	_	ExtPos=PRON|Idiom=Yes
13	de	de	ADP	_	_	12	comp:obl	_	_
14	sauce	sauce	NOUN	_	Gender=Fem|Number=Sing	13	comp:obj	_	_
15	!	!	PUNCT	_	_	2	punct	_	_
{{</conll>}}

#### **beaucoup de**

{{<conll>}}
# text = Il a la particularité de marquer beaucoup de la tête.
1	Il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj	_	wordform=il
2	a	avoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	4	det	_	_
4	particularité	particularité	NOUN	_	Gender=Fem|Number=Sing	2	comp:obj	_	_
5	de	de	ADP	_	_	4	udep	_	_
6	marquer	marquer	VERB	_	VerbForm=Inf	5	comp:obj	_	Subject=SubjRaising
7	beaucoup	beaucoup	ADV	_	_	6	mod	_	_
8	de	de	ADP	_	_	6	mod	_	_
9	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	10	det	_	_
10	tête	tête	NOUN	_	Gender=Fem|Number=Sing	8	comp:obj	_	SpaceAfter=No
11	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

#### **plein de**

{{<conll>}}
# text = Boutique agréable, on y trouve plein de marques.
1	Boutique	boutique	NOUN	_	Gender=Fem|Number=Sing	6	mod	_	wordform=boutique
2	agréable	agréable	ADJ	_	Gender=Fem|Number=Sing	1	mod	_	SpaceAfter=No
3	,	,	PUNCT	_	_	1	punct	_	_
4	on	on	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Ind	6	subj	_	_
5	y	y	PRON	_	Person=3|PronType=Prs	6	mod	_	_
6	trouve	trouver	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
7	plein	plein	ADV	_	_	6	comp:obj	_	ExtPos=PRON
8	de	de	ADP	_	_	7	comp:obl	_	_
9	marques	marque	NOUN	_	Gender=Fem|Number=Plur	8	comp:obj	_	SpaceAfter=No
10	.	.	PUNCT	_	_	6	punct	_	_
{{</conll>}}

#### **nombre de**

{{<conll>}}
# text = Nombre d'investisseurs qui, auparavant, voyaient d'un mauvais œil l'accumulation de liquidités par les entreprises reconnaissent maintenant les avantages de la constitution de réserves de liquidités importantes.
1	Nombre	nombre	ADV	_	_	20	subj	_	ExtPos=PRON|wordform=nombre
2	d'	de	ADP	_	_	1	comp:obl	_	SpaceAfter=No
3	investisseurs	investisseur	NOUN	_	Gender=Masc|Number=Plur	2	comp:obj	_	_
4	qui	qui	PRON	_	PronType=Rel	8	subj	_	SpaceAfter=No
5	,	,	PUNCT	_	_	4	punct	_	_
6	auparavant	auparavant	ADV	_	_	8	mod	_	SpaceAfter=No
7	,	,	PUNCT	_	_	6	punct	_	_
8	voyaient	voir	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin	3	mod@relcl	_	_
9	d'	de	ADP	_	_	8	mod	_	SpaceAfter=No
10	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	12	det	_	_
11	mauvais	mauvais	ADJ	_	Gender=Masc|Number=Sing	12	mod	_	_
12	œil	œil	NOUN	_	Gender=Masc|Number=Sing	9	comp:obj	_	_
13	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	14	det	_	SpaceAfter=No
14	accumulation	accumulation	NOUN	_	Gender=Fem|Number=Sing	8	comp:obj	_	_
15	de	de	ADP	_	_	14	udep	_	_
16	liquidités	liquidité	NOUN	_	Gender=Fem|Number=Plur	15	comp:obj	_	_
17	par	par	ADP	_	_	14	udep	_	_
18	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	19	det	_	_
19	entreprises	entreprise	NOUN	_	Gender=Fem|Number=Plur	17	comp:obj	_	_
20	reconnaissent	reconnaître	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
21	maintenant	maintenant	ADV	_	_	20	mod	_	_
22	les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	23	det	_	_
23	avantages	avantage	NOUN	_	Gender=Masc|Number=Plur	20	comp:obj	_	_
24	de	de	ADP	_	_	23	udep	_	_
25	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	26	det	_	_
26	constitution	constitution	NOUN	_	Gender=Fem|Number=Sing	24	comp:obj	_	_
27	de	de	ADP	_	_	26	udep	_	_
28	réserves	réserve	NOUN	_	Gender=Fem|Number=Plur	27	comp:obj	_	_
29	de	de	ADP	_	_	28	udep	_	_
30	liquidités	liquidité	NOUN	_	Gender=Fem|Number=Plur	29	comp:obj	_	_
31	importantes	important	ADJ	_	Gender=Fem|Number=Plur	28	mod	_	SpaceAfter=No
32	.	.	PUNCT	_	_	20	punct	_	_
{{</conll>}}

