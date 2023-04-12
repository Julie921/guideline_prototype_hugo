### Compounds and phrasal verbs

  

Our annotation of Naija makes frequent use of the `compound` relation. In our annotation system, this relation is systematically applied to relationships between two nouns in which one of them acts as a form of modifier. In this sense, `compound` functions much like the `mod` relation, except that it links two nouns together rather than a noun to an adjective.

  
<!-- tabs:start -->
#### **Example 1**
{{< conll >}}

1 no  no  PART  _ Polarity=Neg  2 mod _ AlignBegin=62165|AlignEnd=62648|Gloss=NEG

2 be  be  VERB  _ PartType=Cop  0 root  _ AlignBegin=62648|AlignEnd=63130|Gloss=be

3 children  child NOUN  _ Number=Plur 4 compound  _ AlignBegin=63130|AlignEnd=63612|Gloss=child.PL

4 food  food  NOUN  _ _ 2 comp:pred _ AlignBegin=63612|AlignEnd=64095|Gloss=food

5 ? ? PUNCT _ _ 2 punct _ AlignBegin=64095|AlignEnd=64095|Gloss=PUNCT

{{< /conll >}}

  
#### **Example 2**  

{{< conll >}}

1 I I PRON  _ Case=Nom|Number=Sing|Person=1|PronType=Prs  2 subj  _ AlignBegin=59955|AlignEnd=60188|Gloss=I

2 know  know  VERB  _ _ 0 root  _ AlignBegin=60188|AlignEnd=60420|Gloss=know

3 banga banga NOUN  _ _ 4 compound  _ AlignBegin=60420|AlignEnd=60652|Gloss=palm_kernel

4 soup  soup  NOUN  _ _ 2 comp:obj  _ AlignBegin=60652|AlignEnd=60885|Gloss=soup

5 . . PUNCT _ _ 2 punct _ AlignBegin=60885|AlignEnd=60885|Gloss=PUNCT

{{< /conll >}}

  
#### **Example 3**

{{< conll >}}

1 she she PRON  _ Case=Nom|Gender=Fem|Number=Sing|Person=3|PronType=Prs 2 subj  _ AlignBegin=76490|AlignEnd=76688|deprel_main_pred=subj|Gloss=she|head_MST=8

2 be  be  VERB  _ PartType=Cop  0 root  _ AlignBegin=76688|AlignEnd=76886|deprel_main_pred=comp:obj|Gloss=be|head_MST=5

3 city  city  NOUN  _ _ 4 compound  _ AlignBegin=76886|AlignEnd=77084|deprel_main_pred=compound|Gloss=city|head_MST=10

4 girl  girl  NOUN  _ _ 2 comp:pred _ AlignBegin=77084|AlignEnd=77282|deprel_main_pred=comp:pred|Gloss=girl|head_MST=8

{{< /conll >}}

<!-- tabs:end -->

  
  
  

The `compound` relation is also used in some relations between nouns and adjectives, such as *dry cleaner*, which are considered fixed expressions whose meaning cannot be directly understood from its constituent parts

>[!NOTE]
> Please note that other languages might use the `compound` relation in a more limited set of contexts, if at all. For a more general overview of this relation, please consult the [dedicated page](../../../General_Guideline/Syntactic_relations/compound/compound.md).

  

{{< conll >}}

1 you you PRON  _ Case=Nom|Person=2|PronType=Prs  2 subj  _ AlignBegin=119950|AlignEnd=120306|deprel_main_pred=subj|Gloss=NOM.2|head_MST=2

2 fit fit AUX _ Mood=Pot  0 root  _ AlignBegin=120306|AlignEnd=120661|deprel_main_pred=root|Gloss=ABIL|head_MST=0

3 carry carry VERB  _ _ 2 comp:aux  _ AlignBegin=120661|AlignEnd=121017|deprel_main_pred=comp:aux|Gloss=carry|head_MST=2

4 am  am  PRON  _ Case=Acc|Number=Sing|Person=3|PronType=Prs  3 comp:obj  _ AlignBegin=121017|AlignEnd=121373|deprel_main_pred=comp:obj|Gloss=ACC.SG.3|head_MST=3

5 go  go  VERB  _ _ 3 compound:svc  _ AlignBegin=121373|AlignEnd=121729|deprel_main_pred=compound:svc|Gloss=go|head_MST=3

6 dry dry ADJ _ _ 7 compound  _ AlignBegin=121729|AlignEnd=122084|deprel_main_pred=mod|Gloss=dry|head_MST=7

7 cleaner cleaner NOUN  _ _ 5 comp:obj  _ AlignBegin=122084|AlignEnd=122440|deprel_main_pred=comp:obj|Gloss=cleaner|head_MST=5

{{< /conll >}}

  
  
  

The subtype `compound:prt` is also used to connect the components of various phrasal verbs inherited from English.

{{< conll >}}

1 just  just  ADV _ _ 2 mod _ AlignBegin=226630|AlignEnd=226860|Gloss=just

2 after after ADP _ _ 7 mod:periph  _ AlignBegin=226860|AlignEnd=227130|Gloss=after

3 one one NUM _ NumType=Card  4 det:num _ AlignBegin=227130|AlignEnd=227280|Gloss=one

4 minute  minute  NOUN  _ _ 2 comp:obj  _ AlignBegin=227280|AlignEnd=227680|Gloss=minute

5 , , PUNCT _ _ 2 punct _ AlignBegin=227680|AlignEnd=227680|Gloss=PUNCT

6 you you PRON  _ Case=Nom|Person=2|PronType=Prs  7 subj  _ AlignBegin=227680|AlignEnd=227792|Gloss=NOM.2

7 bring bring VERB  _ _ 0 root  _ AlignBegin=227792|AlignEnd=227990|Gloss=bring

8 am  am  PRON  _ Case=Acc|Number=Sing|Person=3|PronType=Prs  7 comp:obj  _ AlignBegin=227990|AlignEnd=228120|Gloss=ACC.SG.3

9 down  down  ADP _ _ 7 compound:prt  _ AlignBegin=228120|AlignEnd=228290|Gloss=down

10  . . PUNCT _ _ 7 punct _ AlignBegin=228290|AlignEnd=228290|Gloss=PUNCT

{{< /conll >}}

  
  
