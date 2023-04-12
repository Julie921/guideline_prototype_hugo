# Number's annotation
**Written in Letter**
[Grew-match](http://universal.grew.fr/?corpus=SUD_French-GSD@latest)
The number written in letter are annoted with the depency `flat`

Numbers composed of more than one word, such as *five hundred* or *six thousand* are primarily chained together with the `flat` relation. If the number contains the coordinating conjunction *and*, such as in *one hundred and one*, the integer directly preceding the coordinating conjunction is connected to one directly following it with a `conj:coord` relation.

>[!tip]
> pattern { N1 [upos=NUM]; N2 [upos=NUM]; N1-[flat]->N2 }

<!-- tabs:start -->
#### **Naija**
{{< conll >}}

1 # # PUNCT _ _ 3 punct _ AlignBegin=136812|AlignEnd=137203|Gloss=PUNCT

2 den dem ADV _ _ 3 mod:periph  _ AlignBegin=137203|AlignEnd=137405|Gloss=den

3 housing housing NOUN  _ _ 0 root  _ AlignBegin=137405|AlignEnd=137841|Gloss=housing

4 and and CCONJ _ _ 5 cc  _ AlignBegin=137841|AlignEnd=138054|Gloss=and

5 clothing  clothing  NOUN  _ _ 3 conj:coord  _ AlignBegin=138054|AlignEnd=138431|Gloss=clothing

6 of  of  ADP _ _ 5 mod _ AlignBegin=138431|AlignEnd=138534|Gloss=of

7 sixty sixty NUM _ NumType=Card  6 comp:obj  _ AlignBegin=138534|AlignEnd=138941|Gloss=sixty.CARD

8 five  five  NUM _ NumType=Card  7 flat  _ AlignBegin=138941|AlignEnd=139261|Gloss=five.CARD

9 million million NUM _ NumType=Card  8 flat  _ AlignBegin=139261|AlignEnd=139574|Gloss=million.CARD

10  //  //  PUNCT _ _ 3 punct _ AlignBegin=139574|AlignEnd=139604|Gloss=PUNCT

{{< /conll >}}


#### **English**

{{< conll >}}

1 you you PRON  _ Case=Nom|Person=2|PronType=Prs  2 subj  _ AlignBegin=98152|AlignEnd=98230|Gloss=NOM.2

2 invest  invest  VERB  _ _ 0 root  _ AlignBegin=98230|AlignEnd=98757|Gloss=invest

3 # # PUNCT _ _ 4 punct _ AlignBegin=98757|AlignEnd=98980|Gloss=PUNCT

4 one one NUM _ NumType=Card  2 comp:obj  _ AlignBegin=98980|AlignEnd=99090|Gloss=one

5 hundred hundred NUM _ NumType=Card  4 flat  _ AlignBegin=99090|AlignEnd=99390|Gloss=hundred.CARD

6 and and CCONJ _ _ 7 cc  _ AlignBegin=99390|AlignEnd=99520|Gloss=and

7 thirty  thirty  NUM _ NumType=Card  5 conj:coord  _ AlignBegin=99520|AlignEnd=99760|Gloss=thirty.CARD

8 seven seven NUM _ NumType=Card  7 flat  _ AlignBegin=99760|AlignEnd=100080|Gloss=seven.CARD

9 thousand  thousand  NUM _ NumType=Card  8 flat  _ AlignBegin=100080|AlignEnd=100448|Gloss=thousand.CARD

{{< /conll >}}
<!-- tabs:end -->



