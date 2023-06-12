# mod

The `mod` relation is used for modifiers of verbs, nouns, adjectives, adverbs, auxiliaries, adpositions and conjunctions.


> The relation `mod` can have these features:
> * [@relcl](../../Deep/relcl.md)
> pattern { GOV -[mod@relcl]-> DEP}


> pattern { GOV-[mod]->DEP }
> % or with a clustering e.label 
> pattern { e : GOV-[1=mod]->DEP }
  
> English
{{< conll >}}
1   a   a   DET _   _   2   det _   _
2   country country NOUN    _   _   0   root    _   _
3   with    with    ADP _   _   2   mod _   _
4   so  so  ADV _   _   5   mod _   _
5   many    many    ADJ _   _   8   mod _   _
6   different   different   ADJ _   _   8   mod _   _
7   language    language    NOUN    _   _   8   compound    _   _
8   groups  group   NOUN    _   _   3   comp:obj    _   _
{{< /conll >}}

  
> English
{{< conll >}}
1   Even    even    ADV _   _   2   mod _   _
2   when    when    SCONJ   _   _   8   mod _   _
3   he  he  PRON    _   _   4   subj    _   _
4   robbed  rob VERB    _   _   2   comp:obj    _   _
5   Dostoevski  Dostoevski  PROPN   _   _   4   comp:obj    _   _
6   ,   ,   PUNCT   _   _   2   punct   _   _
7   he  he  PRON    _   _   8   subj    _   _
8   pitied  pity    VERB    _   _   0   root    _   _
9   him he  PRON    _   _   8   comp:obj    _   _
{{< /conll >}}

> French
{{< conll >}}
# text = Cerebral concussions have become so commun in this sport that one can consider them the routine.
1   Les le  DET _   Definite=Def|Gender=Fem|Number=Plur|PronType=Art    2   det _   Gloss=the
2   commotions  commotion   NOUN    _   Gender=Fem|Number=Plur  4   subj    _   Gloss=concussions
3   cérébrales  cérébral    ADJ _   Gender=Fem|Number=Plur  2   mod _   Gloss=cerebral
4   sont    être    AUX _   Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin   0   root    _   Gloss=have
5   devenu  devenir VERB    _   Gender=Masc|Number=Sing|Tense=Past|Typo=Yes|VerbForm=Part   4   comp:aux@tense  _ Gloss=become
6   si  si  ADV _   _   7   mod _   Gloss=so
7   courantes   courant ADJ _   Gender=Fem|Number=Plur  5   comp:pred   _   Gloss=common
8   dans    dans    ADP _   _   7   mod _   Gloss=in
9   ce  ce  DET _   Gender=Masc|Number=Sing|PronType=Dem    10  det _   Gloss=this
10  sport   sport   NOUN    _   Gender=Masc|Number=Sing 8   comp:obj    _   Gloss=sport
11  qu' que SCONJ   _   _   7   mod _   Gloss=that
12  on  on  PRON    _   Gender=Masc|Number=Sing|Person=3    14  subj    _   Gloss=one
13  les le  PRON    _   Number=Plur|Person=3|PronType=Prs   14  comp:obj    _   Gloss=them
14  considére   considérer  VERB    _   Mood=Ind|Number=Sing|Person=3|Tense=Pres|Typo=Yes|VerbForm=Fin  11  comp:obj    _   Gloss=considers
15  presque presque ADV _   _   14  mod _   Gloss=almost
16  comme   comme   ADP _   _   14  comp:obl@x  _   Gloss=like
17  la  le  DET _   Definite=Def|Gender=Fem|Number=Sing|PronType=Art    18  det _   Gloss=the
18  routine routine NOUN    _   Gender=Fem|Number=Sing  16  comp:obj    _   Gloss=routine
19  .   .   PUNCT   _   _   4   punct   _   .
{{< /conll >}}


## french

### Overview

 this is a fancy description. Does it work ??????






## bedja

TODO
### Overview

### Specific Pattern




## beja

TODO
### Overview

### Specific Pattern


