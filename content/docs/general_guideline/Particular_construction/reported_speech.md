# Reported Speech in spoken corpora
## Universal 

Reported speech as a feature `Reported=Yes` on its head. It is generally the `comp:obj`of a speech verb, such as _dire_ 'to say'. 

> pattern { GOV -[comp:obj]-> DEP ; DEP [Reported=Yes] }


> French
{{<conll>}}
# text = je fais oui, oui, j'ai l'impression de t'avoir déjà vue !
1	je	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	AlignBegin=11315|AlignEnd=11458
2	fais	faire	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	AlignBegin=11458|AlignEnd=11601
3	oui	oui	ADV	_	_	8	discourse	_	AlignBegin=11601|AlignEnd=11743|ExtPos=INTJ|SpaceAfter=No
4	,	,	PUNCT	_	_	5	punct	_	AlignBegin=11743|AlignEnd=11743
5	oui	oui	ADV	_	_	3	conj:coord	_	AlignBegin=11743|AlignEnd=11886|ExtPos=INTJ|SpaceAfter=No
6	,	,	PUNCT	_	_	5	punct	_	AlignBegin=11886|AlignEnd=11886
7	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	8	subj	_	AlignBegin=11886|AlignEnd=12024|SpaceAfter=No
8	ai	avoir	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	2	comp:obj	_	AlignBegin=12024|AlignEnd=12162|Reported=Yes
9	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	10	det	_	AlignBegin=12162|AlignEnd=12300|SpaceAfter=No
10	impression	impression	NOUN	_	Gender=Fem|Number=Sing	8	comp:obj@lvc	_	AlignBegin=12300|AlignEnd=12438
11	de	de	ADP	_	_	10	udep	_	AlignBegin=12438|AlignEnd=12577
12	t'	le	PRON	_	Number=Sing|Person=2|PronType=Prs	15	comp:obj	_	AlignBegin=12577|AlignEnd=12715|SpaceAfter=No
13	avoir	avoir	AUX	_	VerbForm=Inf	11	comp:obj	_	AlignBegin=12715|AlignEnd=12853|Subject=SubjRaising
14	déjà	déjà	ADV	_	_	13	mod	_	AlignBegin=12853|AlignEnd=12991
15	vue	voir	VERB	_	Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part	13	comp:aux@tense	_	AlignBegin=12991|AlignEnd=13129
16	!	!	PUNCT	_	_	2	punct	_	AlignBegin=13129|AlignEnd=13129
{{</conll>}}

{{< hint warning>}}
We previously annotated reported speech using the syntactic relation parataxis:obj, but this is now considered obsolete.
{{</hint>}}

## French spoken 

### Reported speech introduce by a verb 

Usually, the reported speech are introduce by a speech verb (such as `dire`, `demander`, `répondre`) :

{{<conll>}}
# text = j'ai dit tu es, euh, nouvelle, une redoublante ?
1	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	AlignBegin=13129|AlignEnd=13370|SpaceAfter=No
2	ai	avoir	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	AlignBegin=13370|AlignEnd=13610
3	dit	dire	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	2	comp:aux@tense	_	AlignBegin=13610|AlignEnd=13851
4	tu	il	PRON	_	Number=Sing|Person=2|PronType=Prs	5	subj	_	AlignBegin=13851|AlignEnd=14185
5	es	être	AUX	_	Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	3	comp:obj	_	AlignBegin=14185|AlignEnd=14519|Reported=Yes|SpaceAfter=No
6	,	,	PUNCT	_	_	5	punct	_	AlignBegin=14519|AlignEnd=14519
7	euh	euh	INTJ	_	_	5	discourse	_	AlignBegin=14519|AlignEnd=14853|SpaceAfter=No
8	,	,	PUNCT	_	_	9	punct	_	AlignBegin=14853|AlignEnd=14853
9	nouvelle	nouveau	ADJ	_	Gender=Fem|Number=Sing	5	comp:pred	_	AlignBegin=14853|AlignEnd=15187|SpaceAfter=No
10	,	,	PUNCT	_	_	12	punct	_	AlignBegin=15187|AlignEnd=15187
11	une	un	DET	_	Definite=Ind|Gender=Fem|Number=Sing|PronType=Art	12	det	_	AlignBegin=15187|AlignEnd=15521
12	redoublante	redoublant	NOUN	_	Gender=Fem|Number=Sing	9	conj:dicto	_	AlignBegin=15521|AlignEnd=15855
13	?	?	PUNCT	_	_	2	punct	_	AlignBegin=15855|AlignEnd=15855
{{</conll>}}


The verb faire can also be used to introduce reported speech :
{{<conll>}}
# text = je fais oui, oui, j'ai l'impression de t'avoir déjà vue !
1	je	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	AlignBegin=11315|AlignEnd=11458
2	fais	faire	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	AlignBegin=11458|AlignEnd=11601
3	oui	oui	ADV	_	_	8	discourse	_	AlignBegin=11601|AlignEnd=11743|ExtPos=INTJ|SpaceAfter=No
4	,	,	PUNCT	_	_	5	punct	_	AlignBegin=11743|AlignEnd=11743
5	oui	oui	ADV	_	_	3	conj:coord	_	AlignBegin=11743|AlignEnd=11886|ExtPos=INTJ|SpaceAfter=No
6	,	,	PUNCT	_	_	5	punct	_	AlignBegin=11886|AlignEnd=11886
7	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	8	subj	_	AlignBegin=11886|AlignEnd=12024|SpaceAfter=No
8	ai	avoir	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	2	comp:obj	_	AlignBegin=12024|AlignEnd=12162|Reported=Yes
9	l'	le	DET	_	Definite=Def|Number=Sing|PronType=Art	10	det	_	AlignBegin=12162|AlignEnd=12300|SpaceAfter=No
10	impression	impression	NOUN	_	Gender=Fem|Number=Sing	8	comp:obj@lvc	_	AlignBegin=12300|AlignEnd=12438
11	de	de	ADP	_	_	10	udep	_	AlignBegin=12438|AlignEnd=12577
12	t'	le	PRON	_	Number=Sing|Person=2|PronType=Prs	15	comp:obj	_	AlignBegin=12577|AlignEnd=12715|SpaceAfter=No
13	avoir	avoir	AUX	_	VerbForm=Inf	11	comp:obj	_	AlignBegin=12715|AlignEnd=12853|Subject=SubjRaising
14	déjà	déjà	ADV	_	_	13	mod	_	AlignBegin=12853|AlignEnd=12991
15	vue	voir	VERB	_	Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part	13	comp:aux@tense	_	AlignBegin=12991|AlignEnd=13129
16	!	!	PUNCT	_	_	2	punct	_	AlignBegin=13129|AlignEnd=13129
{{</conll>}}

### Reported speech introduce by `en mode`

Reported speech can also be introduced by the idomatic preposition _en mode_.
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


### Reported speech introduce by `être là`
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

TODO : rajouter tableau avec les différentes annotations possibles. 