---
title: "flat"
weight: 3
# bookFlatSection: false
bookToc: true
# bookHidden: false
bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# Flat

## Universal 
The `flat` relation plays a similar role to the `[compound](../compound/compound.md)` one, and its exact usage also varies on a language-by-language basis. However, it is most frequently used to connect the various elements of proper names to one another, including titles and honorifics.  

> pattern { GOV-[flat]->DEP }
  
> English
{{< conll >}}
# text = Emperor Joshua Norton, in full military regalia, circa 1880 or earlier


1   Emperor Emperor PROPN   NNP Number=Sing 0   root    _   Entity=(person-1

2   Joshua  Joshua  PROPN   NNP Number=Sing 1   flat    _   _

3   Norton  Norton  PROPN   NNP Number=Sing 1   flat    _   SpaceAfter=No

4   ,   ,   PUNCT   ,   _   5   punct   _   _

5   in  in  ADP IN  _   1   udep    _   _

6   full    full    ADJ JJ  Degree=Pos  8   mod _   Entity=(abstract-72

7   military    military    ADJ JJ  Degree=Pos  8   mod _   _

8   regalia regalia NOUN    NNS Number=Plur 5   comp:obj    _   Entity=abstract-72)|SpaceAfter=No

{{< /conll >}}

> English
{{< conll >}}

1   Once    once    SCONJ   IN  _   8   mod _   _

2   Cyclone Cyclone PROPN   NNP Number=Sing 4   subj    _   Entity=(event-3

3   Phailin Phailin PROPN   NNP Number=Sing 2   flat    _   Entity=event-3)

4   comes   come    VERB    VBZ Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   1   comp:obj    _   _

5   on  on  ADP IN  _   4   udep    _   _

6   shore   shore   NOUN    NN  Number=Sing 5   comp:obj    _   Entity=(place-39)

7   it  it  PRON    PRP Case=Nom|Gender=Neut|Number=Sing|Person=3|PronType=Prs  8   subj    _   Entity=(event-3)

8   will    will    AUX MD  VerbForm=Fin    0   root    _   _

9   immediately immediately ADV RB  _   8   mod _   _

10  begin   begin   VERB    VB  VerbForm=Inf    8   comp:aux    _   _

11  to  to  PART    TO  _   10  comp:pred   _   _

12  lose    lose    VERB    VB  VerbForm=Inf    11  comp:obj    _   _

13  strength    strength    NOUN    NN  Number=Sing 12  comp:obj    _   Entity=(abstract-9)|SpaceAfter=No

14  .   .   PUNCT   .   _   8   punct   _   _

{{< /conll >}}
  

The `flat` relation can also be used to link individual elements of numbers to one another.

  
> French
{{< conll >}}

\# text_en = In 1918, they say there were forty million deaths around the world.

1   il  il  PRON    _   _   3   subj@expl   _   Gloss=it

2   y   y   PRON    _   _   4   comp:obl    _   Gloss=there

3   a   avoir   AUX _   _   0   root    _   Gloss=have

4   eu  avoir   VERB    _   _   3   comp:aux    _   Gloss=had

5   en  en  ADP _   _   4   mod _   Gloss=in

6   mille   mille   NUM _   _   5   comp:obj    _   Gloss=thousand

7   neuf    neuf    NUM _   _   6   flat    _   Gloss=nine

8   cent    cent    NUM _   _   7   flat    _   Gloss=hundred

9   dix-huit    dix-huit    NUM _   _   8   flat    _   Gloss=eighteen

10  sur sur ADP _   _   3   mod _   Gloss=on

11  l'  le  DET _   _   12  det _   Gloss=the

12  ensemble    ensemble    NOUN    _   _   10  comp:obj    _   Gloss=whole

13  de  de  ADP _   _   12  mod _   Gloss=of

14  la  le  DET _   _   15  det _   Gloss=the

15  planète planète NOUN    _   _   13  comp:obj    _   Gloss=planet

16  on  on  PRON    _   _   17  subj    _   Gloss=one

17  dit dire    VERB    DISCOURSE   _   15  discourse   _   Gloss=say

18  quarante    quarante    NUM _   _   19  det _   Gloss=forty

19  millions    million NOUN    _   _   4   comp:obj    _   Gloss=millions

20  de  de  ADP _   _   19  mod _   Gloss=of

21  décès   décès   NOUN    _   _   20  comp:obj    _   Gloss=deaths

{{< /conll >}}

The syntactic relation ̀`flat` can have the deep `[name](../../Deep/name.md)` to annotated the composed proper name. 




## french

TODO
### Overview

### Specific Pattern




## haitien

TODO
### Overview

### Specific Pattern


