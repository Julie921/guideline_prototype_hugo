### Cleft sentences and questions

  

Cleft sentences are an extremely common construction in Naija, making the `comp:cleft` relation a particularly important for the the annotation of this language. The basic cleft construction in Naija includes the phrase *na im* (it's him), followed by a verb phrase, though a number of variants exist. The following provides several such examples.

  
<!-- tabs:start -->
#### **Example 1**
{{< conll >}}

1 laziness  laziness  NOUN  _ _ 3 dislocated  _ AlignBegin=370809|AlignEnd=371360|Gloss=laziness

2 < < PUNCT _ _ 1 punct _ AlignBegin=371360|AlignEnd=371390|Gloss=PUNCT

3 na  na  PART  _ PartType=Cop  0 root  _ AlignBegin=371390|AlignEnd=371510|ExtPos=SCONJ|Gloss=be|Idiom=Yes

4 im  im  PRON  _ Case=Nom|Number=Sing|Person=3|PronType=Prs  3 comp:pred _ AlignBegin=371510|AlignEnd=371563|Gloss=NOM.SG.3

5 >+  >+  PUNCT _ _ 6 punct _ AlignBegin=371563|AlignEnd=371563|Gloss=PUNCT

6 scatter scatter VERB  _ _ 3 comp:cleft  _ AlignBegin=371563|AlignEnd=371990|Gloss=scatter

7 you you PRON  _ Case=Nom|Person=2|PronType=Prs  6 comp:obj  _ AlignBegin=371990|AlignEnd=372090|Gloss=NOM.2

8 //  //  PUNCT _ _ 3 punct _ AlignBegin=372090|AlignEnd=372120|Gloss=PUNCT  

{{< /conll >}}

#### **Example 2**  

{{< conll >}}

1 after after ADP _ _ 4 mod:periph  _ AlignBegin=161950|AlignEnd=162120|Gloss=after

2 all all DET _ _ 1 comp:obj  _ AlignBegin=162120|AlignEnd=162160|Gloss=all

3 < < PUNCT _ _ 1 punct _ AlignBegin=162160|AlignEnd=162190|Gloss=PUNCT

4 na  na  PART  _ PartType=Cop  0 root  _ AlignBegin=162190|AlignEnd=162340|Gloss=be

5 Warri Warri PROPN _ _ 4 comp:pred _ AlignBegin=162340|AlignEnd=162524|Gloss=Warri

6 >+  >+  PUNCT _ _ 8 punct _ AlignBegin=162524|AlignEnd=162554|Gloss=PUNCT

7 you you PRON  _ Case=Nom|Person=2|PronType=Prs  8 subj  _ AlignBegin=162554|AlignEnd=162677|Gloss=NOM.2

8 grow  grow  VERB  _ _ 4 comp:cleft  _ AlignBegin=162677|AlignEnd=162890|Gloss=grow

9 up  up  ADP _ _ 8 compound:prt  _ AlignBegin=162890|AlignEnd=162990|Gloss=up

{{< /conll >}}

  
#### **Example 3** 

{{< conll >}}

1 na  na  PART  _ PartType=Cop  0 root  _ AlignBegin=39139|AlignEnd=39299|Gloss=be

2 so  so  ADV _ _ 1 comp:pred _ AlignBegin=39299|AlignEnd=39389|Gloss=so

3 >+  >+  PUNCT _ _ 5 punct _ AlignBegin=39389|AlignEnd=39419|Gloss=PUNCT

4 Oyibo Oyinbo  PROPN _ _ 5 subj  _ AlignBegin=39419|AlignEnd=39719|Gloss=foreign(er)

5 call  call  VERB  _ _ 1 comp:cleft  _ AlignBegin=39719|AlignEnd=39895|Gloss=call

6 am  am  PRON  _ Case=Acc|Number=Sing|Person=3|PronType=Prs  5 comp:obj  _ AlignBegin=39895|AlignEnd=39968|Gloss=ACC.SG.3

7 //  //  PUNCT _ _ 1 punct _ AlignBegin=39968|AlignEnd=39998|Gloss=PUNCT

{{< /conll >}}

#### **Example 4**

{{< conll >}}

1 # # PUNCT _ _ 3 punct _ AlignBegin=271340|AlignEnd=278340|Gloss=PUNCT

2 hm  hm  INTJ  _ _ 3 discourse _ AlignBegin=276082|AlignEnd=276400|Gloss=hm

3 na  na  PART  _ PartType=Cop  0 root  _ AlignBegin=276400|AlignEnd=276540|Gloss=be

4 dem dem PRON  _ Case=Nom|Number=Plur|Person=3|PronType=Prs  3 comp:pred _ AlignBegin=276540|AlignEnd=276680|Gloss=NOM.PL.3

5 >+  >+  PUNCT _ _ 6 punct _ AlignBegin=276680|AlignEnd=276710|Gloss=PUNCT

6 start start VERB  _ _ 3 comp:cleft  _ AlignBegin=276710|AlignEnd=276930|Gloss=start

7 to  to  ADP _ _ 6 comp:obl@x  _ AlignBegin=276930|AlignEnd=277060|Gloss=to

8 dey dey AUX _ Aspect=Imp  7 comp:obj  _ AlignBegin=277060|AlignEnd=277208|Gloss=IPFV

9 do  do  VERB  _ _ 8 comp:aux  _ AlignBegin=277208|AlignEnd=277350|Gloss=do

10  am  am  PRON  _ Case=Acc|Number=Sing|Person=3|PronType=Prs  9 comp:obj  _ AlignBegin=277350|AlignEnd=277600|Gloss=ACC.SG.3

11  //  //  PUNCT _ _ 3 punct _ AlignBegin=277600|AlignEnd=277630|Gloss=PUNCT

{{< /conll >}}
<!-- tabs:end -->
  
  

The `comp:cleft` relation is also used in questions containing interrogative words such as *who* or *where*. In such cases, the wh-word is annotated as the root, and is connected to the verb via a `comp:cleft` relation.

  
<!-- tabs:start -->
#### **Example 1**
{{< conll >}}

1 # # PUNCT _ _ 2 punct _ AlignBegin=139780|AlignEnd=140131|Gloss=PUNCT

2 who who PRON  _ PronType=Int  0 root  _ AlignBegin=140131|AlignEnd=140320|Gloss=who.Q

3 you you PRON  _ Case=Nom|Person=2|PronType=Prs  4 subj  _ AlignBegin=140320|AlignEnd=140540|Gloss=NOM.2

4 work  work  VERB  _ _ 2 comp:cleft  _ AlignBegin=140540|AlignEnd=140720|Gloss=work

5 for for ADP _ _ 4 comp:obl  _ AlignBegin=140720|AlignEnd=140950|Gloss=for

6 ?// ?// PUNCT _ _ 2 punct _ AlignBegin=140950|AlignEnd=140980|Gloss=PUNCT

{{< /conll >}}

#### **Example 2**  

{{< conll >}}

1 wetin wetin PRON  _ PronType=Int  0 root  _ AlignBegin=134010|AlignEnd=134323|Gloss=what.Q

2 be  be  VERB  _ PartType=Cop  1 comp:cleft  _ AlignBegin=134323|AlignEnd=134462|Gloss=be

3 Ponzi Ponzi PROPN _ _ 4 compound  _ AlignBegin=134462|AlignEnd=134803|Gloss=Ponzi

4 Scheme  scheme  NOUN  _ _ 2 comp:pred@agent _ AlignBegin=134803|AlignEnd=135070|Gloss=scheme

5 ?// ?// PUNCT _ _ 1 punct _ AlignBegin=135070|AlignEnd=135100|Gloss=PUNCT

{{< /conll >}}

#### **Example 3** 

{{< conll >}}

1 # # PUNCT _ _ 2 punct _ AlignBegin=69065|AlignEnd=69421|Gloss=PUNCT

2 where where ADV _ PronType=Int  0 root  _ AlignBegin=69421|AlignEnd=69661|Gloss=where.Q

3 di  di  DET _ Definite=Def|PronType=Art 4 det _ AlignBegin=69661|AlignEnd=69761|Gloss=DEF.ART

4 money money NOUN  _ _ 5 subj  _ AlignBegin=69761|AlignEnd=70024|Gloss=money

5 dey dey AUX _ Aspect=Imp  2 comp:cleft  _ AlignBegin=70024|AlignEnd=70194|Gloss=IPFV

6 go  go  VERB  _ _ 5 comp:aux  _ AlignBegin=70194|AlignEnd=70349|Gloss=go

7 ?// ?// PUNCT _ _ 2 punct _ AlignBegin=70349|AlignEnd=70379|Gloss=PUNCT

{{< /conll >}}

<!-- tabs:end -->