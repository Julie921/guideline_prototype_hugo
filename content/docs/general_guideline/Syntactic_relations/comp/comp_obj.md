# comp:obj
The `comp:obj` relation is used for direct object complements, including direct complements of an adposition or a subordinating conjunction.

> The relation `comp:obj` can have these features:
> * [@agent](../../Deep/agent.md)
> * [@lvc](../../Deep/lvc.md)
> pattern { GOV-[comp:obj]->DEP }

## Direct object complements

  
> English
{{< conll >}}
1   Norton  Norton  PROPN   _   _   2   subj    _   _
2   spent   spend   VERB    _   _   0   root    _   _
3   most    most    ADV _   _   2   comp:obj    _   _
4   of  of  ADP _   _   3   comp:obl    _   _
5   his his PRON    _   _   7   udep    _   _
6   early   early   ADJ _   _   7   mod _   _
7   life    life    NOUN    _   _   4   comp:obj    _   _
{{< /conll >}}

  
  

> French
{{< conll >}}
# text_fr = j'adore ce bar
# text_en = I love this bar
1   j'  I   PRON    _   Number=Sing|Person=1|PronType=Prs   2   subj    _   SpaceAfter=No
2   adore   love    VERB    _   Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin   0   root    _   _
3   ce  this    DET _   Gender=Masc|Number=Sing|PronType=Dem    4   det _   _
4   bar bar NOUN    _   Gender=Masc|Number=Sing 2   comp:obj    _   SpaceAfter=No
{{< /conll >}}


> Russian
{{< conll >}}
# text_ru = Я ставлю точку
# text_en = I put a point
1   Я   я   PRON    _   Animacy=Anim|Case=Nom|Number=Sing   2   subj    _   Gloss=I
2   ставлю  ставить VERB    _   Aspect=Imp|Mood=Ind|Number=Sing|Person=1|Tense=Pres|VerbForm=Fin|Voice=Act  0   root    _   Gloss=put
3   точку   точка   NOUN    _   Animacy=Inan|Case=Acc|Gender=Fem|Number=Sing    2   comp:obj    _   Gloss=point
{{< /conll >}}

  
Usually, in order to determine whether an object is direct or not, it suffices to know if it forms a construction with a preposition. If it doesn't, the object is direct. According to different languages, this criterion may be insufficient.

In the following examples we can see direct objects of the Spanish verb *ver*. With animate objects this verb takes the preposition *a*, however the object is still considered direct and therefore the relation stays `comp:obj`.

  
> Spanish
{{< conll >}}
# text_es = Veo su foto
# text_en = I see his photo
1   Veo ver VERB    _   _   0   root    _   Gloss=I see
2   su  su  DET _   _   3   det _   Gloss=his
3   foto    foto    NOUN    _   _   1   comp:obj    _   Gloss=photo
{{< /conll >}}

  
> Spanish
{{< conll >}}
# text_es = Veo a Clinton
# text_en = I see Clinton
1   Veo ver VERB    _   _   0   root    _   Gloss=I see
2   a   a   ADP _   _   1   comp:obj    _   _
3   Clinton Clinton PROPN   _   _   2   comp:obj    _   Gloss=Clinton
{{< /conll >}}

  
  

## Adposition arguments

> French
{{< conll >}}
# text_fr = On a décidé d'aller au CROUS de Censier
# text_en = We decided to go to the Censier CROUS
1   on  on  PRON    _   _   2   subj    _   Gloss=we
2   a   avoir   AUX _   _   0   root    _   Gloss=have
3   décidé  décider VERB    _   _   2   comp:aux    _   Gloss=decided
4   d'  de  ADP _   _   3   comp:obj@x  _   Gloss=to
5   aller   aller   VERB    _   _   4   comp:obj    _   Gloss=go
6   à   à   ADP _   _   5   comp:obl    _   Gloss=to
7   le  le  DET _   _   8   det _   Gloss=the
8   CROUS   CROUS   PROPN   _   _   6   comp:obj    _   Gloss=CROUS
9   de  de  ADP _   _   8   mod _   Gloss=of
10  Censier Censier PROPN   _   _   9   comp:obj    _   Gloss=Censier
{{< /conll >}}


