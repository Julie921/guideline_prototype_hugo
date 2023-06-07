# Cleft constructions

  

As shown in the page about the [`comp:cleft`](../../../general_guideline/Syntactic_relations/comp/comp_cleft.md) relation,  the cleft constructions are analysed with a `comp:cleft` relation going from the head of the main sentence to the head of the complement.

  

* With **qui** and **que** direct object, the cleft clause is analysed as a relative clause. in particular, **qui** and **que** are analysed as relative pronouns (PRON).

<!-- tabs:start -->
#### **Example**
{{< conll >}}

\# text_en = It is the team of Avengers which is reconstituted under the aegis of SHIELD

\# text = C'est l'équipe des Vengeurs qui est reconstituée sous l'égide du SHIELD

1 C'  ce  PRON  _ _ 2 subj@expl _ Gloss=It

2 est être  AUX _ _ 0 root  _ Gloss=is

3 l'  le  DET _ _ 4 det _ Gloss=the

4 équipe  équipe  NOUN  _ _ 2 comp:pred _ Gloss=team

5 de  de  ADP _ _ 4 udep  _ Gloss=of

6 les le  DET _ _ 7 det _ Gloss=the

7 Vengeurs  vengeur NOUN  _ _ 5 comp:obj  _ Gloss=Avengers

8 qui qui PRON  _ _ 9 subj  _ Gloss=which

9 est être  AUX _ _ 2 comp:cleft  _ Gloss=is

10  reconstituée  reconstituer  VERB  _ _ 9 comp:aux@tense  _ Gloss=reconstituted

11  sous  sous  ADP _ _ 9 mod _ Gloss=under

12  l'  le  DET _ _ 13  det _ Gloss=the

13  égide égide NOUN  _ _ 11  comp:obj  _ Gloss=aegis

14  de  de  ADP _ _ 13  udep  _ Gloss=of

15  le  le  DET _ _ 16  det _ Gloss=the

16  SHIELD  SHIELD  PROPN _ _ 14  comp:obj  _ Gloss=shield

{{< /conll >}}
<!-- tabs:end -->
  
  

In the other cases, the cleft clause is analysed as a complement clause, with **que** as a SCONJ.
<!-- tabs:start -->
#### **Example**
  {{< conll >}}

  # text_en = Most of the furniture is actually associated with this style.

  # text = C'est d'ailleurs à ce style que se rattache la majorité du mobilier.

  1 C'  ce  PRON  _ _ 2 subj@expl _ Gloss=it

  2 est être  AUX _ _ 0 root  _ Gloss=is

  3 d'  de  ADP _ _ 2 mod _ Gloss=of

  4 ailleurs  ailleurs  ADV _ _ 3 comp:obj  _ InIdiom=Yes|Gloss=actually

  5 à à ADP _ _ 2 comp:pred _ Gloss=to

  6 ce  ce  DET _ _ 7 det _ Gloss=this

  7 style style NOUN  _ _ 5 comp:obj  _ Gloss=style

  8 que que SCONJ _ _ 2 comp:cleft  _ Gloss=that

  9 se  se  PRON  _ _ 10  comp@pass _ Gloss=itself

  10  rattache  rattacher VERB  _ _ 8 comp:obj  _ Gloss=associated

  11  la  le  DET _ _ 12  det _ Gloss=the

  12  majorité  majorité  NOUN  _ G_  10  subj@pass _ Gloss=majority

  13-14 du  _ _ _ _ _ _ _ _

  13  de  de  ADP _ _ 12  udep  _ Gloss=of

  14  le  le  DET _ _ 15  det _ Gloss=the

  15  mobilier  mobilier  NOUN  _ _ 13  comp:obj  _ Gloss=furniture

  16  . . PUNCT _ _ 2 punct _ _

  {{< /conll >}}
<!-- tabs:end -->