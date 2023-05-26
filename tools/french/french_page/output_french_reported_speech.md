## french

### Overview

 Usually, the reported speech are introduce by a speech verb (such as dire, demander, répondre) 

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

### Specific Pattern

#### reported speech introduce by a verb 

- Description: Usually, the reported speech are introduce by a speech verb (such as dire, demander, répondre) 

- Pattern:  N [Reported=Yes] ; GOV-[comp:obj]->N ; GOV[upos= VERB,lemma <>faire]


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

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_reported_speech >}}