> English
{{< conll >}}
1   Get get VERB    VB  VerbForm=Inf    0   root    _   _
2   feedback    feedback    NOUN    NN  Number=Sing 1   comp:obj    _   Entity=(abstract-120
3   from    from    ADP IN  _   2   udep    _   _
4   librarians  librarian   NOUN    NNS Number=Plur 3   comp:obj    _   Entity=(person-119)
5   on  on  ADP IN  _   2   udep    _   _
6   possible    possible    ADJ JJ  Degree=Pos  7   mod _   Entity=(abstract-105
7   subjects    subject NOUN    NNS Number=Plur 5   comp:obj    _   Entity=abstract-120)abstract-105)|SpaceAfter=No
8   ,   ,   PUNCT   ,   _   9   punct   _   _
9   based   base    VERB    VBN Tense=Past|VerbForm=Part    1   mod _   _
10  on  on  ADP IN  _   9   udep    _   _
11  already already ADV RB  _   12  mod _   _
12  known   know    VERB    VBN Tense=Past|VerbForm=Part    13  mod _   Entity=(abstract-121
13  gaps    gap NOUN    NNS Number=Plur 10  comp:obj    _   _
14  in  in  ADP IN  _   13  udep    _   _
15  their   their   PRON    PRP$    Number=Plur|Person=3|Poss=Yes|PronType=Prs  16  mod@poss    _   Entity=(abstract-122(person-119)
16  knowledge   knowledge   NOUN    NN  Number=Sing 14  comp:obj    _   Entity=abstract-122)
17  and and CCONJ   CC  _   18  cc  _   _
18  skills  skill   NOUN    NNS Number=Plur 16  conj    _   Entity=(abstract-123)abstract-121)|SpaceAfter=No
{{< /conll >}}

  
> Russian
{{< conll >}}
# sent_id = dev-s184
# text_ru = С запада к храму примыкала трапезная часть с колокольней
# text_en = From the west, the refectory part with the bell tower was adjoining the temple
1   С   с   ADP IN  _   5   comp:obl    _   Gloss=From
2   запада  запад   NOUN    NN  Animacy=Inan|Case=Gen|Gender=Masc|Number=Sing   1   comp:obj    _   Gloss=west
3   к   к   ADP IN  _   5   comp:obl    _   Gloss=to
4   храму   храм    NOUN    NN  Animacy=Inan|Case=Dat|Gender=Masc|Number=Sing   3   comp:obj    _   Gloss=temple
5   примыкала   примыкать   VERB    VBC Aspect=Imp|Gender=Fem|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Act    0   root    _   Gloss=was adjoining
6   трапезная   трапезный   ADJ JJL Case=Nom|Degree=Pos|Gender=Fem|Number=Sing  7   mod _   Gloss=refectory
7   часть   часть   NOUN    NN  Animacy=Inan|Case=Nom|Gender=Fem|Number=Sing    5   subj    _   Gloss=part
8   с   с   ADP IN  _   7   udep    _   Gloss=with
9   колокольней колокольня  NOUN    NN  Animacy=Inan|Case=Ins|Gender=Fem|Number=Sing    8   comp:obj    _   Gloss=bell tower
{{< /conll >}}

  
  

