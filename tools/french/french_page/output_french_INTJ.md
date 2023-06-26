## french

### Overview

 Pure interjections (such as ah, hein, ouais, euh, etc.) are analysed as INTJs. Discourse markers coming from other POS (such as enfin, chouette, disons, etc.), as well as idioms (such as en fait, tu sais, etc.), keep their original POS but have an additional [ExtPos](docs/general_guideline/Misc/ExtPos.md) = [INTJ](docs/general_guideline/Upos/INTJ.md) feature. Except 4 of them which are frequent and are analysed as pure INTJs: bon, ben, quoi, and tiens.

{{<conll>}} 
# text_en = So it was the price of, I mean, the price of a full course you know.
# text = Donc le prix d'un, enfin ouais c'était, le prix d'un repas en fait hein.
1	donc	donc	ADV	_	_	10	discourse	_	_
2	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	3	det	_	_
3	prix	prix	NOUN	_	Gender=Masc|Number=Sing	10	dislocated	_	_
4	d'	de	ADP	_	_	3	udep	_	SpaceAfter=No
5	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	4	comp:obj@scrap	_	SpaceAfter=No
6	,	,	PUNCT	_	_	7	punct	_	_
7	enfin	enfin	ADV	_	_	3	discourse	_	ExtPos=INTJ
8	ouais	ouais	INTJ	_	_	3	discourse	_	_
9	c'	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	10	subj	_	SpaceAfter=No
10	était	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	SpaceAfter=No
11	,	,	PUNCT	_	_	13	punct	_	_
12	le	le	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	13	det	_	_
13	prix	prix	NOUN	_	Gender=Masc|Number=Sing	10	comp:pred	_	_
14	d'	de	ADP	_	_	13	udep	_	SpaceAfter=No
15	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	16	det	_	_
16	repas	repas	NOUN	_	Gender=Masc|Number=Sing	14	comp:obj	_	_
17	en	en	ADP	_	_	10	discourse	_	ExtPos=ADV|Idiom=Yes
18	fait	fait	NOUN	_	Gender=Masc|Number=Sing	17	comp:obj	_	InIdiom=Yes
19	hein	hein	INTJ	_	_	10	discourse	_	SpaceAfter=No
20	.	.	PUNCT	_	_	10	punct	_	_
{{</conll>}}

- The upos  has the values : ['']


### Specific Pattern

#### other part of speech as interjection  

- Description: Idioms (such as en fait, tu sais, etc.), keep their original POS but have an additional [ExtPos](docs/general_guideline/Misc/ExtPos.md) = [INTJ](docs/general_guideline/Upos/INTJ.md) feature.

- Pattern: N [ExtPos=INTJ]


{{<conll>}}
# text_en = uh so actually uh you'll see then.
# text = euh ben en fait juste euh tu verras après.
1	euh	euh	INTJ	_	_	8	discourse	_	_
2	ben	ben	INTJ	_	_	8	discourse	_	_
3	en	en	ADP	_	_	8	discourse	_	ExtPos=ADV|Idiom=Yes
4	fait	fait	NOUN	_	Gender=Masc|Number=Sing	3	comp:obj	_	InIdiom=Yes
5	juste	juste	ADV	_	_	8	mod	_	_
6	euh	euh	INTJ	_	_	5	discourse	_	_
7	tu	il	PRON	_	Number=Sing|Person=2|PronType=Prs	8	subj	_	_
8	verras	voir	VERB	_	Mood=Ind|Number=Sing|Person=2|Tense=Fut|VerbForm=Fin	0	root	_	_
9	après	après	ADV	_	_	8	mod	_	SpaceAfter=No
10	.	.	PUNCT	_	_	8	punct	_	_
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_INTJ >}}
