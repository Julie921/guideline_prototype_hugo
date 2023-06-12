# conj:dicto

This relation is used to indicate difluencies when a speaker corrects his speech and to analyse reformulations. The relation `conj:coord` is used to link two different objects, two referants (ex: *Mary and John* are two different referents). The relation `conj:dicto` on the other hand is used to link two denotations of the same referent (ex: *the desert in Kenya, the Kenya desert* is denoting the same referant).

The ability of `conj:dicto` to anlyse both disfluencies and reformulations is the reason why we don't use the the [`reparandum`](https://universaldependencies.org/u/dep/reparandum.html) relationship as used in UD. For the moment, it is only used in SUD for analysis of written texts.

>[!tip]
> pattern { GOV-[conj:dicto]->DEP }

<!-- tabs:start -->
#### **French 1**
{{< conll >}}
\# text_fr = puisque les les les les c~ les capitales les grandes villes ne me disaient rien du tout
\# text_en = since I didn't know anything at all about the the the the c ~ the capitals the big cities
1   puisque puisque SCONJ   _   _   0   root    _   Gloss=since
2   les le  DET _   Definite=Def|Number=Plur|PronType=Art   6   det _   Gloss=the
3   les le  DET _   Definite=Def|Number=Plur|PronType=Art   2   conj:dicto  _   Gloss=the
4   les le  DET _   Definite=Def|Number=Plur|PronType=Art   3   conj:dicto  _   Gloss=the
5   les le  DET _   Definite=Def|Number=Plur|PronType=Art   4   conj:dicto  _   Gloss=the
6   c~  c~  X   _   _   14  subj    _   _
7   les le  DET _   Definite=Def|Number=Plur|PronType=Art   8   det _   Gloss=the
8   capitales   capitale    NOUN    _   Gender=Fem|Number=Plur  6   conj:dicto  _   Gloss=capitals
9   les le  DET _   Definite=Def|Number=Plur|PronType=Art   11  det _   Gloss=the
10  grandes grand   ADJ _   Gender=Fem|Number=Plur  11  mod _   Gloss=big
11  villes  ville   NOUN    _   Gender=Fem|Number=Plur  8   conj:dicto  _   Gloss=cities
12  ne  ne  ADV _   Polarity=Neg    14  mod _   Gloss=not
13  me  lui PRON    _   _   14  comp:obl    _   Gloss=me
14  disaient    dire    VERB    _   Mood=Ind|Number=Plur|Person=3|Tense=Imp|VerbForm=Fin    1   comp:obj    _   Gloss=tell
15  rien    rien    PRON    _   _   14  comp:obj    _   Gloss=nothis
16-17   du  _   _   _   _   _   _   _   _
16  de  de  ADP _   _   15  mod _   Gloss=of
17  le  le  DET _   Definite=Def|Gender=Masc|Number=Sing|PronType=Art   18  det _   Gloss=it
18  tout    tout    ADV _   _   16  comp:obj    _   Gloss=all
{{< /conll >}}

#### **French 2**
{{< conll >}}
\# sent_id = ParisStories_2019_stagePrimaire_15
\# text_fr = j'ai j'ai vraiment adoré ce côté là .
\# text_en = I did I did really like that part
1   j'  il  PRON    _   Number=Sing|Person=1|PronType=Prs   2   subj    _   SpaceAfter=No|Gloss=I
2   ai  ai~ AUX _   Number=Sing|Person=1    0   root    _   Gloss=have
3   j'  il  PRON    _   Number=Sing|Person=1|PronType=Prs   4   subj    _   SpaceAfter=No|Gloss=I
4   ai  avoir   AUX _   Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin   2   conj:dicto  _   Gloss=have
5   vraiment    vraiment    ADV _   _   6   mod _   Gloss=really
6   adoré   adorer  VERB    _   Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part    4   comp:aux    _   Gloss=loved
7   ce  ce  DET _   _   8   det _   Gloss=that
8   côté    côté    NOUN    _   Gender=Masc|Number=Sing 6   comp:obj    _   Gloss=part
9   là  là  ADV _   _   8   mod _   Gloss=that
10  .   .   PUNCT   _   _   _   _   _   _
{{< /conll >}}

