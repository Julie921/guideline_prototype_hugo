# Annotation of **-ci** and **-là** 

In French, we consider **-ci** and **-là** as `ADV`. 

>pattern { N [form="-ci"|"-là"] }



{{<conll>}}
# text = Pourquoi en serait-il autrement cette fois-ci ?
1	Pourquoi	pourquoi	ADV	_	_	3	mod	_	wordform=pourquoi
2	en	en	PRON	_	Person=3|PronType=Prs	3	comp@expl	_	_
3	serait	être	VERB	_	Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	SpaceAfter=No
4	-il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj	_	wordform=il
5	autrement	autrement	ADV	_	_	3	mod	_	_
6	cette	ce	DET	_	Gender=Fem|Number=Sing|PronType=Dem	7	det	_	_
7	fois	fois	NOUN	_	Gender=Fem|Number=Sing	3	mod	_	SpaceAfter=No
8	-ci	ci	ADV	_	_	7	mod	_	wordform=ci
9	?	?	PUNCT	_	_	3	punct	_	_
{{</conll>}}


{{<conll>}}
# text = j'étais communiste à ce moment-là.
1	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	SpaceAfter=No
2	étais	être	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin	0	root	_	_
3	communiste	communiste	ADJ	_	Number=Sing	2	comp:pred	_	_
4	à	à	ADP	_	_	2	mod	_	_
5	ce	ce	DET	_	Gender=Masc|Number=Sing|PronType=Dem	6	det	_	_
6	moment	moment	NOUN	_	Gender=Masc|Number=Sing	4	comp:obj	_	SpaceAfter=No
7	-là	là	ADV	_	_	6	mod	_	SpaceAfter=No
8	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

> You can find the conversation about this issues [here](https://github.com/surfacesyntacticud/guidelines/issues/12)