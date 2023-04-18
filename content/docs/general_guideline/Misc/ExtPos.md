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

See [Idioms and titles](./extpos/idioms_titles) page for examples of idioms and titles annotations.

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
 * tokens with [`upos=NOUN` and `ExtPos=ADV`](adv.md#upos-noun--extpos--adv) for phrases like *grâce à NOUN*, *face à NOUN* [Grew-match on SUD_French-GSD](http://match.grew.fr/?corpus=SUD_French-GSD@latest&custom=613e0370bf8ee&clustering=N.lemma)
 