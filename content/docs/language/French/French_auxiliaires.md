# French Auxiliaires

In French, only four verbs are considered auxiliaries: **être**, **avoir**, **faire** (also ***refaire***) and **se voir**.

>[!tip] 
> pattern { N [upos=AUX] } % and clustering N.lemma for example

The `comp:aux` relation can be used with one of the three sub-relations `@tense`, `@pass` or `@caus`, depending on whether the auxiliary is expressing a tense, a passive or a causative construction. In French, the relation `comp:aux@tense` is used with both verbs **être** and **avoir** and is the most common sub-relation. The relation `comp:aux@pass` is only used with the verb **être** and **se voir**, while `comp:aux@caus` is only used with the verb **faire**.

<!-- tabs:start -->
#### **auxilary expressing a tense**
{{< conll >}}

\# text_en = She has disappeared.

1 elle  il  PRON  _ Gender=Fem|Number=Sing|Person=3|PronType=Prs  2 subj  _ Gloss=she

2 a avoir AUX _ Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin 0 root  _ Gloss=has

3 disparu disparaître VERB  _ Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part  2 comp:aux@tense  _ Gloss=disappeared

{{< /conll >}}

>[!tip] 
> pattern { GOV-[comp:aux@tense]->DEP }  

#### **passive construction**

{{< conll >}}

\# text_en = The castle is then sold.

1 Le  le  DET _ Definite=Def|Gender=Masc|Number=Sing|PronType=Art 2 det _ Gloss=the

2 château château NOUN  _ Gender=Masc|Number=Sing 3 subj@pass _ Gloss=castle

3 est être  AUX _ Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin 0 root  _ Gloss=is

4 ensuite ensuite ADV _ _ 3 mod _ Gloss=next

5 vendu vendre  VERB  _ Gender=Masc|Number=Sing|Tense=Past|VerbForm=Part  3 comp:aux@pass _ Gloss=sold

{{< /conll >}}

>[!tip] 
> pattern { GOV-[comp:aux@pass]->DEP }   

#### **causative construction**

{{< conll >}}

\# text_en = He makes it fall.

1 il  il  PRON  _ Gender=Masc|Number=Sing|Person=3|PronType=Prs 3 subj@caus _ Gloss=he

2 le  le  PRON  _ Gender=Masc|Number=Sing|Person=3|PronType=Prs 3 comp:obj@agent  _ Gloss=it

3 fait  faire AUX _ Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin 0 root  _ Gloss=makes

4 tomber  tomber  VERB  _ VerbForm=Inf  3 comp:aux@caus _ Gloss=fall

{{< /conll >}}

>[!tip] 
> pattern { GOV-[comp:aux@caus]->DEP }  
<!-- tabs:end -->


> [!NOTE]
> You can find a discussion about the french auxiliaires [here](https://github.com/surfacesyntacticud/guidelines/issues/13)

## AUX or VERB ?

It is sometimes not trivial to chose between the part of speech `AUX` and `VERB` for **être**. We propose this distinction : 
- when **être** has a predicative complement, it is always considered as a copula and it has the POS `AUX` 
- when **être** has an existensial meaning (*je pense donc je suis* -***I think therefore I am***) or has a locative argument or another argument, which is not a predicative argument (*je suis pour la dépénalisation du cannabis* -***I am for the decriminalization of cannabis***), it has the POS `VERB`.