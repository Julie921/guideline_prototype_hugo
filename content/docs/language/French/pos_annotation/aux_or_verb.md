# AUX or VERB ?

It is sometimes not trivial to chose between the part of speech `AUX` and `VERB` for **être**. We propose this distinction : 
- when **être** has a predicative complement, it is always considered as a copula and it has the POS `AUX` 

**Example**


- when **être** has an existensial meaning (*je pense donc je suis* -***I think therefore I am***) or has a locative argument or another argument, which is not a predicative argument (*je suis pour la dépénalisation du cannabis* -***I am for the decriminalization of cannabis***), it has the POS `VERB`.

## Locativ argument
{{< conll >}}
# text = Ils sont sur Cherbourg depuis 2007.
1	Ils	eux	PRON	_	Emph=No|Gender=Masc|Number=Plur|Person=3|PronType=Prs	2	subj	_	wordform=ils
2	sont	être	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	_
3	sur	sur	ADP	_	_	2	comp:obl	_	_
4	Cherbourg	Cherbourg	PROPN	_	_	3	comp:obj	_	_
5	depuis	depuis	ADP	_	_	2	mod	_	_
6	2007	2007	NUM	_	Number=Plur	5	comp:obj	_	SpaceAfter=No
7	.	.	PUNCT	_	_	2	punct	_	_
{{< /conll >}}

## Existensial meaning
{{< conll >}}
# text = Pourquoi en serait-il autrement cette fois-ci ?
1	Pourquoi	pourquoi	ADV	_	_	3	mod	_	wordform=pourquoi
2	en	en	PRON	_	Emph=No|Person=3|PronType=Prs	3	comp@expl	_	_
3	serait	être	VERB	_	Mood=Cnd|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	SpaceAfter=No
4	-il	lui	PRON	_	Emph=No|Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	subj	_	wordform=il
5	autrement	autrement	ADV	_	_	3	mod	_	_
9	?	?	PUNCT	_	_	3	punct	_	_
{{< /conll >}}

>[!NOTE]
> you can find the discussion about the distinction between `AUX` and `VERB` [here](https://github.com/surfacesyntacticud/guidelines/issues/11)

**Table**

{{< hint danger >}}

WARNING : cette table ne renvoie pas vers les requêtes grew car j'utilise le lemme "être" et il y a un problème d'encodage.

{{< /hint >}}

{{< agg etre_aux_verb >}}
