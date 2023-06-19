## haitien

### Overview

 In Haitian creole The [subj](docs/general_guideline/Syntactic_relations/subj/subj.md) relation is used for all subjects, regardless of their form. The [subj](docs/general_guideline/Syntactic_relations/subj/subj.md) label in Haitian Creole is usually used to mark relations between a [VERB](docs/general_guideline/Upos/VERB.md) and a nominal group ( [NOUN](docs/general_guideline/Upos/NOUN.md), [PROPN](docs/general_guideline/Upos/PROPN.md) or [PRON](docs/general_guideline/Upos/PRON.md)). You can see all the patterns in the table below.

{{<conll>}} 
# sent_id = my_sample__1
# text = Yon pòt pawòl Depatman d Eta deklare Samdi, gouvènman Ameriken an o kouran de rapò ki di kòm kwa gen 2 sitwayen Ameriken ki disparèt an Ayiti, apre laprès nan eta Florid rapòte yo kidnape yon koup.
# text_fr = Un porte-parole du département d'Etat américain déclare samedi, que le gouvernement est au courant du rapport qui dit comme quoi qu'il y a deux citoyens américains qui sont disparus en Haïti , après que la presse dans l'Etat Floride rapporte qu'ils ont kidnappé un couple.
1	Yon	Yon 	DET	_	Definite=Ind|Number=Sing	2	det	_	Gloss=Un
2	pòt	pòt 	NOUN	_	_	7	subj	_	Gloss=porte
3	pawòl	pawòl 	NOUN	_	_	2	compound	_	Gloss=parole
4	Depatman	Depatman	NOUN	_	_	3	comp:obj	_	Gloss=département
5	d	d	X	_	_	4	udep	_	Gloss=d'
6	Eta	Eta	NOUN	_	_	5	goeswith	_	Gloss=Eta
7	deklare	deklare 	VERB	_	Number=Sing|Person=3|Tense=Pres	0	root	_	Gloss=déclarer
8	Samdi	Samdi	NOUN	_	_	7	mod	_	Gloss=samedi|SpaceAfter=No
9	,	,	PUNCT	_	_	7	punct	_	_
10	gouvènman	gouvènman 	NOUN	_	_	13	subj	_	Gloss=gouvernement
11	Ameriken	ameriken 	ADJ	_	_	10	mod	_	Gloss=américain
12	an	an	DET	_	Definite=Def|Number=Sing	11	det	_	Gloss=le
13	o	o	X	_	_	7	comp:obj	_	Gloss=au
14	kouran	kouran	NOUN	_	VerbForm=Vnoun	13	goeswith	_	Gloss=être au courant
15	de	de 	ADP	_	_	14	udep	_	Gloss=de
16	rapò	rapò 	NOUN	_	_	15	comp:obj	_	Gloss=rapport
17	ki	ki	PRON	_	_	18	subj	_	Gloss=qui
18	di	di	VERB	_	Number=Sing|Person=3|Tense=Pres	16	mod@relcl	_	Gloss=dire
19	kòm	kòm	SCONJ	_	_	18	comp:obj	_	Gloss=comme
20	kwa	kwa	PRON	_	_	19	unk	_	Gloss=quoi
21	gen	gen 	VERB	_	_	19	comp:obj	_	Gloss=avoir
22	2	2	NUM	_	_	23	det:num	_	Gloss=deux
23	sitwayen	sitwayen 	NOUN	_	_	21	comp:obj	_	Gloss=citoyen
24	Ameriken	amirekèn	ADJ	_	_	23	mod	_	Gloss=américain
25	ki	ki	PRON	_	_	26	subj	_	Gloss=qui
26	disparèt	disparèt	VERB	_	Number=Plur|Person=3|Tense=Pres	24	mod@relcl	_	Gloss=disparaître
27	an	an	ADP	_	_	26	mod	_	Gloss=en
28	Ayiti	Aiti	PROPN	_	_	27	comp:obj	_	Gloss=Haïti|SpaceAfter=No
29	,	,	PUNCT	_	_	26	punct	_	_
30	apre	apre	ADP	_	_	31	mod	_	Gloss=après
31	laprès	laprès 	NOUN	_	_	35	subj	_	Gloss=la presse
32	nan	nan	ADP	_	_	31	mod	_	Gloss=dans
33	eta	eta	NOUN	_	_	32	comp:obj	_	Gloss=eta
34	Florid	Florid 	PROPN	_	_	33	comp:obj	_	Gloss=Floride
35	rapòte	rapòte 	VERB	_	Number=Sing|Person=3|Tense=Pres	7	conj	_	Gloss=rapporter
36	yo	yo	PRON	_	Number=Plur|Person=3|PronType=Prs	37	subj	_	Gloss=PRON
37	kidnape	kidnape	VERB	_	_	35	comp:obj	_	Gloss=kidnapper
38	yon	yon	DET	_	Definite=Ind|Number=Sing	39	det	_	Gloss=une
39	koup	koup 	NOUN	_	_	37	comp:obj	_	Gloss=coupe|SpaceAfter=No
40	.	.	PUNCT	_	_	7	punct	_	_
{{</conll>}}

