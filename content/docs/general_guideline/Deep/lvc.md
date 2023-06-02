---
title: "lvc"
weight: 3
bookFlatSection: true
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# Light Verb Construction - lvc

## Universal 

A light verb construction (LVC) is a type of verbal structure in which a verb is coupled with another element – typically a noun phrase – which provides the primary semantic value. Common examples of LVCs in English include *take a walk*, *give a kiss*, or *have a drink*. In SUD, LVCs are marked with the deep feature `@lvc`.

  
> French 
{{< conll >}}

\# text_fr = faire face à la situation

\# text_en = He faces the situation

1   Il  il  PRON    _   _   2   subj    _   Gloss=he

2   fait    faire   VERB    _   _   0   root    _   Gloss=makes

3   face    face    NOUN    _   _   2   comp:obj@lvc    _   Gloss=face

4   à   à   ADP _   _   3   comp:obl    _   Gloss=to

5   la  le  DET _   _   6   det _   Gloss=the

6   situation   situation   NOUN    _   _   4   comp:obj    _   Gloss=situation

{{< /conll >}}

  
  

The complements of these constructions are sometimes attached to the noun rather than the verb because:

* the noun can form a phrase with the complement : "the projectile has the tendency to get in the way" -> "this tendency to get in the way needs to be resolved"

* it's the noun that is the predicate and controls the valency. In the previous example, HAVE is binary predicate, not a ternary predicate.

  

This first criterion explains the differing interpretations of the following two sentences. "A date with his girlfriend" forms a perfectly coherent phrase which allows for reformulations such as "the date with his girlfriend, it was pleasant". However, "part in the discussion" is less semantically transparent and therefore less prone to such reformulations. Because of this, the verb "take" is treated as the head of the complement.

> English 

{{< conll >}}

1   He  he  PRON    _   _   2   subj    _   _

2   has have    VERB    _   _   0   root    _   _

3   a   a   DET _   _   4   det _   _

4   date    date    NOUN    _   _   2   comp:obj@lvc    _   _

5   with    with    ADJ _   _   4   mod _   _

6   his his DET _   _   7   det _   _

7   girlfriend  girlfriend  NOUN    _   _   5   comp:obj    _   _

{{< /conll >}}

> English 
{{< conll >}}

1   take    take    VERB    _   _   0   root    _   _

2   part    part    NOUN    _   _   1   comp:obj@lvc    _   _

3   in  in  ADP _   _   1   comp:obl    _   _

4   the the DET _   _   5   det _   _

5   discussion  discussion  NOUN    _   _   3   comp:obj    _   _

{{< /conll >}}
  
  

In cases of ambiguity, pronominalization can be a useful test for determining dependencies. Pronominalizing "He has a date with his girlfriend" as "the date, he has it with his girlfriend" would sound awkward to most native English speakers. However, pronominalizing "He took a walk with his wife" as "the walk, he took it with his wife" sounds much more natural. This explains the different syntactic interpretations of the following sentences.

  
> English
{{< conll >}}

1   He  he  PRON    _   _   2   subj    _   _

2   has have    VERB    _   _   0   root    _   _

3   a   a   DET _   _   4   det _   _

4   date    date    NOUN    _   _   2   comp:obj@lvc    _   _

5   with    with    ADJ –   –   4   mod _   _

6   his his DET _   _   7   det _   _

7   girlfriend  girlfriend  NOUN    _   _   5   comp:obj    _   _

{{< /conll >}}

> English
{{< conll >}}

1   He  he  PRON    _   _   2   subj    _   _

2   took    take    VERB    _   _   0   root    _   _

3   a   a   DET _   _   4   det _   _

4   walk    walk    NOUN    _   _   2   comp:obj@lvc    _   _

5   with    with    ADJ –   –   2   mod _   _

6   his his DET _   _   7   det _   _

7   wife    wife    NOUN    _   _   5   comp:obj    _   _

{{< /conll >}}

The `@lvc` feature is used for arguments of light verbs.

  
> English
{{< conll >}}

1   take    take    VERB    _   _   0   root    _   _

2   part    part    NOUN    _   _   1   comp:obj@lvc    _   _

3   in  in  ADP _   _   1   comp:obl    _   _

4   the the DET _   _   5   det _   _

5   discussion  discussion  NOUN    _   _   3   comp:obj    _   _

{{< /conll >}}

> French
{{< conll >}}

# text_en = He's afraid of the spider

1   il  il  PRON    _   Gender=Masc|Number=Sing|Person=3|PronType=Prs   2   subj    _   Gloss=he

2   a   avoir   VERB    _   Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin   0   root    _   Gloss=have

3   peur    peur    NOUN    _   Gender=Fem|Number=Sing  2   comp:obj@lvc    _   Gloss=fear

4   de  de  ADP _   _   3   comp:obl    _   Gloss=of

5   l'  le  DET _   Definite=Def|Number=Sing|Person=3|PronType=Art  6   det _   Gloss=the

6   araignée    araignée    PROPN   _   _   4   comp:obj    _   Gloss=spider

{{< /conll >}}

## French 


You can find more information about the annotation in french corpora [here](../../language/French/syntaxic/french_light_verb.md)## test 

