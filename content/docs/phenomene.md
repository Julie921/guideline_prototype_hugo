---
title: "Phenomene"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

## [Pronominal verbs](http://universal.grew.fr/?custom=642d856e524ac)

Four relations are considered for the reflexive marker _se_: `comp:obj`, `comp:obl`, `comp@expl`, and `comp@pass`.

![Pronominal Verb](/images/pron_verb.png)

All reflexive marker (_se_, _me_, _te_, _nous_, _vous_) are analysed as forms of the reflexive pronoun _se_: `PRON`, `Reflex=Yes`, and `lemma=se`.

The semantic dstinction between reflexive meaning (_je me rase_) and reciprocal meaning (_ils s'aiment_) is not marked. 

* `comp:obj`: Reflexive pronouns replacing a direct object.
{{<conll>}}
# text = donc ils se retournent.
# text_en = and then they turn around

1	donc	donc	ADV	_	_	4	cc	_	_
2	ils	il	PRON	_	Gender=Masc|Number=Plur|Person=3|PronType=Prs	4	subj	_	_
3	se	le	PRON	_	Person=3|PronType=Prs	4	comp:obj	_	Reflex=Yes
4	retournent	retourner	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	SpaceAfter=No
5	.	.	PUNCT	_	_	4	punct	_	_
{{</conll>}}

* `comp:obl`: Reflexive pronouns replacing an oblique complement.
{{<conll>}}
# text = ils se racontent leurs vacances.
# text_en =  they tell each other about their vacation.

1	ils	il	PRON	_	Gender=Masc|Number=Plur|Person=3|PronType=Prs	3	subj	_	_
2	se	lui	PRON	_	Person=3|PronType=Prs	3	comp:obl	_	Reflex=Yes
3	racontent	raconter	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	leurs	son	DET	_	Number=Plur|Number[psor]=Plur|Person[psor]=3|PronType=Prs	5	det	_	_
5	vacances	vacance	NOUN	_	Gender=Fem|Number=Plur	3	comp:obj	_	SpaceAfter=No
6	.	.	PUNCT	_	_	3	punct	_	_
{{</conll>}}

* `comp@expl` : For pronominal verbs i.e. verbs that can only be used with a relexive pronoun (such as _se souvenir_, _s'évaporer_, etc.), or lexicalised verb senses (such as _s'entendre_).
{{<conll>}}
# text = tu te souviens ?
# text_en = do you remember ?

1	tu	il	PRON	_	Number=Sing|Person=2|PronType=Prs	3	subj	_	_
2	te	se	PRON	_	Number=Sing|Person=2|PronType=Prs	3	comp@expl	_	InIdiom=Yes|Reflex=Yes
3	souviens	souvenir	VERB	_	Mood=Ind|Number=Sing|Person=2|Tense=Pres|VerbForm=Fin	0	root	_	ExtPos=VERB|Idiom=Yes
4	?	?	PUNCT	_	_	3	punct	_	_
{{</conll>}}

* `comp@pass`: For passive reflexive constructions, where the the object has been promoted in the subject position: _je vend des livres_ => _les livres se vendent bien_. The marker _se_ is still analysed as a reflexive pronoun, even if it has no pronominal vlue.
{{<conll>}}
# text = donc ça s'est fait.
# text_en = and then it was done 

1	donc	donc	ADV	_	_	4	discourse	_	_
2	ça	ça	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	4	subj	_	_
3	s'	se	PRON	_	Person=3|PronType=Prs	5	comp@pass	_	Reflex=Yes|SpaceAfter=No
4	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
5	fait	faire	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part	4	comp:aux	_	SpaceAfter=No
6	.	.	PUNCT	_	_	4	punct	_	_
{{</conll>}}