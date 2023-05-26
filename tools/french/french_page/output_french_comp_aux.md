## french

### Overview

 test for conll

{{<conll>}} 
# text_en = He makes it fall.
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@caus	_	Gloss=he
2	le	le	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	comp:obj@agent	_	Gloss=it
3	fait	faire	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=makes
4	tomber	tomber	VERB	_	VerbForm=Inf	3	comp:aux@caus	_	Gloss=fall
{{</conll>}}

### Specific Pattern

#### test one 

- Description: test

- Pattern: GOV[Number]


{{<conll>}}
# text_en = He makes it fall.
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@caus	_	Gloss=he
2	le	le	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	comp:obj@agent	_	Gloss=it
3	fait	faire	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=makes
4	tomber	tomber	VERB	_	VerbForm=Inf	3	comp:aux@caus	_	Gloss=fall
{{</conll>}}

#### causative test two 

- Description: test 2

- Pattern: GOV[Gender]


{{<conll>}}
# text_en = He makes it fall.
1	il	il	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj@caus	_	Gloss=he
2	le	le	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	comp:obj@agent	_	Gloss=it
3	fait	faire	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	Gloss=makes
4	tomber	tomber	VERB	_	VerbForm=Inf	3	comp:aux@caus	_	Gloss=fall
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_comp_aux >}}
