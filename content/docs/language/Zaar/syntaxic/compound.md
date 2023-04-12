# compound

  

## compound:prt

  

## compound:redup

  

## compound:svc

The `compound:svc` relation defines a serial verb construction that is normally connecting two (different) verbs. In Zaar, this relation can also connect two auxiliaries that are repeated.

  

### Example of a serial verb construction with auxiliaries

  

{{< conll >}}

# text_en =  After we collect wood, we come back and sit down.

1   mə́ á  AUX _   Aspect=Aor|Number=Plur|Person=1 7   parataxis@mod   _   AlignBegin=15869|AlignEnd=16080|Gloss=1PL.AOR

2   nat nat VERB    _   VerbForm=Fin    1   comp:aux    _   AlignBegin=16080|AlignEnd=16291|Gloss=tie

3   ŋamtsə́ ŋamtsə́ NOUN    _   _   2   comp:obj    _   AlignBegin=16291|AlignEnd=16397|Gloss=wood

4   ɗi  ɗi  PART    _   _   2   compound:prt    _   AlignBegin=16397|AlignEnd=16502|Gloss=CTP

5   <   <   PUNCT   _   _   1   punct   _   AlignBegin=16502|AlignEnd=16714|Gloss=PUNCT

6   tôː tòː PART    _   _   7   discourse   _   AlignBegin=16714|AlignEnd=16885|Gloss=well

7   mə́ á  AUX _   Aspect=Aor|Number=Plur|Person=1 0   root    _   AlignBegin=16885|AlignEnd=17056|Gloss=1PL.AOR

8   máni    máni    VERB    _   VerbForm=Fin    7   comp:aux    _   AlignBegin=17056|AlignEnd=17227|Gloss=come

9   mə́ á  AUX _   Aspect=Aor|Number=Plur|Person=1 7   compound:svc    _   AlignBegin=17227|AlignEnd=17398|Gloss=1PL.AOR

10  mán mán VERB    _   VerbForm=Fin    9   comp:aux    _   AlignBegin=17398|AlignEnd=17569|Gloss=come|SVC=Yes

11-12   tsə́tnni    _   _   _   _   _   _   _   _

11  tsə́tn  tsə́tn  VERB    _   VerbForm=Fin    10  compound:svc    _   AlignBegin=17569|AlignEnd=17655|Gloss=sit

12  ni  ni  PART    _   Aspect=Inch 11  compound:prt    _   AlignBegin=17655|AlignEnd=17740|Gloss=INCH

13  //  //  PUNCT   _   _   7   punct   _   AlignBegin=17740|AlignEnd=17910|Gloss=PUNCT

{{< /conll >}}