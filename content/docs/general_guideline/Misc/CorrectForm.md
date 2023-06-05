# CorrectForm 

This fetaures `CorrectForm` is used to annotate typo correction.

{{< conll >}}
# text = Ironiquement, Trois morceaux en forme de poire comporte sept mouvements.
1	Ironiquement	ironiquement	ADV	_	_	9	mod	_	SpaceAfter=No|wordform=ironiquement
2	,	,	PUNCT	_	_	1	punct	_	_
3	Trois	trois	NUM	_	Number=Plur	4	det	_	wordform=trois
4	morceaux	morceau	NOUN	_	Gender=Masc|Number=Plur	9	subj	_	_
5	en	en	ADP	_	_	4	udep	_	_
6	forme	forme	NOUN	_	Gender=Fem|Number=Sing	5	comp:obj	_	_
7	de	de	ADP	_	_	6	udep	_	_
8	poire	poire	NOUN	_	Gender=Fem|Number=Sing	7	comp:obj	_	_
9	comporte	comporter	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|Typo=Yes|VerbForm=Fin	0	root	_	CorrectForm=comportent|CorrectNumber=Plur
10	sept	sept	NUM	_	Number=Plur	11	det	_	_
11	mouvements	mouvement	NOUN	_	Gender=Masc|Number=Plur	9	comp:obj	_	SpaceAfter=No
12	.	.	PUNCT	_	_	9	punct	_	_
{{< /conll >}}

There is always the features `[Typo](Typo.md)=Yes` with the node which has the features `CorrectForm`. ## test 






