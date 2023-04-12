# Reported Speech in Spoken French

We use the annotation as described [there](../../../General_Guideline/particular_construction/reported_speech.md)

* **en mode** : Reported speech can also be introduced by the idomatic preposition _en mode_.
{{<conll>}}
# text_en = he was like are you really sure miss, uh.
# text = il était là en mode mais vous êtes sûre madame, euh.
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj	_	_
2	était	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	_
3	là	là	ADV	_	_	2	comp:pred	_	_
4	en	en	ADP	_	_	2	mod	_	ExtPos=ADP|Idiom=Yes
5	mode	mode	NOUN	_	Number=Sing	4	comp:obj	_	InIdiom=Yes
6	mais	mais	CCONJ	_	_	8	cc	_	_
7	vous	il	PRON	_	Number=Plur|Person=2|PronType=Prs	8	subj	_	_
8	êtes	être	AUX	_	Mood=Ind|Number=Plur|Person=2|Tense=Pres|VerbForm=Fin	5	comp:obj	_	Reported=Yes
9	sûre	sûr	ADJ	_	Gender=Fem|Number=Sing	8	comp:pred	_	_
10	madame	madame	NOUN	_	Gender=Fem|Number=Sing	8	vocative	_	SpaceAfter=No
11	,	,	PUNCT	_	_	12	punct	_	_
12	euh	euh	INTJ	_	_	8	discourse	_	SpaceAfter=No
13	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}


* **être là** :
Sometimes, _en mode_ is absent and there is a direct relation between the idiom _être là_ and the reported speech, which we decide to label `comp:obj`.

{{<conll>}}
# text_en = I was like, my god what is this guy.
# text = j'étais là, mon dieu mais c'est quoi ce gars.
1	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	conj:dicto	_	SpaceAfter=No
2	étais	être	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin	0	root	_	_
3	là	là	ADV	_	_	2	comp:pred	_	SpaceAfter=No
4	,	,	PUNCT	_	_	2	punct	_	_
5	mon	son	DET	_	Number=Sing|Number[psor]=Sing|Person[psor]=1|PronType=Prs	6	det	_	_
6	dieu	dieu	NOUN	_	_	9	discourse	_	ExtPos=INTJ
7	mais	mais	CCONJ	_	_	9	cc	_	_
8	c'	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	9	subj	_	SpaceAfter=No
9	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	2	comp:obj	_	Reported=Yes
10	quoi	quoi	PRON	_	Person=3|PronType=Int	9	comp:pred	_	_
11	ce	ce	DET	_	Gender=Masc|Number=Sing|PronType=Dem	12	det	_	_
12	gars	gars	NOUN	_	Gender=Masc	9	dislocated	_	SpaceAfter=No
13	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

