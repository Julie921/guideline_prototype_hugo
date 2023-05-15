### Numbers and dates


If the number contains a decimal, the *point* is marked as a noun and is integrated into the number with a simple `flat` relation.  

{{< conll >}}

1 one one NUM _ NumType=Card  0 det:num _ AlignBegin=17090|AlignEnd=17300|Gloss=one

2 hundred hundred NUM _ NumType=Card  1 flat  _ AlignBegin=17300|AlignEnd=17580|Gloss=hundred.CARD

3 and and CCONJ _ _ 4 cc  _ AlignBegin=17580|AlignEnd=17700|Gloss=and

4 fifty fifty NUM _ NumType=Card  2 conj:coord  _ AlignBegin=17700|AlignEnd=18000|Gloss=fifty.CARD

5 six six NUM _ NumType=Card  4 flat  _ AlignBegin=18000|AlignEnd=18300|Gloss=six.CARD

6 point point NOUN  _ _ 5 flat  _ AlignBegin=18300|AlignEnd=18480|Gloss=point

7 six six NUM _ NumType=Card  6 flat  _ AlignBegin=18480|AlignEnd=18785|Gloss=six.CARD

8 billion billion NUM _ _ 7 flat  _ AlignBegin=19379|AlignEnd=19980|Gloss=billion

{{< /conll >}}

  
  

If numerals are listed a sequence, such as in telephone numbers, the constituents are chained together with the `conj:coord` relation.

{{< conll >}}

1 # # PUNCT _ _ 2 punct _ AlignBegin=573880|AlignEnd=574100|Gloss=PUNCT

2 zero  zero  NUM _ NumType=Card  0 root  _ AlignBegin=574100|AlignEnd=574380|Gloss=zero.CARD

3 nine  nine  NUM _ NumType=Card  2 conj:coord  _ AlignBegin=574380|AlignEnd=574590|Gloss=nine.CARD

4 zero  zero  NUM _ NumType=Card  3 conj:coord  _ AlignBegin=574590|AlignEnd=575100|Gloss=zero.CARD

5 nine  nine  NUM _ NumType=Card  4 conj:coord  _ AlignBegin=575100|AlignEnd=575394|Gloss=nine.CARD

6 five  five  NUM _ NumType=Card  5 conj:coord  _ AlignBegin=575394|AlignEnd=575700|Gloss=five.CARD

7 # # PUNCT _ _ 8 punct _ AlignBegin=575700|AlignEnd=576060|Gloss=PUNCT

8 nine  nine  NUM _ NumType=Card  6 conj:coord  _ AlignBegin=576060|AlignEnd=576294|Gloss=nine.CARD

9 six six NUM _ NumType=Card  8 conj:coord  _ AlignBegin=576294|AlignEnd=576640|Gloss=six.CARD

10  five  five  NUM _ NumType=Card  9 conj:coord  _ AlignBegin=576640|AlignEnd=576930|Gloss=five.CARD

11  three three NUM _ NumType=Card  10  conj:coord  _ AlignBegin=576930|AlignEnd=577143|Gloss=three.CARD

12  two two NUM _ NumType=Card  11  conj:coord  _ AlignBegin=577143|AlignEnd=577280|Gloss=two.CARD

13  nine  nine  NUM _ NumType=Card  12  conj:coord  _ AlignBegin=577280|AlignEnd=577429|Gloss=nine.CARD

{{< /conll >}}

  
  

Note that references to radio stations which use this format nevertheless contain a `flat` relation. This is because we consider that the frequency number effectively functions as a title.

{{< conll >}}

1 Bronze  bronze  NOUN  _ _ 0 comp:obj  _ AlignBegin=166800|AlignEnd=167090|ExtPos=PROPN|Gloss=bronze|Title=Yes

2 FM  FM  NOUN  _ _ 1 flat  _ AlignBegin=167090|AlignEnd=167559|Gloss=FM|InTitle=Yes

3 |a  |a  PUNCT _ _ 4 punct _ AlignBegin=167559|AlignEnd=167589|Gloss=PUNCT

4 one one NUM _ NumType=Card  2 mod:appos _ AlignBegin=167589|AlignEnd=167780|Gloss=one

5 o o NUM _ _ 4 flat  _ AlignBegin=167780|AlignEnd=167870|Gloss=o

6 one one NUM _ NumType=Card  5 flat  _ AlignBegin=167870|AlignEnd=168040|Gloss=one

7 dot dot NOUN  _ _ 6 flat  _ AlignBegin=168040|AlignEnd=168260|Gloss=dot

8 five  five  NUM _ NumType=Card  7 flat  _ AlignBegin=168260|AlignEnd=168450|Gloss=five.CARD

{{< /conll >}}

  
  

When annotating dates, the `mod:appos` relation is used to connect the month to the numerical day. Meanwhile, the year is connected to the month using the `mod` relation.  

{{< conll >}}

1 sey sey SCONJ _ _ 2 discourse _ AlignBegin=49550|AlignEnd=49730|Gloss=COMP

2 make  make  AUX _ Mood=Opt  0 root  _ AlignBegin=49760|AlignEnd=50050|Gloss=SBJV

3 de  dem PRON  _ Case=Nom|Number=Plur|Person=3|PronType=Prs  4 subj  _ AlignBegin=50050|AlignEnd=50265|Gloss=NOM.PL.3

4 do  do  VERB  _ _ 2 comp:aux  _ AlignBegin=50265|AlignEnd=50510|Gloss=do

5 am  am  PRON  _ Case=Acc|Number=Sing|Person=3|PronType=Prs  4 comp:obj  _ AlignBegin=50510|AlignEnd=50717|Gloss=ACC.SG.3

6 # # PUNCT _ _ 7 punct _ AlignBegin=50717|AlignEnd=51078|Gloss=PUNCT

7 before  before  ADP _ _ 4 mod _ AlignBegin=51078|AlignEnd=51590|Gloss=before

8 August  August  PROPN _ _ 7 comp:obj  _ AlignBegin=51590|AlignEnd=52162|Gloss=August

9 # # PUNCT _ _ 10  punct _ AlignBegin=52162|AlignEnd=52331|Gloss=PUNCT

10  twenty  twenty  NUM _ NumType=Card  8 mod:appos _ AlignBegin=52331|AlignEnd=52600|Gloss=twenty.CARD

11  fourth  fourth  ADJ _ NumType=Ord 10  flat  _ AlignBegin=52600|AlignEnd=53020|Gloss=fourth.ORD

12  two two NUM _ NumType=Card  8 mod _ AlignBegin=53020|AlignEnd=53224|Gloss=two.CARD

13  thousand  thousand  NUM _ NumType=Card  12  flat  _ AlignBegin=53224|AlignEnd=53570|Gloss=thousand.CARD

14  and and CCONJ _ _ 15  cc  _ AlignBegin=53570|AlignEnd=53813|Gloss=and

15  eighteen  eighteen  NUM _ NumType=Card  13  conj:coord  _ AlignBegin=53813|AlignEnd=54463|Gloss=eighteen.CARD

16  //  //  PUNCT _ _ 2 punct _ AlignBegin=54463|AlignEnd=54493|Gloss=PUNCT

{{< /conll >}}

  