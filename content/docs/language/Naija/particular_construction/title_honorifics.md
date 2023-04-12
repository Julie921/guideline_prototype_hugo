
### Titles and honorifics

  

Honorifics such as *Mister* or *President* are connected to the names they precede with a simple `flat` relation.

<!-- tabs:start -->
#### **Example 1**
{{< conll >}}

1 Mister  Mister  NOUN  _ _ 0 conj:appos  _ AlignBegin=228030|AlignEnd=228400|Gloss=Mister

2 Sunday  Sunday  PROPN _ _ 1 flat  _ AlignBegin=228400|AlignEnd=228820|Gloss=Sunday

3 Ajayi Ajayi PROPN _ _ 2 flat  _ AlignBegin=228820|AlignEnd=229306|Gloss=Ajayi

{{< /conll >}}

  
#### **Example 2**
{{< conll >}}

1 Presido presido NOUN  _ _ 0 subj  _ AlignBegin=17490|AlignEnd=17830|Gloss=president

2 Joe Joe PROPN _ _ 1 flat  _ AlignBegin=17830|AlignEnd=18270|Gloss=Joe

3 Biden Biden PROPN _ _ 2 flat  _ AlignBegin=18270|AlignEnd=18540|Gloss=Biden

{{< /conll >}}
<!-- tabs:end -->
  
  

However, this is not the case when a title is connected to a determiner or otherwise modified in some way. In these cases, a `mod:appos` relation is used.

{{< conll >}}

1 di  di  DET _ Definite=Def|PronType=Art 2 det _ AlignBegin=69661|AlignEnd=69761|Gloss=DEF.ART

2 Presido presido NOUN  _ _ 0 subj  _ AlignBegin=17490|AlignEnd=17830|Gloss=president

3 for for ADP _ _ 2 mod _ AlignBegin=90227|AlignEnd=90390|Gloss=for

4 America America PROPN _ _ 3 comp:obj  _ AlignBegin=17830|AlignEnd=18270|Gloss=America

5 Joe Joe PROPN _ _ 2 mod:appos _ AlignBegin=17830|AlignEnd=18270|Gloss=Joe

6 Biden Biden PROPN _ _ 5 flat  _ AlignBegin=18270|AlignEnd=18540|Gloss=Biden

{{< /conll >}}

  
  

Official multi-word titles such as *Minister of Foreign Affairs* are treated as titles (see [here](../u/extpos/idioms_titles) for a detailed guide). The head of the title is given an `ExtPos` of `PROPN`.

{{< conll >}}

\# text_en = The Minister of Foreign Affairs, Geoffrey Onyeama Godfrey.

1 di  di  DET _ Definite=Def|PronType=Art 2 det _ AlignBegin=46977|AlignEnd=47085|Gloss=DEF.ART

2 Minister  minister  NOUN  _ _ 0 comp:obj  _ AlignBegin=47085|AlignEnd=47482|ExtPos=PROPN|Gloss=minister|Title=Yes

3 of  of  ADP _ _ 2 mod _ AlignBegin=47482|AlignEnd=47587|Gloss=of|InTitle=Yes

4 Foreign foreign ADJ _ _ 5 mod _ AlignBegin=47587|AlignEnd=47827|Gloss=foreign|InTitle=Yes

5 Affairs affair  NOUN  _ Number=Plur 3 comp:obj  _ AlignBegin=47827|AlignEnd=48301|Gloss=affair.PL|InTitle=Yes

6 Geoffrey  Geoffrey  PROPN _ _ 2 mod:appos _ AlignBegin=48331|AlignEnd=48727|Gloss=Geoffrey

7 Onyeama Onyeama PROPN _ _ 6 flat  _ AlignBegin=48727|AlignEnd=49343|Gloss=Onyeama

8 Godfrey Godfrey PROPN _ _ 7 flat  _ AlignBegin=49343|AlignEnd=49799|Gloss=Godfrey

{{< /conll >}}