## Subordinating conjunction arguments
> English
{{< conll >}}
1   this    this    PRON    _   _   2   subj    _   _
2   means   mean    VERB    _   _   0   root    _   _
3   that    that    SCONJ   _   _   2   comp:obj    _   _
4   you you PRON    _   _   5   subj    _   _
5   have    have    VERB    _   _   3   comp:obj    _   _
6   to  to  PART    _   _   5   comp:obj    _   _
7   make    make    VERB    _   _   6   comp:obj    _   _
8   one one PRON    _   _   7   comp:obj    _   _
9   of  of  ADP _   _   8   udep    _   _
10  two two NUM _   _   11  det _   _
11  sacrifices  sacrifice   NOUN    _   _   9   comp:obj    _   _
{{< /conll >}}

  
> Spanish
{{< conll >}}
# text_es = Afirmó que sigue el criterio europeo y que trata de incentivar el mercado
# text_en = He stated that he follows the European criterion and tries to encourage the market
1   Afirmó  afirmar VERB    VERB    Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin   0   root    _   Gloss=affirmed
2   que que SCONJ   SCONJ   _   1   comp:obj    _   Gloss=that
3   sigue   seguir  VERB    VERB    Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   2   comp:obj    _   Gloss=follows
4   el  el  DET DET Definite=Def|Gender=Masc|Number=Sing|PronType=Art   5   det _   Gloss=the
5   criterio    criterio    NOUN    NOUN    Gender=Masc|Number=Sing 3   comp:obj    _   Gloss=criterion
6   europeo europeo ADJ ADJ Gender=Masc|Number=Sing 5   mod _   Gloss=European
7   y   y   CCONJ   CCONJ   _   8   cc  _   Gloss=and
8   que que SCONJ   SCONJ   _   2   conj    _   Gloss=that
9   trata   tratar  VERB    AUX Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   8   comp:obj    _   Gloss=try
10  de  de  ADP ADP AdpType=Prep    9   comp:obl@x  _   Gloss=of
11  incentivar  incentivar  VERB    VERB    VerbForm=Inf    10  comp:obj    _   Gloss=to incentivize
12  el  el  DET DET Definite=Def|Gender=Masc|Number=Sing|PronType=Art   13  det _   Gloss=the
13  mercado mercado NOUN    NOUN    Gender=Masc|Number=Sing 11  comp:obj    _   Gloss=market
{{< /conll >}}

  
> French
{{< conll >}}
# text_fr = il faut que tu deviennes script girl.
# text_en = You need to become a script girl.
1   il  il  PRON    _   _   2   subj    _   Gloss=it is
2   faut    falloir VERB    _   _   0   parataxis:parenth   _   Gloss=necessary
3   que que SCONJ   _   _   2   comp:obj    _   Gloss=that
4   tu  tu  PRON    _   _   5   subj    _   Gloss=you
5   deviennes   devenir VERB    _   _   3   comp:obj    _   Gloss=become
6   script  script  NOUN    _   _   7   compound    _   Gloss=script
7   girl    girl    NOUN    _   _   5   comp:pred   _   Gloss=girl
{{< /conll >}}

  

## Complement of an adverb of comparison

Constructions such as: *plus... que* (French), *more... than* (English), *più... di* (Italian), *bardziej... niż* (Polish), *более... чем* (Russian).

  
> English
{{< conll >}}
# text_en = techniques far more assertive than his predecessors
1   techniques  technique   NOUN    NNS Number=Plur 0   root    _   _
2   far far ADV RB  Degree=Pos  3   mod _   _
3   more    more    ADV RBR _   4   mod _   _
4   assertive   assertive   ADJ JJ  Degree=Pos  1   mod _   _
5   than    than    ADP IN  _   3   comp:obj    _   _
6   his his PRON    PRP$    Gender=Masc|Number=Sing|Person=3|Poss=Yes|PronType=Prs  7   mod@poss    _   _
7   predecessors    predecessor NOUN    NNS Number=Plur 5   comp:obj    _   _
{{< /conll >}}

> Russian
{{< conll >}}
# text = электроны имеют отклик намного более быстрый, чем атомы
1   электроны   электрон    NOUN    _   Animacy=Inan|Case=Nom|Gender=Masc|Number=Plur   2   subj    _   _
2   имеют   иметь   VERB    _   Aspect=Imp|Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin|Voice=Act  0   root    _   _
3   отклик  отклик  NOUN    _   Animacy=Inan|Case=Acc|Gender=Masc|Number=Sing   2   comp:obj    _   _
4   намного намного ADV _   Degree=Pos  5   mod _   _
5   более   более   ADV _   Degree=Cmp  6   mod _   _
6   быстрый быстрый ADJ _   Animacy=Inan|Case=Acc|Degree=Pos|Gender=Masc|Number=Sing    3   mod _   SpaceAfter=No
7   ,   ,   PUNCT   _   _   8   punct   _   _
8   чем чем SCONJ   _   _   5   comp:obj    _   _
9   атомы   атом    NOUN    _   Animacy=Inan|Case=Nom|Gender=Masc|Number=Plur   8   comp:obj    _   _
{{< /conll >}}

  
  
## Complement in consecutive constructions

