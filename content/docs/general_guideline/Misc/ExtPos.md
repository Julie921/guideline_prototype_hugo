---
title: "Ext Pos"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# ExtPos 

## Universal

The `ExtPos` feature was introduced to facilitate the annotation of idioms, titles, and other multi-word units which behave like a certain part of speech, even though none of their constituents necessarily carry that part of speech. This feature allows the annotator to preserve the internal syntactic relationships between the various components of these units.

See [Idioms and titles](./Idiom_Titles.md) page for examples of idioms and titles annotations.

The usage of `ExtPos` was also generalized to cases of single tokens which are given a `upos`  but they are used in the syntactic structure with another role.

## Naija

In Naija, it is mostly used for adjective used as verbs.

![Extpos cluster in Naija](/images/General_Guideline/Misc/ExtPos/naija_extpos_cluster.png)

> Naija

{{< conll >}}
# text_en = It'll get better.
1	e	im	PRON	_	Case=Nom|Number=Sing|Person=3|PronType=Prs	2	subj	_	AlignBegin=307749|AlignEnd=308144|Gloss=NOM.SG.3
2	go	go	AUX	_	Aspect=Prosp	0	root	_	AlignBegin=308144|AlignEnd=308540|Gloss=PROSP
3	better	beta	ADJ	_	Degree=Cmp|ExtPos=VERB	2	comp:aux	_	AlignBegin=308540|AlignEnd=308935|Gloss=good.CMPR
4	//	//	PUNCT	_	_	2	punct	_	AlignBegin=308935|AlignEnd=308935|Gloss=PUNCT
{{< /conll >}}

