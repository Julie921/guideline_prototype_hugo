### Multi-word placenames and organizations


In Naija, multi-word placenames and organizations are currently annotated with a simple `flat` relation, though their constituents retain their typical parts of speech.
<!-- tabs:start -->
#### **Exampe 1**
{{< conll >}}

1 # # PUNCT _ _ 3 punct _ AlignBegin=102090|AlignEnd=102457|Gloss=PUNCT

2 I I PRON  _ Case=Nom|Number=Sing|Person=1|PronType=Prs  3 subj  _ AlignBegin=102457|AlignEnd=102537|Gloss=NOM.SG.1

3 con con AUX _ Aspect=Cons 0 root  _ AlignBegin=102537|AlignEnd=102657|Gloss=CONS

4 come  come  VERB  _ _ 3 comp:aux  _ AlignBegin=102657|AlignEnd=102837|Gloss=come

5 Port  Port  NOUN  _ _ 4 comp:obj  _ AlignBegin=102837|AlignEnd=102947|ExtPos=PROPN|Gloss=Port|Title=Yes

6 Harcourt  Harcourt  PROPN _ _ 5 flat  _ AlignBegin=102947|AlignEnd=103137|Gloss=Harcourt|InTitle=Yes

7 for for ADP _ _ 4 mod _ AlignBegin=103137|AlignEnd=103261|Gloss=for

8 twenty  twenty  NUM _ NumType=Card  7 comp:obj  _ AlignBegin=103261|AlignEnd=103704|Gloss=twenty.CARD

9 fourteen  fourteen  NUM _ NumType=Card  8 flat  _ AlignBegin=103704|AlignEnd=104330|Gloss=fourteen.CARD

10  //  //  PUNCT _ _ 3 punct _ AlignBegin=104330|AlignEnd=104360|Gloss=PUNCT

{{< /conll >}}

#### **Exampe 2**

{{< conll >}}

1 # # PUNCT _ _ 3 punct _ AlignBegin=4080|AlignEnd=4899|Gloss=PUNCT

2 de  dem PRON  _ Case=Nom|Number=Plur|Person=3|PronType=Prs  3 subj  _ AlignBegin=4899|AlignEnd=5016|Gloss=NOM.PL.3

3 bin bin AUX _ Tense=Past  0 root  _ AlignBegin=5016|AlignEnd=5131|Gloss=PST

4 born  born  VERB  _ _ 3 comp:aux  _ AlignBegin=5131|AlignEnd=5296|Gloss=give_birth

5 me  me  PRON  _ Case=Acc|Number=Sing|Person=1|PronType=Prs  4 comp:obj  _ AlignBegin=5296|AlignEnd=5360|Gloss=ACC.SG.1

6 for for ADP _ _ 4 comp:obl  _ AlignBegin=5360|AlignEnd=5856|Gloss=for

7 Wuse  Wuse  PROPN _ _ 6 comp:obj  _ AlignBegin=5856|AlignEnd=6183|ExtPos=PROPN|Gloss=Wuse|Title=Yes

8 General general ADJ _ _ 7 flat  _ AlignBegin=6183|AlignEnd=6580|Gloss=general|InTitle=Yes

9 Hospital  hospital  NOUN  _ _ 8 flat  _ AlignBegin=6580|AlignEnd=7052|Gloss=hospital|InTitle=Yes

10  //  //  PUNCT _ _ 3 punct _ AlignBegin=7052|AlignEnd=7082|Gloss=PUNCT

{{< /conll >}}

#### **Example 3**

{{< conll >}}

1 Manchester  Manchester  PROPN _ _ 7 dislocated  _ AlignBegin=118620|AlignEnd=119365|ExtPos=PROPN|Gloss=Manchester|Title=Yes

2 United  United  ADJ _ _ 1 flat  _ AlignBegin=119365|AlignEnd=120036|Gloss=United|InTitle=Yes

3 < < PUNCT _ _ 1 punct _ AlignBegin=120036|AlignEnd=120066|Gloss=PUNCT

4 oh  oh  INTJ  _ _ 7 discourse _ AlignBegin=120066|AlignEnd=120355|Gloss=oh

5 dis dis DET _ Number=Sing|PronType=Dem  7 det _ AlignBegin=120355|AlignEnd=120625|Gloss=SG.DEM

6 ball  ball  NOUN  _ _ 7 compound  _ AlignBegin=120625|AlignEnd=120905|Gloss=ball

7 club  club  NOUN  _ _ 0 root  _ AlignBegin=120905|AlignEnd=121280|Gloss=club

8 !// !// PUNCT _ _ 7 punct _ AlignBegin=121280|AlignEnd=121310|Gloss=PUNCT

{{< /conll >}}
<!-- tabs:end -->
  