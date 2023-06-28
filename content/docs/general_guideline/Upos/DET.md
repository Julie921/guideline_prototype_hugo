---
title: "DET"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

#  Determinant  

##  Universal  

*Definition from de [UD website](https://universaldependencies.org/u/pos/DET.html)*

Determiners are words that modify nouns or noun phrases and express the reference of the noun phrase in context. That is, a determiner may indicate whether the noun is referring to a definite or indefinite element of a class, to a closer or more distant element, to an element belonging to a specified person or thing, to a particular number or quantity, etc.

Determiners under this definition include both articles and pro-adjectives (pronominal adjectives), which is a slightly broader sense than what is usually regarded as determiners in English. In particular, there is no general requirement that a nominal can be modified by at most one determiner, although some languages may show a strong tendency towards such a constraint. (For example, an English nominal usually allows only one DET modifier, but there are occasional cases of addeterminers, which appear outside the usual determiner, such as [en] all in all the children survived. In such cases, both all and the are given the POS DET.)

Note that the DET tag includes (pronominal) quantifiers (words like many, few, several), which are included among determiners in some languages but may belong to numerals in others. However, cardinal numerals in the narrow sense (one, five, hundred) are not tagged DET even though some authors would include them in quantifiers. Cardinal numbers have their own tag NUM.

Also note that the notion of determiners is unknown in traditional grammar of some languages (e.g. Czech); words equivalent to English determiners may be traditionally classified as pronouns and/or numerals in these languages. In order to annotate the same thing the same way across languages, the words satisfying our definition of determiners should be tagged DET in these languages as well.

It is not always crystal clear where pronouns end and determiners start. Unlike in UD v1 it is no longer required that they are told apart solely on the base of the context. The words can be pre-classified in the dictionary as either PRON or DET, based on their typical syntactic distribution (and morphology, when applicable). Language-specific documentation should list all determiners (it is a closed class) and point out ambiguities, if any.

See also general principles on pronominal words for more tips on how to define determiners. In particular:

- Articles (the, a, an) are always tagged DET; their PronType is Art.
- Pronominal numerals (quantifiers) are tagged DET; besides PronType, they also use the NumType feature.
- Words that behave similar to adjectives are DET. Similar behavior means:
    - They are more likely to be used attributively (modifying a noun phrase) than substantively (replacing a noun phrase). They may occur alone, though. If they do, it is either because of ellipsis, or because the hypothetical modified noun is something unspecified and general, as in All [visitors] must pay.
    - Their inflection (if applicable) is similar to that of adjectives, and distinct from nouns. They agree with the nouns they modify. Especially the ability to inflect for gender is typical for adjectives and determiners. (Gender of nouns is determined lexically and determiners may be required by the grammar to agree with their nouns in gender; therefore they need to inflect for gender.)
- Possessives vary across languages. In some languages the above tests put them in the DET category. In others, they are more like a normal personal pronoun in a specific case (often the genitive), or a personal pronoun with an adposition; they are tagged PRON.

Examples
- articles (a closed class indicating definiteness, specificity or givenness): a, an, the
possessive determiners (which modify a nominal) (note that some languages use PRON for similar words): [cs] můj, tvůj, jeho, její, náš, váš, jejich
- demonstrative determiners: this as in I saw this car yesterday.
- interrogative determiners: which as in “Which car do you like?”
- relative determiners: which as in “I wonder which car you like.”
- quantity determiners (quantifiers): indefinite any, universal: all, and negative no as in “We have no cars available.”


## french

TODO
### Overview

### Specific Pattern






## haitien

### Overview

 Determiners are words that modify nouns or noun phrases and express the reference of the noun phrase in context. In Haitian Creole the determiners are placed always after a noun. However, the "yon" determiner has an exceptional behaviour and is placed before a noun. 

{{<conll>}} 
# sent_id = my_sample__3
# text = Koup la tap vizite fanmi yo an Ayiti epi asiste yon festival lè yo te kidnape yo nan yon otobis, dapre sa yon manm fanmi yo di CNN.
# text_fr = Le couple visitait leur famille en Haïti et assistait à un festival quand ils les ont kidnappés dans un autobus, d'après ce qu'un membre de leur famille a dit à CNN.
1	Koup	Koup	NOUN	_	_	4	subj	_	Gloss=couple
2	la	la	DET	_	Definite=Def|Number=Sing	1	det	_	Gloss=le
3	tap	tap 	AUX	_	_	4	aux	_	Gloss=  PAST PROG
4	vizite	vizite 	VERB	_	Number=Sing|Person=3|Tense=Imp	0	root	_	Gloss=visiter
5	fanmi	fanmi 	NOUN	_	_	4	comp:obj	_	Gloss=famille
6	yo	yo	PRON	_	Number=Sing|Person=3|Poss=Yes	5	det	_	Gloss=PRON
7	an	an	ADP	_	_	4	mod	_	Gloss=en
8	Ayiti	Ayiti	PROPN	_	_	7	comp:obj	_	Gloss=Haïti
9	epi	epi	CCONJ	_	_	10	cc	_	Gloss=puis
10	asiste	asiste 	VERB	_	Number=Sing|Person=3|Tense=Imp	4	conj	_	Gloss=assister
11	yon	yon 	DET	_	Definite=Ind|Number=Sing	12	det	_	Gloss=un
12	festival	festival	NOUN	_	_	10	comp:obj	_	Gloss=festival
13	lè	lè	SCONJ	_	_	10	mod	_	Gloss=quand
14	yo	yo	PRON	_	Number=Plur|Person=3|PronType=Prs	16	subj	_	Gloss=PRON
15	te	te	AUX	_	_	16	aux	_	Gloss=PAST
16	kidnape	kidnape 	VERB	_	Number=Plur|Person=3|Tense=Past	13	comp:obj	_	Gloss=kidnapper
17	yo	yo	PRON	_	Definite=Def|Number=Plur	16	comp:obj	_	Gloss=les
18	nan	nan	ADP	_	_	16	mod	_	Gloss=dans
19	yon	yon 	DET	_	Definite=Ind|Number=Sing	20	det	_	Gloss=un
20	otobis	otobis 	NOUN	_	_	18	comp:obj	_	Gloss=autobus|SpaceAfter=No
21	,	, 	PUNCT	_	_	16	punct	_	_
22	dapre	dapre	ADP	_	_	4	mod	_	Gloss=d'après
23	sa	sa 	PRON	_	_	22	comp:obj	_	Gloss=cela
24	yon	yon	DET	_	Definite=Ind|Number=Sing	25	det	_	Gloss=un
25	manm	manm	NOUN	_	_	28	subj	_	Gloss=membre
26	fanmi	fanmi	NOUN	_	_	25	udep	_	Gloss=famille
27	yo	yo	PRON	_	Definite=Def|Number=Plur	26	det	_	Gloss=PRON
28	di	di	VERB	_	Number=Sing|Person=3|Tense=Past	23	mod@relcl	_	Gloss=dire
29	CNN	CNN	NOUN	_	_	28	comp:obj@R	_	Gloss=CNN|SpaceAfter=No
30	.	.	PUNCT	_	_	28	punct	_	_

{{</conll>}}

- The upos  has the values : ['']


### Specific Pattern

#### Yon determiner 

- Description: The "yon" determiner is an equivalent of an indefinite singular article. It has an exceptional behaviour compared to other determiners in Haitian Creole and it is always placed before a noun. 

- Pattern: GOV -[det]-> DEP; DEP[lemma=yon]


{{<conll>}}
# sent_id = my_sample__5
# text = Lè yon sitwayen Ameriken disparèt, nou travay sere-sere ak otorite lokal yo pandan yap chache moun sa yo e nou pataje enfòmasyon ak fanmi yo nempòt kijan nou kapab."
# text_fr = Quand un citoyen américain disparait, nous travaillons étroitement avec les autorités locales pendant qu'ils cherchent ces gens et nous partageons des informations avec leur famille  n'importe quelle façon dont nous pouvons.
1	Lè	Lè	ADV	_	_	8	mod	_	Gloss=Quand
2	yon	yon	DET	_	Definite=Ind|Number=Sing	3	det	_	Gloss=un
3	sitwayen	sitwayen	NOUN	_	_	5	subj	_	Gloss=citoyen
4	Ameriken	Ameriken	ADJ	_	_	3	mod	_	Gloss=américain
5	disparèt	disparèt	VERB	_	Number=Sing|Person=3|Tense=Pres	1	comp:obj	_	Gloss=disparaitre|SpaceAfter=No
6	,	,	PUNCT	_	_	5	punct	_	_
7	nou	nou	PRON	_	Number=Plur|Person=1|PronType=Prs	8	subj	_	Gloss=PRON
8	travay	travay 	VERB	_	Number=Plur|Person=1|Tense=Pres	0	root	_	Gloss=travailler
9	sere-sere	sere-sere	ADV	_	_	8	mod	_	Gloss=étroitement
10	ak	ak	CCONJ	_	_	8	udep	_	Gloss=avec
11	otorite	otorite 	NOUN	_	_	10	comp:obj	_	Gloss=autorité
12	lokal	lokal	ADJ	_	_	11	mod	_	Gloss=local
13	yo	yo	DET	_	Definite=Def|Number=Plur	11	det	_	Gloss=les
14	pandan	pandan 	ADP	_	_	8	mod	_	Gloss=pendant
15	yap	yap	AUX	_	_	16	subj:aux	_	Gloss=PROG
16	chache	chache	VERB	_	Number=Plur|Person=3|Tense=Pres	14	comp:obj	_	Gloss=chercher
17	moun	moun	NOUN	_	_	16	comp:obj	_	Gloss=gens
18	sa	sa	PRON	_	_	17	det	_	_
19	yo	yo	PRON	_	Number=Plur|PronType=Dem	18	mod	_	Gloss=ces
20	e	e	CCONJ	_	_	22	cc	_	Gloss=et
21	nou	nou	PRON	_	Number=Plur|Person=1|PronType=Prs	22	subj	_	Gloss=nous
22	pataje	pataje	VERB	_	Number=Plur|Person=1|Tense=Pres	8	conj:coord	_	Gloss=partageons
23	enfòmasyon	enfòmasyon 	NOUN	_	_	22	comp:obj	_	Gloss=informations
24	ak	ak	CCONJ	_	_	22	comp:obl	_	Gloss=avec
25	fanmi	fanmi	NOUN	_	_	24	comp:obj	_	Gloss=familles
26	yo	yo	DET	_	Number=Plur|Poss=Yes	25	det	_	Gloss=PRON
27	nenpòt	nenpòt 	ADV	_	_	30	mod	_	Gloss=n'importe
28	kijan	kijan	ADV	_	_	27	unk	_	Gloss=comment
29	nou	nou	PRON	_	Number=Sing|Person=1|PronType=Prs	30	subj	_	Gloss=PRON
30	kapab	kapab	VERB	_	Number=Sing|Person=1|Tense=Pres	25	mod@relcl	_	Gloss=pouvoir|SpaceAfter=No
31	."	."	PUNCT	_	_	8	punct	_	_

{{</conll>}}

#### Tables

 Here is the table where you can find the pattern in the treebanks.

{{< agg table_output_haitien_DET >}}
 



