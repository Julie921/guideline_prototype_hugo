---
title: "Number"
weight: 2
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false 
---

# Number 

## Universal

*Definition from de [UD website](https://universaldependencies.org/u/feat/Number.html)*
Number is usually an inflectional feature of [nouns](../Upos/NOUN.md) and, depending on language, other parts of speech ([pronouns](../Upos/PRON.md), [adjectives](../Upos/ADJ.md), [determiners](../Upos/DET.md), [numerals](../Upos/NUM.md), [verbs](../Upos/VERB.md)) that mark agreement with [nouns](../Upos/NOUN.md).

In languages where noun phrases are pluralized using a specific function word (pluralizer), this function word is tagged DET and `Number=Plur` is its lexical feature.

{{< conll >}}
# text = euh, je pense que la chirurgie, c'est pareil, hein.
1	euh	euh	INTJ	_	_	4	discourse	_	SpaceAfter=No
2	,	,	PUNCT	_	_	1	punct	_	_
3	je	il	PRON	_	Number=Sing|Person=1|PronType=Prs	4	subj	_	_
4	pense	penser	VERB	_	Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin	0	root	_	_
5	que	que	SCONJ	_	_	4	comp:obj	_	_
6	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	7	det	_	_
7	chirurgie	chirurgie	NOUN	_	Gender=Fem|Number=Sing	10	dislocated	_	SpaceAfter=No
8	,	,	PUNCT	_	_	7	punct	_	_
9	c'	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	10	subj	_	SpaceAfter=No
10	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	5	comp:obj	_	_
11	pareil	pareil	ADJ	_	Gender=Masc|Number=Sing	10	comp:pred	_	SpaceAfter=No
12	,	,	PUNCT	_	_	13	punct	_	_
13	hein	hein	INTJ	_	_	11	discourse	_	SpaceAfter=No
14	.	.	PUNCT	_	_	4	punct	_	_
{{< /conll >}}

## French 

Several upos can have the `Number` features in French : 

![Number POS french](/images/french_number_upos.png)

{{< hint info >}}
Tableau double entrée pour avoir les valeurs de traits ? Est-ce qu'on décrit les règles d'accord par exemple ? 
{{< /hint >}}

