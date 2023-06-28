---
title: "udep"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# Udep 



## Universal 

The `udep` relation is used for complements when one does not wish to or is unable to distinguish between arguments and modifiers. This relationship can notably be used in cases where the complement's relationship with its governor is ambiguous. When there is little debate about the nature of the relationship, the more specific label is preferred.


>pattern { GOV-[udep]->DEP} 

The governor and the dependent of a `udep` relation can have any POS. The `udep` relation is frequently given to the complements of nouns, since it is generally more difficult to distinguish between arguments and modifiers for nouns than it is for verbs.

  

As shown in the [correspondences between SUD and UD](../../../../_index.md#correspondences-between-ud-and-sud), the `udep` label is used while automatically converting an `obl` label from a UD annotation. This is because `obl` can correspond to both `comp:obl` and `mod` in SUD.

  
> English
{{<conll>}}

1   An  a   DET _   _   2   det _   _

2   act act NOUN    _   _   0   root    _   _

3   of  of  ADP _   _   2   udep    _   _

4   creation    creation    NOUN    _   _   3   comp:obj    _   _

{{</conll>}}

  
> English
{{<conll>}}

1   She she PRON    _   _   2   subj    _   _

2   smiles  smile   VERB    _   _   0   root    _   _

3   at  at  ADP _   _   2   udep    _   _

4   this    this    DET _   _   5   det _   _

5   discomfiture    discomfiture    NOUN    _   _   3   comp:obj    _   _

{{</conll>}}

  

> Spanish
{{<conll>}}

# text_es = Ficha de Juanjo Ciércolen en Don Balón

# text_en = File of Juan Ciércoles in Don Balón
1   Ficha   ficha   PRON    _   _   0   root    _   Gloss=file

2   de  de  ADP _   _   1   udep    _   Gloss=of

3   Juanjo  juanjo  PROPN   _   _   2   comp:obl    _   Gloss=Juanjo

4   Ciércoles   ciércoles   PROPN   _   _   3   flat    _   Gloss=Ciércoles

5   en  en  ADP _   _   1   udep    _   Gloss=in

6   Don don PROPN   _   _   5   comp:obj    _   Gloss=Don

7   Balón   balón   PROPN   _   _   6   appos   _   Gloss=Balón

{{</conll>}}




## french

TODO
### Overview

### Specific Pattern






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

 