#### **Naija**
{{< conll >}}
\# sent_id = JOS_10_Mothers-Against-Mini-Skirts_DG__79
\# sound_url = http://www.tal.univ-paris3.fr/trameur/iTrameur-naija/mp3/JOS_10_Mothers-Against-Mini-Skirts_DG.mp3
\# speaker_id = Sp125
\# text = we used to { use eh || wear } mini skirt o //
\# text_en = We used to use uh... wear mini skirts.
\# text_ortho = We used to use eh, wear mini skirt o.
1   we  we  PRON    _   Case=Nom|Number=Plur|Person=1|PronType=Prs  2   subj    _   AlignBegin=144296|AlignEnd=144584|Gloss=NOM.PL.1|Lang=en
2   used    use VERB    _   Mood=Ind|Tense=Past|VerbForm=Fin    0   root    _   AlignBegin=144584|AlignEnd=144872|Gloss=use.IND.PST.FIN|Lang=en
3   to  to  ADP _   _   2   comp:obl@x  _   AlignBegin=144872|AlignEnd=145160|Gloss=to|Lang=en
4   {   {   PUNCT   _   _   5   punct   _   AlignBegin=145160|AlignEnd=145160|Gloss=PUNCT
5   use use VERB    _   _   3   comp:obj    _   AlignBegin=145160|AlignEnd=145448|Gloss=use|Lang=en
6   eh  eh  INTJ    _   _   5   discourse   _   AlignBegin=145448|AlignEnd=145736|Gloss=eh|Lang=en
7   ||  ||  PUNCT   _   _   8   punct   _   AlignBegin=145736|AlignEnd=145736|Gloss=PUNCT
8   wear    wear    VERB    _   _   5   conj:dicto  _   AlignBegin=145736|AlignEnd=146024|Gloss=wear|Lang=en
9   }   }   PUNCT   _   _   5   punct   _   AlignBegin=146024|AlignEnd=146024|Gloss=PUNCT
10  mini    mini    ADJ _   _   11  compound    _   AlignBegin=146024|AlignEnd=146312|Gloss=mini|Lang=en
11  skirt   skirt   NOUN    _   _   8   comp:obj    _   AlignBegin=146312|AlignEnd=146600|Gloss=skirt|Lang=en
12  o   o   PART    _   PartType=Disc   11  mod:emph    _   AlignBegin=146600|AlignEnd=146888|Gloss=EMPH|Lang=en
13  //  //  PUNCT   _   _   2   punct   _   AlignBegin=146888|AlignEnd=146888|Gloss=PUNCT
{{< /conll >}}
<!-- tabs:end -->
  

Note that `conj:dicto` (SUD) considers the first element as the head of the next one, while `reparandum` (UD) considers these constructions as reparations and considers the last element as head.

This is because UD relies more on the semantics - it is the last element that holds the meaning. SUD on the other hand relies on the syntactic aspect and considers that it is the first element that occupies the syntactic position.

This may result in some incoherencies. Note the following example. In this sentence we have two options of annotation. We can annotate the *é~* with an unknown POS (`X`). In that case `X` is the head of a `subj` relation which is undesirable (only `VERB` and `AUX` should be head of a `subj` relation). The other option would be to guess the POS and lemma of the unfinished word with the risk of guessing it wrong. In our case the token *é~* would be annotated with the lemma *être* and POS `AUX`. In this scenario, *é~* becomes part of the paradigm of the conjugated verb *être* which is also undesirable.

In SUD we decided to adopt the following analysis.
<!-- tabs:start -->
#### **French**
{{< conll >}}
\# text_fr = C' é~ c' était vraiment
\# text_en = It w~ it was really
1   C'  ce  PRON    _   Gender=Masc|Number=Sing|Person=3|PronType=Dem   2   subj    _   Gloss=it
2   é~  é~  X   _   _   0   root    _   _
3   c'  ce  PRON    _   Gender=Masc|Number=Sing|Person=3|PronType=Dem   4   subj    _   Gloss=it
4   était   être    AUX conj:reform Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin    2   conj:dicto  _   Gloss=was
5   vraiment    vraiment    ADV _   _   4   mod _   Gloss=really
{{< /conll >}}
<!-- tabs:end -->
  
For more examples on disfluencies, you can refer to [this page](../../Particular_construction/disfluency.md).




## bedja

TODO
### Overview

### Specific Pattern




## beja

TODO
### Overview

### Specific Pattern


