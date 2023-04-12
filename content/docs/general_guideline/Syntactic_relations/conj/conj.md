# conj

In UD there are three relations

[`reparandum`](https://universaldependencies.org/u/dep/reparandum.html),

[`conj`](https://universaldependencies.org/u/dep/conj.html),

[`appos`](https://universaldependencies.org/u/dep/appos.html)

that SUD only uses for analysing written texts.

These three relations work as paradigmatic lists. That's why in SUD for oral speech, we decided to gather these three relations under the relation `conj` to underline the similarity between the three.

>[tip]
> pattern { e : GOV-[1=conj]->DEP}
> you can find more [here](http://universal.grew.fr/?custom=63ff56c2f1034)

We distinguish:

   * [`conj:dicto`](../conj_dicto) for disfluencies when the speaker corrects his speech (parallel to `reparandum` in written texts)

   * [`conj:coord`](../conj_coord) for elements connected by a coordinating conjunction (parallel to `conj` in written texts)

   * [`conj:appos`](../conj_appos) for appositional modifiers that serve to define better the previous noun (parallel to `appos` in written texts)

Note : for analysing oral speech we never use the `conj` relationship alone.


## Chained conjuncts

In UD, all conjuncts of a coordination are attached to the head of the first conjunct in a bouquet. In SUD, each conjunct is attached to the head of the previous one in a chain.


The first example below shows the annotation of a coordination in UD and the second one the corresponding annotation in SUD.

  
<!-- tabs:start -->
#### **English 1**
{{< conll >}}
1   John    John    PROPN   _   _   7   nsubj   _   _
2   ,   ,   PUNCT   _   _   3   punct   _   _
3   Mary    Mary    PROPN   _   _   1   conj    _   _
4   and and CCONJ   _   _   5   cc  _   _
5   Peter   Peter   PROPN   _   _   1   conj    _   _
6   will    will    AUX _   _   7   aux _   _
7   come    come    VERB    _   _   0   root    _   _
{{< /conll >}}


#### **English 2**
{{< conll >}}
1   John    John    PROPN   _   _   6   subj    _   _
2   ,   ,   PUNCT   _   _   3   punct   _   _
3   Mary    Mary    PROPN   _   _   1   conj    _   _
4   and and CCONJ   _   _   5   cc  _   _
5   Peter   Peter   PROPN   _   _   3   conj    _   _
6   will    will    AUX _   _   0   root    _   _
7   come    come    VERB    _   _   6   comp:aux    _   _
{{< /conll >}}
<!-- tabs:end -->