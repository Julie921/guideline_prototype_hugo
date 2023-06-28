## haitien

### Overview

 Determiners are words that modify nouns or noun phrases and express the reference of the noun phrase in context. In Haitian Creole the determiners are placed always after a noun. However, the "yon" determiner has an exceptional behaviour and is placed before a noun. 

{{<conll>}} 
# sent_id = my_sample__3
# text = Koup la tap vizite fanmi yo an Ayiti epi asiste yon festival lè yo te kidnape yo nan yon otobis, dapre sa yon manm fanmi yo di CNN.
# text_fr = Le couple visitait leur famille en Haïti et assistait à un festival quand ils les ont kidnappés dans un autobus, d'après ce qu'un membre de leur famille a dit à CNN.
1	Koup	Koup	NOUN	_	_	4	subj	_	Gloss=couple
2	la	la	DET	_	Definite=Def|Number=Sing	1	det	_	Gloss=le
3	tap	tap 	AUX	_	_	4	aux	_	Gloss=  PAST PROG
4	vizite	vizite 	VERB	_	Number=Sing|Person=3|Tense=Imp	0	root	_	Gloss=visiter
5	fanmi	fanmi 	NOUN	_	_	4	comp:obj	_	Gloss=famille
6	yo	yo	PRON	_	Number=Sing|Person=3|Poss=Yes	5	det	_	Gloss=PRON
7	an	an	ADP	_	_	4	mod	_	Gloss=en
8	Ayiti	Ayiti	PROPN	_	_	7	comp:obj	_	Gloss=Haïti
9	epi	epi	CCONJ	_	_	10	cc	_	Gloss=puis
10	asiste	asiste 	VERB	_	Number=Sing|Person=3|Tense=Imp	4	conj	_	Gloss=assister
11	yon	yon 	DET	_	Definite=Ind|Number=Sing	12	det	_	Gloss=un
12	festival	festival	NOUN	_	_	10	comp:obj	_	Gloss=festival
13	lè	lè	SCONJ	_	_	10	mod	_	Gloss=quand
14	yo	yo	PRON	_	Number=Plur|Person=3|PronType=Prs	16	subj	_	Gloss=PRON
15	te	te	AUX	_	_	16	aux	_	Gloss=PAST
16	kidnape	kidnape 	VERB	_	Number=Plur|Person=3|Tense=Past	13	comp:obj	_	Gloss=kidnapper
17	yo	yo	PRON	_	Definite=Def|Number=Plur	16	comp:obj	_	Gloss=les
18	nan	nan	ADP	_	_	16	mod	_	Gloss=dans
19	yon	yon 	DET	_	Definite=Ind|Number=Sing	20	det	_	Gloss=un
20	otobis	otobis 	NOUN	_	_	18	comp:obj	_	Gloss=autobus|SpaceAfter=No
21	,	, 	PUNCT	_	_	16	punct	_	_
22	dapre	dapre	ADP	_	_	4	mod	_	Gloss=d'après
23	sa	sa 	PRON	_	_	22	comp:obj	_	Gloss=cela
24	yon	yon	DET	_	Definite=Ind|Number=Sing	25	det	_	Gloss=un
25	manm	manm	NOUN	_	_	28	subj	_	Gloss=membre
26	fanmi	fanmi	NOUN	_	_	25	udep	_	Gloss=famille
27	yo	yo	PRON	_	Definite=Def|Number=Plur	26	det	_	Gloss=PRON
28	di	di	VERB	_	Number=Sing|Person=3|Tense=Past	23	mod@relcl	_	Gloss=dire
29	CNN	CNN	NOUN	_	_	28	comp:obj@R	_	Gloss=CNN|SpaceAfter=No
30	.	.	PUNCT	_	_	28	punct	_	_

{{</conll>}}

- The upos  has the values : ['']


### Specific Pattern

#### Yon determiner 