Constructions such as: *tellement... que* (French), *so... that* (English), *così... che* (Italian), *tak... że* (Polish), *настолько... что* (Russian).

  
> French
{{< conll >}}
1   tellement   tellement   ADV _   _   2   mod _   _
2   vaste   vaste   ADJ _   _   0   root    _   _
3   qu' que SCONJ   _   _   1   comp:obj    _   _
4   on  on  PRON    _   _   7   subj    _   _
5   s'  se  PRON    _   _   7   comp    _   _
6   y   y   PRON    _   _   7   mod _   _
7   perd    perd    VERB    _   _   3   comp:obj    _   _
{{< /conll >}}

  
> Russian
{{< conll >}}
# sent_id = 2007Tele.xml_38
# text_ru = Изображение настолько хорошее, что все забыли о тестировании
# text_en = The image was so good that everyone forgot about testing
1   Изображение изображение NOUN    _   Animacy=Inan|Case=Nom|Gender=Neut|Number=Sing   3   subj    _   Gloss=image
2   настолько   настолько   ADV _   Degree=Pos  3   mod _   Gloss=so
3   хорошее хороший ADJ _   Case=Nom|Degree=Pos|Gender=Neut|Number=Sing 0   root    _   Gloss=good
4   ,   ,   PUNCT   _   _   5   punct   _   _
5   что что SCONJ   _   _   2   comp:obj    _   Gloss=that
6   все все PRON    _   Animacy=Anim|Case=Nom|Number=Plur   7   subj    _   Gloss=everyone
7   забыли  забыть  VERB    _   Aspect=Perf|Mood=Ind|Number=Plur|Tense=Past|VerbForm=Fin|Voice=Act  5   comp:obj    _   Gloss=forgot
8   о   о   ADP _   _   7   comp:obl    _   Gloss=about
9   тестировании    тестирование    NOUN    _   Animacy=Inan|Case=Loc|Gender=Neut|Number=Sing   8   comp:obj    _   Gloss=testing
{{< /conll >}}


## Deep subjects of impersonal constructions
 
 > French
{{< conll >}}
# text_en = There exist by the way many different types of cleats.
1   Il  il  PRON    _   Gender=Masc|Number=Sing|Person=3|PronType=Prs   2   subj@expl   _   Gloss=it
2   existe  exister VERB    _   Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   0   root    _   Gloss=exists
3   d'  de  ADP _   _   2   mod _   Gloss=of
4   ailleurs    ailleurs    ADV _   _   3   comp:obj    _   Gloss=elsewhere
5   beaucoup    beaucoup    ADV _   _   2   comp:obj@agent  _   Gloss=many
6   de  de  ADP _   _   5   comp:obl    _   Gloss=of
7   types   type    NOUN    _   Gender=Masc|Number=Plur 6   comp:obj    _   Gloss=types
8   de  de  ADP _   _   7   udep    _   Gloss=of
9   crampons    crampon NOUN    _   Gender=Masc|Number=Plur 8   comp:obj    _   Gloss=cleats
10  différents  différent   ADJ _   Gender=Masc|Number=Plur 9   mod _   Gloss=different
{{< /conll >}}

  
> Russian
{{< conll >}}
# sent_id = uppsalaGrekova_3.xml_179
# text_ru = Прошло много времени, пока я к ней приспособилась
# text_en = It took a lot of time until I got used to her
1   Прошло  пройти  VERB    _   Aspect=Perf|Gender=Neut|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Act  0   root    _   Gloss=passed
2   много   много   ADV _   Degree=Pos  1   comp:obj@agent  _   Gloss=a lot of
3   времени время   NOUN    _   Animacy=Inan|Case=Gen|Gender=Neut|Number=Sing   2   comp:obl    _   Gloss=time
4   ,   ,   PUNCT   _   _   5   punct   _   _
5   пока    пока    SCONJ   _   _   1   mod _   Gloss=until
6   я   я   PRON    _   Case=Nom|Number=Sing|Person=1   9   subj    _   Gloss=I
7   к   к   ADP _   _   9   comp:obl    _   Gloss=to
8   ней она PRON    _   Case=Dat|Gender=Fem|Number=Sing|Person=3    7   comp:obj    _   Gloss=her
9   приспособилась  приспособиться  VERB    _   Aspect=Perf|Gender=Fem|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Mid   5   comp:obj    _   Gloss=got used
{{< /conll >}}


