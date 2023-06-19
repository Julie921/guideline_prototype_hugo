## haitien

### Overview

 The governor and the dependent of an [udep](docs/general_guideline/Syntactic_relations/udep/udep.md) relation can have any POS. The [udep](docs/general_guideline/Syntactic_relations/udep/udep.md) relation is frequently given to the complements of nouns, since it is generally more difficult to distinguish between arguments and modifiers for nouns than it is for verbs. In most cases the dependent of an [udep](docs/general_guideline/Syntactic_relations/udep/udep.md) can have a [ADP](docs/general_guideline/Upos/ADP.md) pos. 

{{<conll>}} 
# text = Gen 17 misyonè ki moun Etazini ak Kanada ke yon gang te kenbe pou ranson an 2021 pandan yo tap travay pou Christian Aid Ministries ki gen katye jeneral li nan eta Ohio nan sant wès Etazini.
# text_fr = Il y a 17 missionnaires qui sont des américains et canadiens  qu'un gang a capturé pour de l'argent en 2021 pendant qu'ils étaient en train de travailler pour Christian Aid Ministrie qui a son quartier général dans l'Etat Ohio dans le  centre Ouest des Etats-Unis.
1	Gen	Gen	VERB	_	Number=Sing|Person=3|Tense=Pres	0	root	_	Gloss=Avoir
2	17	17	NUM	_	_	3	det	_	Gloss=17
3	misyonè	misyonè	NOUN	_	_	1	comp:obj	_	Gloss=missionnaire
4	ki	ki 	PRON	_	_	5	cc	_	Gloss=qui
5	moun	moun	NOUN	_	VerbForm=Vnoun	3	mod@relcl	_	Gloss=gens
6	Etazini	Etazini	PROPN	_	_	5	udep	_	Gloss=Etats-Unis
7	ak	ak	CCONJ	_	_	8	cc	_	Gloss=et
8	Kanada	kanada 	PROPN	_	_	6	conj:coord	_	Gloss=Kanada
9	ke	ke	PRON	_	_	13	comp:obj	_	Gloss=que
10	yon	yon	DET	_	_	11	det	_	Gloss=un
11	gang	gang	NOUN	_	_	13	subj	_	Gloss=gang
12	te	te	AUX	_	_	13	aux	_	Gloss=marqueur du passé
13	kenbe	kenbe	VERB	_	_	5	mod@relcl	_	Gloss=capturer
14	pou	pou 	ADP	_	_	13	udep	_	Gloss=pour
15	ranson	ranson	NOUN	_	_	14	comp:obj	_	Gloss=raison
16	an	an	DET	_	_	13	udep	_	Gloss=la
17	2021	2021	NUM	_	_	16	comp:obj	_	Gloss=2021
18	pandan	pandan	SCONJ	_	_	13	mod	_	Gloss=pendant
19	yo	yo	PRON	_	_	21	subj	_	Gloss=ils
20	t ap	t ap	AUX	_	_	21	aux	_	Gloss=marqueur du passé: travaillaient
21	travay	travay 	VERB	_	_	18	comp:obj	_	Gloss=travailler
22	pou	pou	ADP	_	_	21	udep	_	Gloss=pour
23	Christian	Christian	PROPN	_	_	22	comp:obj	_	Gloss=Christian
24	Aid	Aid 	PROPN	_	_	23	flat:foreign@name	_	Gloss=Aid
25	Ministries	Ministries 	PROPN	_	_	24	flat:foreign@name	_	Gloss=Ministries
26	ki	ki	PRON	_	_	27	subj	_	Gloss=qui
27	gen	gen	VERB	_	_	23	mod@relcl	_	Gloss=avoir
28	katye	katye	NOUN	_	_	27	comp:obj	_	Gloss=quartier
29	jeneral	jeneral 	ADJ	_	_	28	mod	_	Gloss=général
30	li	li 	DET	_	_	28	det	_	Gloss=son
31	nan	nan 	ADP	_	_	27	udep	_	Gloss=dans
32	Eta	Eta 	NOUN	_	_	31	comp:obj	_	Gloss=état
33	Ohio	Ohio	PROPN	_	_	32	udep	_	Gloss=Ohio
34	nan	nan	ADP	_	_	32	mod	_	Gloss=dans
35	sant	sant 	NOUN	_	_	34	comp:obj	_	Gloss=centre
36	wès	wès 	NOUN	_	_	35	mod	_	Gloss=ouest
37	Etazini	Etazini 	PROPN	_	_	35	udep	_	Gloss=Etats-Unis|SpaceAfter=No
38	.	. 	PUNCT	_	_	1	punct	_	_
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

{{< agg table_output_haitien_udep >}}
