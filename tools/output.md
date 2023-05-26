## french

### Overview

 Description of comp:aux@tense

{{<conll>}} 
# text = j'ai d~ euh, bah tu as fait quoi ?
1	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	AlignBegin=31907|AlignEnd=32051|SpaceAfter=No
2	ai	avoir	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	AlignBegin=32051|AlignEnd=32194
3	d~	d~	X	_	_	2	comp:aux@tense	_	AlignBegin=32194|AlignEnd=32338|ExtPos=X
4	euh	euh	INTJ	_	_	8	discourse	_	AlignBegin=32338|AlignEnd=32505|SpaceAfter=No
5	,	,	PUNCT	_	_	4	punct	_	AlignBegin=32505|AlignEnd=32505
6	bah	bah	INTJ	_	_	8	discourse	_	AlignBegin=32505|AlignEnd=32672
7	tu	il	PRON	_	Number=Sing|Person=2|PronType=Prs	8	subj	_	AlignBegin=32672|AlignEnd=32839
8	as	avoir	AUX	_	Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	3	comp:obj	_	AlignBegin=32839|AlignEnd=33005|Reported=Yes
9	fait	faire	VERB	_	Gender=Masc|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	8	comp:aux@tense	_	AlignBegin=33005|AlignEnd=33172
10	quoi	quoi	PRON	_	_	9	comp:obj	_	AlignBegin=33172|AlignEnd=33339
11	?	?	PUNCT	_	_	2	punct	_	AlignBegin=33339|AlignEnd=33339

{{</conll>}}

### Specific Pattern

#### explication one 

- Pattern: GOV-[comp:aux@tense]->DEP


- Description: Description of AUX 

{{<conll>}}
# text = j'ai d~ euh, bah tu as fait quoi ?
1	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	AlignBegin=31907|AlignEnd=32051|SpaceAfter=No
2	ai	avoir	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	AlignBegin=32051|AlignEnd=32194
3	d~	d~	X	_	_	2	comp:aux@tense	_	AlignBegin=32194|AlignEnd=32338|ExtPos=X
4	euh	euh	INTJ	_	_	8	discourse	_	AlignBegin=32338|AlignEnd=32505|SpaceAfter=No
5	,	,	PUNCT	_	_	4	punct	_	AlignBegin=32505|AlignEnd=32505
6	bah	bah	INTJ	_	_	8	discourse	_	AlignBegin=32505|AlignEnd=32672
7	tu	il	PRON	_	Number=Sing|Person=2|PronType=Prs	8	subj	_	AlignBegin=32672|AlignEnd=32839
8	as	avoir	AUX	_	Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	3	comp:obj	_	AlignBegin=32839|AlignEnd=33005|Reported=Yes
9	fait	faire	VERB	_	Gender=Masc|Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	8	comp:aux@tense	_	AlignBegin=33005|AlignEnd=33172
10	quoi	quoi	PRON	_	_	9	comp:obj	_	AlignBegin=33172|AlignEnd=33339
11	?	?	PUNCT	_	_	2	punct	_	AlignBegin=33339|AlignEnd=33339

{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg request_output_french_comp_aux >}}
