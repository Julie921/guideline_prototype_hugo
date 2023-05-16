## french

### Overview

 description of the [subj](docs/general_guideline/Syntactic_relations/subj/subj.md) in french

### Specific Pattern

#### nominal subject 

- Pattern: GOV-[[subj](docs/general_guideline/Syntactic_relations/subj/subj.md)]->DEP ; DEP [upos=[PRON](docs/general_guideline/Upos/PRON.md)|[PROPN](docs/general_guideline/Upos/PROPN.md)|[NOUN](docs/general_guideline/Upos/NOUN.md)]


- Description: Description of nominal subject

{{<conll>}} 
# text = quand vous étiez à la manif, ouais.
1	quand	quand	[SCONJ](docs/general_guideline/Upos/SCONJ.md)	_	_	0	root	_	AlignBegin=32406|AlignEnd=32669
2	vous	il	[PRON](docs/general_guideline/Upos/PRON.md)	_	[Number](docs/general_guideline/Features/Number.md)=Plur|[Person](docs/general_guideline/Features/Person.md)=2|PronType=Prs	3	[subj](docs/general_guideline/Syntactic_relations/subj/subj.md)	_	AlignBegin=32669|AlignEnd=32931
3	étiez	être	[VERB](docs/general_guideline/Upos/VERB.md)	_	[Mood](docs/general_guideline/Features/Mood.md)=Ind|[Number](docs/general_guideline/Features/Number.md)=Plur|[Person](docs/general_guideline/Features/Person.md)=2|[Tense](docs/general_guideline/Features/Tense.md)=Imp|[VerbForm](docs/general_guideline/Features/VerbForm.md)=Fin	1	comp:obj	_	AlignBegin=32931|AlignEnd=33194
4	à	à	[ADP](docs/general_guideline/Upos/ADP.md)	_	_	3	comp:obl	_	AlignBegin=33194|AlignEnd=33194
5	la	le	[DET](docs/general_guideline/Upos/DET.md)	_	Definite=Def|[Gender](docs/general_guideline/Features/Gender.md)=Fem|[Number](docs/general_guideline/Features/Number.md)=Sing|PronType=Art	6	det	_	AlignBegin=33194|AlignEnd=33457
6	manif	manif	[NOUN](docs/general_guideline/Upos/NOUN.md)	_	[Gender](docs/general_guideline/Features/Gender.md)=Fem|[Number](docs/general_guideline/Features/Number.md)=Sing	4	comp:obj	_	AlignBegin=33457|AlignEnd=33719|SpaceAfter=No
7	,	,	[PUNCT](docs/general_guideline/Upos/PUNCT.md)	_	_	8	punct	_	AlignBegin=33719|AlignEnd=33719
8	ouais	ouais	[INTJ](docs/general_guideline/Upos/INTJ.md)	_	_	6	[discourse](docs/general_guideline/Syntactic_relations/macrosyntaxe/discourse/discourse.md)	_	AlignBegin=33719|AlignEnd=33982|SpaceAfter=No
9	.	.	[PUNCT](docs/general_guideline/Upos/PUNCT.md)	_	_	1	punct	_	AlignBegin=33982|AlignEnd=33982
{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_subj >}}
