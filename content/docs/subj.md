---
title: "Subj"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

## The `subj` relation 

### Universal

The `subj` relation is used for all subjects, regardless of their form (nominal or verbal). This relationship encompasses both the `nsubj` and `csubj` relationships as defined by UD, as the following examples show.

> English

{{< conll >}}
      1	A	a	DET	_	_	2	det	_	_
      2	man	man	NOUN	_	_	3	subj	_	_
      3	walks	walk	VERB	_	_	0	root	_	_
{{< /conll >}}



### French
The `subj` in french is usualy between a VERB or an AUX (often the root) and a nominal group (PRON, PROPN or NOUN). You can see all the pattern in this table. 

![extrait_image](/images/tableau_subj_test.png)

{{< hint info >}}
Dans l'idéal, les patterns du tableau sont reliés aux patterns d'explication (s'il y en a ?) dans la page correspondante des guidelines. Est-ce qu'on met touts les patterns ? Comment on décide ? Pour le moment - manuellement. 
{{< /hint >}}


#### nominal subject 
The `subj`dependancy is usually between a AUX or a VERB and a NOUN, PRON, PROPN or a NUM. 

pattern : `GOV-[subj]->DEP ; GOV [upos=AUX|VERB] ; DEP[upos=NOUN|PROPN|PRON|NUM,!Title, !InTitle]`

#### title as a subject 

When the subject is a title, we can have any of the SUD part of speech. 

pattern : `GOV-[subj]->DEP ; DEP [Title=Yes/InTitle=Yes]`

{{< conll >}}
# text = J'étais une aventurière est un film français réalisé par Raymond Bernard.
1	J'	moi	PRON	_	Emph=No|Number=Sing|Person=1|PronType=Prs	2	subj	_	InTitle=Yes|SpaceAfter=No|wordform=j'
2	étais	être	AUX	_	Mood=Ind|Number=Sing|Person=1|Tense=Imp|VerbForm=Fin	5	subj	_	ExtPos=PROPN|Title=Yes
3	une	un	DET	_	Definite=Ind|Gender=Fem|Number=Sing|PronType=Art	4	det	_	InTitle=Yes
4	aventurière	aventurière	NOUN	_	Gender=Fem|Number=Sing	2	comp:pred	_	InTitle=Yes
5	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
6	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	7	det	_	_
7	film	film	NOUN	_	Gender=Masc|Number=Sing	5	comp:pred	_	_
8	français	français	ADJ	_	Gender=Masc|Number=Sing	7	mod	_	_
9	réalisé	réaliser	VERB	_	Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part|Voice=Pass	7	mod	_	_
10	par	par	ADP	_	_	9	comp:obl@agent	_	_
11	Raymond	Raymond	PROPN	_	_	10	comp:obj	_	_
12	Bernard	Bernard	PROPN	_	_	11	flat@name	_	_
13	.	.	PUNCT	_	_	5	punct	_	_
{{< /conll >}}

#### VerbInf as a subject 

In French, a infinitive verb can also be a subject. 

pattern : `GOV-[subj]->DEP ; GOV [upos=AUX|VERB] ; DEP [upos=VERB|AUX, VerbForm = Inf, !Title, !InTitle]`

{{< conll >}}
# text = Aller dans ce restaurant est tout simplement un grand plaisir !
1	Aller	aller	VERB	_	VerbForm=Inf	5	subj	_	Subject=Generic|wordform=aller
2	dans	dans	ADP	_	_	1	comp:obl	_	_
3	ce	ce	DET	_	Gender=Masc|Number=Sing|PronType=Dem	4	det	_	_
4	restaurant	restaurant	NOUN	_	Gender=Masc|Number=Sing	2	comp:obj	_	_
5	est	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
6	tout	tout	ADV	_	_	7	mod	_	_
7	simplement	simplement	ADV	_	_	5	mod	_	_
8	un	un	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	10	det	_	_
9	grand	grand	ADJ	_	Gender=Masc|Number=Sing	10	mod	_	_
10	plaisir	plaisir	NOUN	_	Gender=Masc|Number=Sing	5	comp:pred	_	_
11	!	!	PUNCT	_	_	5	punct	_	_
{{< /conll >}}

#### Adverbial subject 

In French, an [ADV](adv.md) can be a subject. It is a specific phenomena due to the french language. The ADV have an  `ExtPos=PRON`. 

pattern : `GOV-[subj]->DEP ; GOV [upos=AUX|VERB] ; DEP [upos=ADV, ExtPos=PRON, !Title, !InTitle]`

{{< conll >}}
# text = Beaucoup d'entre eux devinrent délinquants.
1	Beaucoup	beaucoup	ADV	_	_	5	subj	_	ExtPos=PRON|wordform=beaucoup
2	d'	de	ADP	_	_	1	comp:obl	_	ExtPos=ADP|Idiom=Yes|SpaceAfter=No
3	entre	entre	ADP	_	_	2	unk	_	InIdiom=Yes
4	eux	eux	PRON	_	Emph=Yes|Gender=Masc|Number=Plur|Person=3|PronType=Prs	2	comp:obj	_	_
5	devinrent	devenir	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Past|VerbForm=Fin	0	root	_	_
6	délinquants	délinquant	NOUN	_	Gender=Masc|Number=Plur	5	comp:pred	_	_
7	.	.	PUNCT	_	_	5	punct	_	_
{{< /conll >}}

{{%expand "Non rédigé" %}}
## Deep syntactic features

The `subj` relation has two deep syntactic sub-relations. The sub-relation `subj@expl` is used to indicate that the subject is present to fill in an obligatory syntactic position and has no semantic value. You can find more information about the expletive constructions on this [page](../../deep_features/expletive).

> French

{{< conll >}}
      # sent_fr = Il pleut dans ma maison
      # text_en = It's raining in my house
      1	Il	il	PRON	_	_	2	subj@expl	_	Gloss=it
      2	pleut	pleuvoir	VERB	_	_	0	root	_	Gloss=rains
      3	dans	dans	ADP	_	_	2	mod	_	Gloss=in
      4	ma	son	DET	_	_	5	det	_	Gloss=my
      5	maison	maison	NOUN	_	_	3	comp:obj	_	Gloss=house
{{< /conll >}}

Meanwhile, the sub-relation `subj@pass` is used to indicate a passive construction. This sub-relation can be used for both standard passive constructions, and for mediopassive constructions.
You can find more information about passive constructions on this [page](../../deep_features/pass).

### Passive constructions

> English

{{< conll >}}
      # text = This shall be applauded
      1	This	this	PRON	DT	Number=Sing|PronType=Dem	2	subj@pass	_	Entity=(event-70)
      2	shall	shall	AUX	MD	VerbForm=Fin	0	root	_	_
      3	be	be	AUX	VB	VerbForm=Inf	2	comp:aux	_	_
      4	applauded	applaud	VERB	VBD	Mood=Ind|Tense=Past|VerbForm=Fin	3	comp:aux@pass	_	_
{{< /conll >}}


> French

{{< conll >}}
      # text = Il fut bâti en 1998.
      # text_en = It was build in 1998.
      1	Il	il	PRON	_	_	2	subj@pass	_	Gloss=It
      2	fut	être	AUX	_	_	0	root	_	Gloss=was
      3	bâti	bâtir	VERB	_	_	2	comp:aux@pass	_	Gloss=built
      4	en	en	ADP	_	_	2	mod	_	Gloss=in
      5	1998	1998	NUM	_	_	4	comp:obj	_	Gloss=1998
{{< /conll >}}

### Mediopassive constructions

> Czech

{{< conll >}}
      # text_en = the number of employees decreased
      # text_cs = počet zaměstnanců se snížil
      1	počet	počet	NOUN	_	_	4	subj@pass	_	Gloss=number
      2	zaměstnanců	zaměstnanec	NOUN	_	_	1	mod	_	Gloss=employees.PL.GEN
      3	se	se	PRON	_	_	4	comp@pass	_	Gloss=itself
      4	snížil	snížit	VERB	_	_	0	root	_	Gloss=decrease
{{< /conll >}}

> French

{{< conll >}}
      # text_en = the book is selling well
      # text_cs = le livre se vend bien
      1	le	le	DET	_	_	2	det	_	Gloss=the
      2	livre	livre	NOUN	_	_	4	subj@pass	_	Gloss=book
      3	se	se	PRON	_	_	4	comp@pass	_	Gloss=itself
      4	vend	vendre	VERB	_	_	0	root	_	Gloss=sell
      5	bien	bien	ADV	_	_	4	mod	_	Gloss=well
{{< /conll >}}

> Russian

{{< conll >}}
      # text_en = the book is selling well
      # text_ru = книга хорошо продаётся
      1	книга	книга	NOUN	_	_	3	subj@pass	_	Gloss=book
      2	хорошо	хорошо	ADV	_	_	3	mod	_	Gloss=well
      3	продаётся	продаваться	VERB	_	_	0	root	_	Gloss=is selling
{{< /conll >}}
{{% /expand%}}