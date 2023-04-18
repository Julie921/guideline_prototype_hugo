# **un peu**

We analyse **peu** from **un peu** as a `NOUN` with an `ExtPos=ADV` because it can modify an `ADJ`, `ADV`, `VERB` and an `SCONJ`. We also add the features `Idiom`. 

{{<conll>}}
# text = Je dis que je trouve ça un peu limite.
1	Je	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	wordform=je
2	dis	dire	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	_
3	que	que	SCONJ	_	_	2	comp:obj	_	_
4	je	il	PRON	_	Number=Sing|Person=1|PronType=Prs	5	subj	_	_
5	trouve	trouver	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	3	comp:obj	_	_
6	ça	ça	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	5	comp:obj	_	_
7	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	8	det	_	InIdiom=Yes
8	peu	peu	NOUN	_	_	9	mod	_	ExtPos=ADV|Idiom=Yes
9	limite	limite	NOUN	_	Gender=Fem|Number=Sing	5	comp:pred	_	SpaceAfter=No
10	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

> You can find the conversation about this annotation [here](https://github.com/surfacesyntacticud/guidelines/issues/10)