### Specific Pattern

#### Causative construction with [ADP](docs/general_guideline/Upos/ADP.md) governor 

- Description: In Haitian Creole a causative construction can be expressed with [ADP](docs/general_guideline/Upos/ADP.md) in the role of the root instead of a [VERB](docs/general_guideline/Upos/VERB.md) or an [AUX](docs/general_guideline/Upos/AUX.md). Then the governor of the [subj](docs/general_guideline/Syntactic_relations/subj/subj.md) is en [ADP](docs/general_guideline/Upos/ADP.md).

- Pattern: GOV -[subj]-> DEP; GOV[upos=ADP]


{{<conll>}}
# sent_id = my_sample__10
# text = Batay ant gang yo pou kontwòl teritwa lakoz anpil san koule epi plizyè santèn milye moun oblije kouri kite kay yo.
# text_fr = La lutte entre les gangs pour le contrôle des territoires  a fait couler beaucoup de sang et plusieurs  centaines de gens sont obligés de courir en laissant leur maison.
1	Batay	Batay 	NOUN	_	_	8	subj	_	Gloss=Lutte
2	ant	ant 	ADP	_	_	1	udep	_	Gloss=entre
3	gang	gang	NOUN	_	_	2	comp:obj	_	Gloss=gangs
4	yo	yo	DET	_	Definite=Def|Number=Plur	3	det	_	Gloss=les
5	pou	pou	ADP	_	_	1	udep	_	Gloss=pour
6	kontwòl	kontwòl	NOUN	_	_	5	comp:obj	_	Gloss=contrôle
7	teritwa	teritwa 	NOUN	_	_	6	comp:obj	_	Gloss=territoire
8	lakoz	lakoz	ADP	_	_	0	root	_	Gloss=à cause
9	anpil	anpil	ADJ	_	_	10	mod	_	Gloss=beacoup
10	san	san	NOUN	_	_	8	comp:obj	_	Gloss=sang
11	koule	koule	VERB	_	Number=Sing|Person=3|Tense=Pres	8	comp:pred	_	Gloss=coulé
12	epi	epi	CCONJ	_	_	17	cc	_	Gloss=et
13	plizyè	plizyè	ADV	_	_	14	det	_	Gloss=plusieurs
14	santèn	santèn	NUM	_	_	17	subj	_	Gloss=centaine
15	milye	milye	NUM	_	_	14	comp:obj	_	Gloss=milliers
16	moun	moun	NOUN	_	_	15	comp:obj	_	Gloss=gens
17	oblije	oblije	VERB	_	Number=Plur|Person=3|Tense=Pres	8	conj:coord	_	Gloss=obliger
18	kouri	kouri	VERB	_	VerbForm=Inf	17	comp:obl	_	Gloss=courir
19	kite	kite 	VERB	_	VerbForm=Inf	18	compound:svc	_	Gloss=quitter
20	kay	kay	NOUN	_	_	19	comp:obj	_	Gloss=maisons
21	yo	yo	DET	_	Number=Plur|Person=3|Poss=Yes	20	det	_	Gloss=PRON|SpaceAfter=No
22	.	.	PUNCT	_	_	8	punct	_	_
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_haitien_subj >}}
