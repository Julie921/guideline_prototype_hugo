---
title: "Il y a"
weight: 3
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Il y a 

There are three possible annotation for `il y a` in french : 

- Il y a as an adposition
- Il y a as an expletive construction
- Il y a as a locativ pronoun

## `Il y a` as an adposition

Sometimes, `il y a` is used to express a temporal argument. 

pattern : N1 [form="il"]; N2 [lemma="y"]; N3 [lemma="avoir"]; N1 << N2; N2 << N3 ; N3-[comp]->N2 ; N3-[subj]-> N1

{{< conll >}}
# text = vous y étiez il y a pas longtemps.
1	vous	il	PRON	_	Number=Plur|Person=2|PronType=Prs	3	subj	_	_
2	y	y	PRON	_	Person=3|PronType=Prs	3	comp:pred	_	_
3	étiez	être	AUX	_	Mood=Ind|Number=Plur|Person=2|Tense=Imp|VerbForm=Fin	0	root	_	_
4	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	6	subj	_	InIdiom=Yes
5	y	y	PRON	_	Person=3|PronType=Prs	6	comp	_	InIdiom=Yes
6	a	avoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	3	mod	_	ExtPos=ADP|Idiom=Yes
7	pas	pas	ADV	_	Polarity=Neg	6	mod	_	_
8	longtemps	longtemps	ADV	_	_	6	mod	_	SpaceAfter=No
9	.	.	PUNCT	_	_	3	punct	_	_

{{< /conll >}}


## `Il y a` as an expletive construction 

Sometimes, `il y a` is used to express an expletive construction. 

pattern : N1 [form="il"]; N2 [lemma="y"]; N3 [lemma="avoir"]; N1 << N2; N2 << N3 ; N3-[comp@expl]->N2 ; N3-[subj@expl]-> N1

{{< conll >}}
# text = il y a pas de problème.
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@expl	_	_
2	y	y	PRON	_	Person=3|PronType=Prs	3	comp@expl	_	_
3	a	avoir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	pas	pas	ADV	_	Polarity=Neg	3	mod	_	_
5	de	de	ADP	_	_	3	comp:obj	_	_
6	problème	problème	NOUN	_	Gender=Masc|Number=Sing	5	comp:obj	_	SpaceAfter=No
7	.	.	PUNCT	_	_	3	punct	_	_
{{< /conll >}}


## `Il y a` with `y` as a locativ pronoun 

Sometimes, the `y` is a locativ pronoun which express a location in the `il y a` expression 

pattern : N1 [form="il"]; N2 [lemma="y"]; N3 [lemma="avoir"]; N1 << N2; N2 << N3 ; N3-[mod]->N2 ; N3-[subj]-> N1


{{< conll >}}
# text = Il a aussi beaucoup travaillé en Allemagne, il y a réalisé par exemple le nouvel hôtel de ville de Mayence, l'entrée du Hannover Concert Hall et le pavillon administratif de la centrale électrique d'Hambourg.
1	Il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs|Shared=No	2	subj	_	wordform=il
2	a	avoir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	aussi	aussi	ADV	_	_	2	mod	_	_
4	beaucoup	beaucoup	ADV	_	_	5	mod	_	_
5	travaillé	travailler	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act	2	comp:aux@tense	_	_
6	en	en	ADP	_	_	2	mod	_	_
7	Allemagne	Allemagne	PROPN	_	_	6	comp:obj	_	SpaceAfter=No
8	,	,	PUNCT	_	_	11	punct	_	_
9	il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	11	subj	_	_
10	y	y	PRON	_	Emph=No|Person=3|PronType=Prs	11	mod	_	_
11	a	avoir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	2	conj:coord	_	_
12	réalisé	réaliser	VERB	_	Gender=Masc|Number=Sing|Shared=No|Tense=Past|VerbForm=Part|Voice=Act	11	comp:aux@tense	_	_
13	par	par	ADP	_	_	12	mod	_	ExtPos=ADV|Idiom=Yes
14	exemple	exemple	NOUN	_	Gender=Masc|Number=Sing	13	comp:obj	_	InIdiom=Yes
15	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art|Shared=No	17	det	_	_
16	nouvel	nouveau	ADJ	_	Gender=Masc|Number=Sing|Shared=No	17	mod	_	_
17	hôtel	hôtel	NOUN	_	Gender=Masc|Number=Sing	12	comp:obj	_	_
18	de	de	ADP	_	_	17	udep	_	_
19	ville	ville	NOUN	_	Gender=Fem|Number=Sing	18	comp:obj	_	_
20	de	de	ADP	_	_	17	udep	_	_
21	Mayence	Mayence	PROPN	_	_	20	comp:obj	_	SpaceAfter=No
22	.	.	PUNCT	_	_	2	punct	_	_
{{< /conll >}}