- Description: The "yon" determiner is an equivalent of an indefinite singular article. It has an exceptional behaviour compared to other determiners in Haitian Creole and it is always placed before a noun. 

- Pattern: GOV -[det]-> DEP; DEP[lemma=yon]


{{<conll>}}
# sent_id = my_sample__5
# text = Lè yon sitwayen Ameriken disparèt, nou travay sere-sere ak otorite lokal yo pandan yap chache moun sa yo e nou pataje enfòmasyon ak fanmi yo nempòt kijan nou kapab."
# text_fr = Quand un citoyen américain disparait, nous travaillons étroitement avec les autorités locales pendant qu'ils cherchent ces gens et nous partageons des informations avec leur famille  n'importe quelle façon dont nous pouvons.
1	Lè	Lè	ADV	_	_	8	mod	_	Gloss=Quand
2	yon	yon	DET	_	Definite=Ind|Number=Sing	3	det	_	Gloss=un
3	sitwayen	sitwayen	NOUN	_	_	5	subj	_	Gloss=citoyen
4	Ameriken	Ameriken	ADJ	_	_	3	mod	_	Gloss=américain
5	disparèt	disparèt	VERB	_	Number=Sing|Person=3|Tense=Pres	1	comp:obj	_	Gloss=disparaitre|SpaceAfter=No
6	,	,	PUNCT	_	_	5	punct	_	_
7	nou	nou	PRON	_	Number=Plur|Person=1|PronType=Prs	8	subj	_	Gloss=PRON
8	travay	travay 	VERB	_	Number=Plur|Person=1|Tense=Pres	0	root	_	Gloss=travailler
9	sere-sere	sere-sere	ADV	_	_	8	mod	_	Gloss=étroitement
10	ak	ak	CCONJ	_	_	8	udep	_	Gloss=avec
11	otorite	otorite 	NOUN	_	_	10	comp:obj	_	Gloss=autorité
12	lokal	lokal	ADJ	_	_	11	mod	_	Gloss=local
13	yo	yo	DET	_	Definite=Def|Number=Plur	11	det	_	Gloss=les
14	pandan	pandan 	ADP	_	_	8	mod	_	Gloss=pendant
15	yap	yap	AUX	_	_	16	subj:aux	_	Gloss=PROG
16	chache	chache	VERB	_	Number=Plur|Person=3|Tense=Pres	14	comp:obj	_	Gloss=chercher
17	moun	moun	NOUN	_	_	16	comp:obj	_	Gloss=gens
18	sa	sa	PRON	_	_	17	det	_	_
19	yo	yo	PRON	_	Number=Plur|PronType=Dem	18	mod	_	Gloss=ces
20	e	e	CCONJ	_	_	22	cc	_	Gloss=et
21	nou	nou	PRON	_	Number=Plur|Person=1|PronType=Prs	22	subj	_	Gloss=nous
22	pataje	pataje	VERB	_	Number=Plur|Person=1|Tense=Pres	8	conj:coord	_	Gloss=partageons
23	enfòmasyon	enfòmasyon 	NOUN	_	_	22	comp:obj	_	Gloss=informations
24	ak	ak	CCONJ	_	_	22	comp:obl	_	Gloss=avec
25	fanmi	fanmi	NOUN	_	_	24	comp:obj	_	Gloss=familles
26	yo	yo	DET	_	Number=Plur|Poss=Yes	25	det	_	Gloss=PRON
27	nenpòt	nenpòt 	ADV	_	_	30	mod	_	Gloss=n'importe
28	kijan	kijan	ADV	_	_	27	unk	_	Gloss=comment
29	nou	nou	PRON	_	Number=Sing|Person=1|PronType=Prs	30	subj	_	Gloss=PRON
30	kapab	kapab	VERB	_	Number=Sing|Person=1|Tense=Pres	25	mod@relcl	_	Gloss=pouvoir|SpaceAfter=No
31	."	."	PUNCT	_	_	8	punct	_	_

{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_haitien_DET >}}
