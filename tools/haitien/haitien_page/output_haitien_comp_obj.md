## haitien

### Overview

 The [comp:obj](docs/general_guideline/Syntactic_relations/comp/comp_obj.md) relation is used for direct object complements, including direct complements of an adposition or a subordinating conjunction. In Haitian Creole the constructions with two direct object complements exist. In this case we use the [comp:obj](docs/general_guideline/Syntactic_relations/comp/comp_obj.md)@R and [comp:obj](docs/general_guideline/Syntactic_relations/comp/comp_obj.md)@T relations.


{{<conll>}} 
# sent_id = my_sample__2
# text = Nikese Toussaint di ke gang te kidnape frè l, madanm li ak yon twazyèm moun ki t ap vwayaje avèk yo 18 mas pase.
# text_fr = Nikese Toussaint a dit que les gangs ont kidnappé son frère, sa femme et une troisième personne qui voyageaient avec eux le 18 mars dernier.
1	Nikese	Nikese	PROPN	_	_	3	subj	_	Gloss=Nikese
2	Toussaint	Toussaint	PROPN	_	_	1	flat:foreign@name	_	Gloss=Toussaint
3	di	di	VERB	_	Number=Sing|Person=3|Tense=Pres	0	root	_	Gloss=dire
4	ke	ke	PRON	_	_	3	comp:obj	_	Gloss=que
5	gang	gang	NOUN	_	_	7	subj	_	Gloss=gang
6	te	te	AUX	_	_	7	aux	_	Gloss=marqueur du passé:
7	kidnape	kidnape	VERB	_	Number=Plur|Person=3|Tense=Past	4	comp:obj	_	Gloss=Kidnapper
8	frè	frè	NOUN	_	_	7	comp:obj	_	Gloss=frère
9	l	l	DET	_	Number=Sing|Person=3|Poss=Yes	8	det	_	Gloss=PRON|SpaceAfter=No
10	,	,	PUNCT	_	_	11	punct	_	_
11	madanm	madanm	NOUN	_	_	8	conj:coord	_	Gloss=madame
12	li	li	DET	_	Number=Sing|Person=3|Poss=Yes	11	det	_	Gloss=PRON
13	ak	ak	CCONJ	_	_	16	cc	_	Gloss=et
14	yon	yon	DET	_	Definite=Ind|Number=Sing	16	det	_	Gloss=une
15	twazyèm	twazyèm	NOUN	_	_	16	mod	_	Gloss=personne
16	moun	moun	NOUN	_	_	11	conj:coord	_	Gloss=personne
17	ki	ki	PRON	_	_	20	subj	_	Gloss=qui
18	t	t	AUX	_	_	20	aux	_	Gloss=PAST
19	ap	ap	AUX	_	_	20	aux	_	Gloss=PROG
20	vwayaje	vwayaje	VERB	_	Number=Plur|Person=3|Tense=Past	16	mod@relcl	_	Gloss=voyager
21	avèk	avèk	ADP	_	_	20	udep	_	Gloss=avec
22	yo	yo	DET	_	Number=Plur|Person=3|PronType=Prs	21	comp:obj	_	Gloss=PRON
23	18	18	NUM	_	_	20	mod	_	Gloss=18
24	mas	mas	NOUN	_	_	23	mod	_	Gloss=mars
25	pase	pase	ADJ	_	_	24	mod	_	Gloss=passé|SpaceAfter=No
26	.	.	PUNCT	_	_	3	punct	_	_

{{</conll>}}

### Specific Pattern

#### direct object complement - recipient 

- Description: In the case of the construction with two direct object complements the [comp:obj](docs/general_guideline/Syntactic_relations/comp/comp_obj.md)@R relation is used for direct object complement that marks the recipient. 

- Pattern: GOV-[comp:obj@R]->DEP


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

#### direct object complement - theme 

- Description: In the case of the construction with two direct object complements the [comp:obj](docs/general_guideline/Syntactic_relations/comp/comp_obj.md)@T relation is used for direct object complement that marks the theme. 

- Pattern: GOV-[comp:obj@T]->DEP


{{<conll>}}
# sent_id = my_sample__3
# text = Toussaint di nan yon entèvyou nan telefòn lendi ke gang nan mande $200,000 pou chak moun, e ke fanmi li pa gen kalite lajan sa a.
# text_fr = Toussaint a dit dans un interview par téléphone lundi que le gang demande $200,000 pour chaque personne et que sa famille n'a pas cette somme d'argent.
1	Toussaint	Toussaint	PROPN	_	_	2	subj	_	Gloss=Toussaint
2	di	di	VERB	_	Number=Sing|Person=3|Tense=Pres	0	root	_	Gloss=dire
3	nan	nan	ADP	_	_	2	mod	_	Gloss=dans
4	yon	yon	DET	_	Definite=Ind|Number=Sing	5	det	_	Gloss=un
5	entèvyou	entèvyou	NOUN	_	_	3	comp:obj	_	Gloss=interview
6	nan	nan	NOUN	_	_	2	mod	_	Gloss=au
7	telefòn	telefòn	NOUN	_	_	6	comp:obj	_	Gloss=téléphone
8	lendi	lendi	NOUN	_	_	2	mod	_	Gloss=lundi
9	ke	ke	PRON	_	_	2	comp:obj	_	Gloss=que
10	gang	gang	NOUN	_	_	12	subj	_	Gloss=gang
11	nan	nan	DET	_	Definite=Def|Number=Sing	12	comp:obj@R	_	Gloss=le
12	mande	mande	VERB	_	Number=Sing|Person=3|Tense=Pres	9	comp:obj	_	Gloss=demander
13	$	$	X	_	_	14	mod	_	_
14	200,000	200,000	NUM	_	NumType=Card	12	comp:obj@T	_	Gloss=deux cent mile
15	pou	pou	ADP	_	_	14	mod	_	Gloss=pour
16	chak	chak	DET	_	_	17	det	_	Gloss=chaque
17	moun	moun	NOUN	_	_	15	comp:obj	_	Gloss=personne|SpaceAfter=No
18	,	,	PUNCT	_	_	20	punct	_	_
19	e	e	CCONJ	_	_	20	cc	_	Gloss=et
20	ke	ke	PRON	_	_	9	conj:coord	_	Gloss=que
21	fanmi	fanmi	NOUN	_	_	24	subj	_	Gloss=famille
22	li	li	DET	_	Number=Sing|Person=3|Poss=Yes	21	det	_	Gloss=PRON
23	pa	pa	PART	_	_	24	mod	_	Gloss=ne pas
24	gen	gen	VERB	_	Number=Sing|Person=3|Tense=Pres	20	comp:obj	_	Gloss=avoir
25	kalite	kalite	NOUN	_	_	26	mod	_	_
26	lajan	lajan	NOUN	_	_	24	comp:obj	_	Gloss=argent
27	sa	sa	DET	_	Number=Sing|PronType=Dem	26	det	_	Gloss=cet
28	a	a	DET	_	_	27	mod	_	SpaceAfter=No
29	.	.	PUNCT	_	_	2	punct	_	_

{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_haitien_comp_obj >}}