See [More examples on Grew-match](http://match.grew.fr/?corpus=SUD_Naija-NSC@latest&custom=613dff2609468).

## French 

{{< hint info >}}
Idée du type de table que l'on pourrait avoir ici. Est-ce que chaque case pourrait être cliquable et renvoyer vers la page correspondante ? Ou plutôt vers le pattern dans GREW (après, on peut être redirigé vers GREW directement depuis la page correspondante) ? On peut rediriger vers la page si elle existe, sinon vers grew.  
{{< /hint >}}

![clusterisation of ExtPos in French](/images/General_Guideline/Misc/ExtPos/extpos_cluster.png)

In French, it is mainly used for:

 * tokens with `upos=SYM` [Grew-match on SUD_French-GSD](http://match.grew.fr/?corpus=SUD_French-GSD@latest&custom=613e03ce49731)
 * tokens with `upos=ADV` and `ExtPos=PRON` for phrases like *beaucoup de NOUN*, *plus de NOUN* [Grew-match on SUD_French-GSD](http://match.grew.fr/?corpus=SUD_French-GSD@latest&custom=613e040411ae4&clustering=N.lemma)
 * tokens with [`upos=NOUN` and `ExtPos=ADV`](../Upos/ADV.md#upos-noun--extpos--adv) for phrases like *grâce à NOUN*, *face à NOUN* [Grew-match on SUD_French-GSD](http://match.grew.fr/?corpus=SUD_French-GSD@latest&custom=613e0370bf8ee&clustering=N.lemma)
 

## french

### Overview

 In French, it is mainly used for:

tokens with upos=[SYM](docs/general_guideline/Upos/SYM.md) 
tokens with upos=[ADV](docs/general_guideline/Upos/ADV.md) and [ExtPos](docs/general_guideline/Misc/ExtPos.md)=[PRON](docs/general_guideline/Upos/PRON.md) for phrases like beaucoup de [NOUN](docs/general_guideline/Upos/NOUN.md), plus de [NOUN](docs/general_guideline/Upos/NOUN.md)
tokens with upos=[NOUN](docs/general_guideline/Upos/NOUN.md) and [ExtPos](docs/general_guideline/Misc/ExtPos.md)=[ADV](docs/general_guideline/Upos/ADV.md) for phrases like grâce à [NOUN](docs/general_guideline/Upos/NOUN.md), face à [NOUN](docs/general_guideline/Upos/NOUN.md)

{{<conll>}} 
# text = Il a fait partie de groupes musicaux comme Los Abuelos de la Nada et Los Rodríguez.
1	Il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	2	subj	_	wordform=il
2	a	avoir	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	fait	faire	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Act	2	comp:aux@tense	_	_
4	partie	partie	NOUN	_	Gender=Fem|Number=Sing	3	comp:obj@lvc	_	_
5	de	de	ADP	_	_	3	comp:obl	_	_
6	groupes	groupe	NOUN	_	Gender=Masc|Number=Plur	5	comp:obj	_	_
7	musicaux	musical	ADJ	_	Gender=Masc|Number=Plur	6	mod	_	_
8	comme	comme	ADP	_	_	6	udep	_	_
9	Los	Los	X	_	Foreign=Yes	8	comp:obj	_	ExtPos=PROPN|Lang=es
10	Abuelos	Abuelos	X	_	Foreign=Yes	9	flat@name	_	Lang=es
11	de	de	X	_	Foreign=Yes	10	flat@name	_	Lang=es
12	la	la	X	_	Foreign=Yes	11	flat@name	_	Lang=es
13	Nada	Nada	X	_	Foreign=Yes	12	flat@name	_	Lang=es
14	et	et	CCONJ	_	_	15	cc	_	_
15	Los	Los	X	_	Foreign=Yes	9	conj:coord	_	Lang=es
16	Rodríguez	Rodríguez	X	_	Foreign=Yes|Shared=No	15	flat@name	_	Lang=es|SpaceAfter=No
17	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

### Specific Pattern

#### adverb used as pronoun 

- Description: It is used for some construction such as : 
- *beaucoup* de + [NOUN](docs/general_guideline/Upos/NOUN.md)
- *près* de + [NOUN](docs/general_guideline/Upos/NOUN.md)
- *peu* de + [NOUN](docs/general_guideline/Upos/NOUN.md)

Here, the adverbs have the features [NOUN](docs/general_guideline/Upos/NOUN.md) as [ExtPos](docs/general_guideline/Misc/ExtPos.md).

- Pattern: N [ExtPos=PRON, !Idiom, !Title, upos=ADV]


{{<conll>}}
# text = Elle y incarnera la Poussette de Manon peu de temps après.
1	Elle	lui	PRON	_	Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs	3	subj	_	wordform=elle
2	y	y	PRON	_	Emph=No|Person=3|PronType=Prs	3	mod	_	_
3	incarnera	incarner	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Fut|VerbForm=Fin	0	root	_	_
4	la	le	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	5	det	_	_
5	Poussette	Poussette	PROPN	_	Gender=Fem|Number=Sing	3	comp:obj	_	_
6	de	de	ADP	_	_	5	udep	_	_
7	Manon	Manon	PROPN	_	_	6	comp:obj	_	_
8	peu	peu	ADV	_	_	11	mod	_	ExtPos=PRON
9	de	de	ADP	_	_	8	comp:obl	_	_
10	temps	temps	NOUN	_	Gender=Masc|Number=Sing	9	comp:obj	_	_
11	après	après	ADV	_	_	3	mod	_	SpaceAfter=No
12	.	.	PUNCT	_	_	3	punct	_	_
{{</conll>}}

#### noun used in prespositional construction 

- Description: It is used for some construction such as : 
- *grâce* + [ADP](docs/general_guideline/Upos/ADP.md) (à)
- *face* + [ADP](docs/general_guideline/Upos/ADP.md) (à)
- *suite* + [ADP](docs/general_guideline/Upos/ADP.md) (à)

Here, the nouns have the features [ADV](docs/general_guideline/Upos/ADV.md) as [ExtPos](docs/general_guideline/Misc/ExtPos.md).

- Pattern: N [ExtPos=ADV, !Idiom, !Title, upos=NOUN]


{{<conll>}}
# text = Elle s'impose grâce à un bond à 7,23 m établi à son sixième et dernier essai.
1	Elle	lui	PRON	_	Emph=No|Gender=Fem|Number=Sing|Person=3|PronType=Prs	3	subj@pass	_	wordform=elle
2	s'	soi	PRON	_	Person=3|PronType=Prs|Reflex=Yes	3	comp@pass	_	SpaceAfter=No
3	impose	imposer	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
4	grâce	grâce	NOUN	_	_	3	mod	_	ExtPos=ADV
5	à	à	ADP	_	_	4	comp:obl	_	_
6	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	7	det	_	_
7	bond	bond	NOUN	_	Gender=Masc|Number=Sing	5	comp:obj	_	_
8	à	à	ADP	_	_	7	udep	_	_
9	7,23	7,23	NUM	_	Number=Plur	10	det	_	_
10	m	mètre	NOUN	_	Gender=Masc|Number=Plur	8	comp:obj	_	_
11	établi	établir	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	7	mod	_	_
12	à	à	ADP	_	_	11	mod	_	_
13	son	son	DET	_	Number=Sing|Number[psor]=Sing|Person[psor]=3|Poss=Yes|PronType=Prs	17	det	_	_
14	sixième	sixième	ADJ	_	Gender=Masc|Number=Sing	17	mod	_	_
15	et	et	CCONJ	_	_	16	cc	_	_
16	dernier	dernier	ADJ	_	Gender=Masc|Number=Sing	14	conj:coord	_	_
17	essai	essai	NOUN	_	Gender=Masc|Number=Sing	12	comp:obj	_	SpaceAfter=No
18	.	.	PUNCT	_	_	3	punct	_	_

{{</conll>}}

#### french symbols 

- Description: The features [ExtPos](docs/general_guideline/Misc/ExtPos.md) is mainly used for the tokens with the symbols [SYM](docs/general_guideline/Upos/SYM.md) part of speech.

- Pattern: N [ExtPos, !Idiom, !Title, upos=SYM]


{{<conll>}}
# text = Les capteurs solaires sous vide de Viessmann offrent un rendement optique maximal (de près 80%).
1	Les	le	DET	_	Definite=Def|Number=Plur|PronType=Art	2	det	_	wordform=les
2	capteurs	capteur	NOUN	_	Gender=Masc|Number=Plur	8	subj	_	_
3	solaires	solaire	ADJ	_	Gender=Masc|Number=Plur	2	mod	_	_
4	sous	sous	ADP	_	_	2	udep	_	_
5	vide	vide	NOUN	_	Gender=Masc|Number=Sing	4	comp:obj	_	_
6	de	de	ADP	_	_	2	udep	_	_
7	Viessmann	Viessmann	PROPN	_	_	6	comp:obj	_	_
8	offrent	offrir	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
9	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	10	det	_	_
10	rendement	rendement	NOUN	_	Gender=Masc|Number=Sing	8	comp:obj	_	_
11	optique	optique	ADJ	_	Gender=Masc|Number=Sing	10	mod	_	_
12	maximal	maximal	ADJ	_	Gender=Masc|Number=Sing	10	mod	_	_
13	(	(	PUNCT	_	_	14	punct	_	SpaceAfter=No
14	de	de	ADP	_	_	10	udep	_	_
15	près	près	ADV	_	_	16	mod	_	_
16	80	80	NUM	_	Number=Plur	17	det	_	SpaceAfter=No
17	%	%	SYM	_	Number=Plur	14	comp:obj	_	ExtPos=NOUN|SpaceAfter=No
18	)	)	PUNCT	_	_	14	punct	_	SpaceAfter=No
19	.	.	PUNCT	_	_	8	punct	_	_

{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_french_ExtPos >}}






## bedja

TODO
### Overview

### Specific Pattern