## Direct Speech

Direct discourse is attached its governor by the relation `comp:obj` with the features `Reported = "Yes"` (link). It used to be annotate with the depency relation `parataxis:obj`. It has now been deleted.

  
> French
{{< conll >}}
# text_fr = Ce qui est horrible c' est de se dire je n' en sortirai jamais
# text_en = What is horrible is to think I will never get out
1   Ce  ce  PRON    _   _   6   dislocated  _   Gloss=this
2   qui qui PRON    _   _   3   subj    _   Gloss=that
3   est être    AUX _   Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   1   mod@relcl   _   Gloss=is
4   horrible    horrible    ADJ _   Gender=Masc|Number=Sing 3   comp:pred   _   Gloss=horrible
5   c'  ce  PRON    _   Gender=Masc|Number=Sing|Person=3|PronType=Dem   6   subj    _   Gloss=that
6   est être    AUX _   Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   0   root    _   Gloss=is
7   de  de  ADP _   _   6   comp:pred   _   Gloss=to
8   se  se  PRON    _   Person=3|PronType=Prs   9   comp    _   InIdiom=Yes|Gloss=yourself
9   dire    dire    VERB    _   VerbForm=Inf    7   comp:obj    _   ExtPos=VERB|PhraseType=Idiom|Gloss=say
10  je  il  PRON    _   Number=Sing|Person=1|PronType=Prs   13  subj    _   Gloss=I
11  n'  ne  ADV _   Polarity=Neg    13  mod _   Gloss=not
12  en  en  PRON    _   Person=3|PronType=Prs   13  comp:obj    _   Gloss=of
13  sortirai    sortir  VERB    _   Number=Sing|Person=1    9   comp:obj    _   Gloss=get_out|Reported=Yes
14  jamais  jamais  ADV _   _   13  mod _   Gloss=never
{{< /conll >}}

> Naija
{{< conll >}}
# sent_id = ABJ_GWA_02_Market-Food-Church_DG__58
# sound_url = http://www.tal.univ-paris3.fr/trameur/iTrameur-naija/mp3/ABJ_GWA_02_Market-Food-Church_DG.mp3
# speaker_id = Sp275
# text = eh e say [ you go parboil di banga //] //
# text_en = She said you'll parboil the banga.
# text_ortho = Eh e say you go parboil di banga.
1   eh  eh  INTJ    _   _   3   discourse   _   AlignBegin=84260|AlignEnd=84598|Gloss=eh
2   e   im  PRON    _   Case=Nom|Number=Sing|Person=3|PronType=Prs  3   subj    _   AlignBegin=84598|AlignEnd=84935|Gloss=NOM.SG.3
3   say say VERB    _   _   0   root    _   AlignBegin=84935|AlignEnd=85272|Gloss=say
4   [   [   PUNCT   _   _   6   punct   _   AlignBegin=85272|AlignEnd=85272|Gloss=PUNCT
5   you you PRON    _   Case=Nom|Person=2|PronType=Prs  6   subj    _   AlignBegin=85272|AlignEnd=85610|Gloss=NOM.2
6   go  go  AUX _   Aspect=Prosp    3   comp:obj    _   AlignBegin=85610|AlignEnd=85948|Gloss=PROSP|Reported=Yes
7   parboil parboil VERB    _   _   6   comp:aux    _   AlignBegin=85948|AlignEnd=86285|Gloss=parboil
8   di  di  DET _   Definite=Def|PronType=Art   9   det _   AlignBegin=86285|AlignEnd=86622|Gloss=DEF.ART
9   banga   banga   NOUN    _   _   7   comp:obj    _   AlignBegin=86622|AlignEnd=86960|Gloss=palm_kernel
10  //] //] PUNCT   _   _   6   punct   _   AlignBegin=86960|AlignEnd=86960|Gloss=PUNCT
11  //  //  PUNCT   _   _   3   punct   _   AlignBegin=86960|AlignEnd=86960|Gloss=PUNCT
{{< /conll >}}

