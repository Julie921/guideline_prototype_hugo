# How to annotate a-**t-il** ? 

We chosse this annotation for **-t-il** : 

\# text = j'étais communiste à ce moment-là.
1	j'	il	PRON	_	Number=Sing|Person=1|PronType=Prs	2	subj	_	SpaceAfter=No
2	étais	être	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin	0	root	_	_
3	communiste	communiste	ADJ	_	Number=Sing	2	comp:pred	_	_
4	à	à	ADP	_	_	2	mod	_	_
5	ce	ce	DET	_	Gender=Masc|Number=Sing|PronType=Dem	6	det	_	_
6	moment	moment	NOUN	_	Gender=Masc|Number=Sing	4	comp:obj	_	SpaceAfter=No
7	-là	là	ADV	_	_	6	mod	_	SpaceAfter=No
8	.	.	PUNCT	_	_	2	punct	_	_

Thus, we consider **-t-il** as a `PRON` and **-t** as no syntactic meaning alone. That is why the lemma is **il**. For **-t**, we consider **-t-il** as an allomorph of **il** and **-il**. **-t** is no a syntactic element. It is a morphophonological rule that introduces the sound /t/.

>[!tip]
> pattern { N1 [form="-t-il"]}