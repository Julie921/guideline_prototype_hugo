# Number's annotation

## Written in Letter

[Grew-match](http://universal.grew.fr/?corpus=SUD_French-GSD@latest)
The number written in letter are annoted with the depency [flat](../Syntactic_relations/flat/flat.md)

Numbers composed of more than one word, such as *five hundred* or *six thousand* are primarily chained together with the `flat` relation. If the number contains the coordinating conjunction *and*, such as in *one hundred and one*, the integer directly preceding the coordinating conjunction is connected to one directly following it with a [conj:coord](../Syntactic_relations/conj/conj_coord.md) relation.

> pattern { N1 [upos=NUM]; N2 [upos=NUM]; N1-[flat]->N2 }

> Naija
{{< conll >}}

1	#	#	PUNCT	_	_	3	punct	_	AlignBegin=136812|AlignEnd=137203|Gloss=PUNCT
2	den	den	ADV	_	_	3	mod:periph	_	AlignBegin=137203|AlignEnd=137405|Gloss=den|LeftOverlap=False|RightOverlap=False|Syl1AvgHeightGlo=L|Syl1AvgHeightLoc=M|Syl1Glo=ll|Syl1Loc=mm|Syl1PitchRangeGlo=L|Syl1PitchRangeLoc=L|Syl1SlopeGlo=Flat|Syl1SlopeLoc=Flat|SyllableCount=1|WordContour=ll
3	housing	housing	NOUN	_	_	0	root	_	AlignBegin=137405|AlignEnd=137841|Gloss=housing|LeftOverlap=False|RightOverlap=True|Syl1AvgHeightGlo=M|Syl1AvgHeightLoc=M|Syl1Glo=lh|Syl1Loc=lh|Syl1PitchRangeGlo=M|Syl1PitchRangeLoc=M|Syl1SlopeGlo=Rise|Syl1SlopeLoc=Rise|Syl2AvgHeightGlo=H|Syl2AvgHeightLoc=H|Syl2Glo=mh|Syl2Loc=mh|Syl2PitchRangeGlo=L|Syl2PitchRangeLoc=L|Syl2SlopeGlo=Rise|Syl2SlopeLoc=Rise|Syl3AvgHeightGlo=M|Syl3AvgHeightLoc=M|Syl3Glo=hl|Syl3Loc=hl|Syl3PitchRangeGlo=M|Syl3PitchRangeLoc=M|Syl3SlopeGlo=Fall|Syl3SlopeLoc=Fall|SyllableCount=3|WordContour=lh
4	and	and	CCONJ	_	_	5	cc	_	AlignBegin=137841|AlignEnd=138054|Gloss=and|LeftOverlap=True|RightOverlap=False|Syl1AvgHeightGlo=M|Syl1AvgHeightLoc=M|Syl1Glo=hl|Syl1Loc=hl|Syl1PitchRangeGlo=M|Syl1PitchRangeLoc=M|Syl1SlopeGlo=Fall|Syl1SlopeLoc=Fall|SyllableCount=1|WordContour=hl
5	clothing	clothing	NOUN	_	_	3	conj:coord	_	AlignBegin=138054|AlignEnd=138431|Gloss=clothing|LeftOverlap=False|RightOverlap=True|Syl1AvgHeightGlo=M|Syl1AvgHeightLoc=M|Syl1Glo=mm|Syl1Loc=mm|Syl1PitchRangeGlo=L|Syl1PitchRangeLoc=L|Syl1SlopeGlo=Flat|Syl1SlopeLoc=Flat|Syl2AvgHeightGlo=H|Syl2AvgHeightLoc=M|Syl2Glo=hh|Syl2Loc=mm|Syl2PitchRangeGlo=L|Syl2PitchRangeLoc=L|Syl2SlopeGlo=Flat|Syl2SlopeLoc=Flat|Syl3AvgHeightGlo=M|Syl3AvgHeightLoc=M|Syl3Glo=ml|Syl3Loc=ml|Syl3PitchRangeGlo=L|Syl3PitchRangeLoc=L|Syl3SlopeGlo=Fall|Syl3SlopeLoc=Fall|SyllableCount=3|WordContour=mmh3
6	of	of	ADP	_	_	5	mod	_	AlignBegin=138431|AlignEnd=138534|Gloss=of|LeftOverlap=True|RightOverlap=False|Syl1AvgHeightGlo=M|Syl1AvgHeightLoc=M|Syl1Glo=ml|Syl1Loc=ml|Syl1PitchRangeGlo=L|Syl1PitchRangeLoc=L|Syl1SlopeGlo=Fall|Syl1SlopeLoc=Fall|SyllableCount=1|WordContour=ml
7	sixty	sixty	NUM	_	NumType=Card	6	comp:obj	_	AlignBegin=138534|AlignEnd=138941|Gloss=sixty.CARD|LeftOverlap=False|RightOverlap=False|Syl1AvgHeightGlo=M|Syl1AvgHeightLoc=M|Syl1Glo=lm|Syl1Loc=lm|Syl1PitchRangeGlo=L|Syl1PitchRangeLoc=L|Syl1SlopeGlo=Rise|Syl1SlopeLoc=Rise|Syl2AvgHeightGlo=L|Syl2AvgHeightLoc=L|Syl2Glo=ll|Syl2Loc=ll|Syl2PitchRangeGlo=L|Syl2PitchRangeLoc=L|Syl2SlopeGlo=Flat|Syl2SlopeLoc=Flat|SyllableCount=2|WordContour=llm2
8	five	five	NUM	_	NumType=Card	7	flat	_	AlignBegin=138941|AlignEnd=139261|Gloss=five.CARD|LeftOverlap=False|RightOverlap=False|Syl1AvgHeightGlo=H|Syl1AvgHeightLoc=H|Syl1Glo=hm|Syl1Loc=hm|Syl1PitchRangeGlo=L|Syl1PitchRangeLoc=L|Syl1SlopeGlo=Fall|Syl1SlopeLoc=Fall|SyllableCount=1|WordContour=lmh3
9	million	million	NUM	_	NumType=Card	8	flat	_	AlignBegin=139261|AlignEnd=139604|Gloss=million.CARD|LeftOverlap=False|RightOverlap=False|Syl1AvgHeightGlo=M|Syl1AvgHeightLoc=M|Syl1Glo=mm|Syl1Loc=mm|Syl1PitchRangeGlo=L|Syl1PitchRangeLoc=L|Syl1SlopeGlo=Flat|Syl1SlopeLoc=Flat|Syl2AvgHeightGlo=L|Syl2AvgHeightLoc=M|Syl2Glo=mL|Syl2Loc=hl|Syl2PitchRangeGlo=M|Syl2PitchRangeLoc=M|Syl2SlopeGlo=Fall|Syl2SlopeLoc=Fall|SyllableCount=2|WordContour=mLm1
10	//	//	PUNCT	_	_	3	punct	_	AlignBegin=139604|AlignEnd=139604|Gloss=PUNCT

{{< /conll >}}


> English
{{< conll >}}
1   you you PRON    _   Case=Nom|Person=2|PronType=Prs  2   subj    _   AlignBegin=98152|AlignEnd=98230|Gloss=NOM.2
2   invest  invest  VERB    _   _   0   root    _   AlignBegin=98230|AlignEnd=98757|Gloss=invest
3   #   #   PUNCT   _   _   4   punct   _   AlignBegin=98757|AlignEnd=98980|Gloss=PUNCT
4   one one NUM _ NumType=Card  2 comp:obj  _ AlignBegin=98980|AlignEnd=99090|Gloss=one
5   hundred hundred NUM _ NumType=Card  4 flat  _ AlignBegin=99090|AlignEnd=99390|Gloss=hundred.CARD
6   and and CCONJ _ _ 7 cc  _ AlignBegin=99390|AlignEnd=99520|Gloss=and
7   thirty  thirty  NUM _ NumType=Card  5 conj:coord  _ AlignBegin=99520|AlignEnd=99760|Gloss=thirty.CARD
8   seven seven NUM _ NumType=Card  7 flat  _ AlignBegin=99760|AlignEnd=100080|Gloss=seven.CARD
9   thousand  thousand  NUM _ NumType=Card  8 flat  _ AlignBegin=100080|AlignEnd=100448|Gloss=thousand.CARD
{{< /conll >}}

> French
{{<conll>}}
# text = c'était en deux mille douze.
1	c'	ce	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Dem	2	subj	_	SpaceAfter=No
2	était	être	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	0	root	_	_
3	en	en	ADP	_	_	2	mod	_	_
4	deux	deux	NUM	_	Number=Plur	3	comp:obj	_	_
5	mille	mille	NUM	_	_	4	flat	_	_
6	douze	douze	NUM	_	Number=Plur	5	flat	_	SpaceAfter=No
7	.	.	PUNCT	_	_	2	punct	_	_
{{</conll>}}

## Written in number

The number have the [NUM](../Upos/NUM.md) part of speech


## bejatest

### Overview

## Specific Pattern




## bejatestone

### Overview

### Specific Pattern


