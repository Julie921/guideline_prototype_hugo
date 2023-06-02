---
title: "emb"
weight: 3
bookFlatSection: true
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---
# Embedded coordination

The conjunct of a coordination can itself be a coordination. Theoretically, this embedding can be nested indefinitely. In natural corpora, however, there is typically only one level of iteration.

The `[conj](../Syntactic_relations/conj/conj_coord.md)` label does not make a distinction between embedded relations and surface relations because they form a single chain. However, these relations can be distinguished with the use of the extension `@emb` for embedded coordinations, as the following example shows.

  
> English
{{< conll >}}

1   John    John    PROPN   _   _   9   subj    _   _

2   ,   ,   PUNCT   _   _   3   punct   _   _

3   Mary    Mary    PROPN   _   _   1   conj    _   _

4   or  or  CCONJ   _   _   6   cc  _   _

5   her her DET _   _   6   det _   _

6   brother brother NOUN    _   _   3   conj@emb    _   _

7   and and CCONJ   _   _   8   cc  _   _

8   Peter   Peter   PROPN   _   _   6   conj    _   _

9   will    will    AUX _   _   0   root    _   _

10  come    come    VERB    _   _   9   comp:aux    _   _

{{< /conll >}}
## test 



## breton 



## testeone 



## testetwo 



## testthree 



## testfour 



## testfive 



## testsix 



## breton

 TODO 


## test

 TODO 


## maintenant

 TODO 


## la

 TODO 


## julie

TODO 



## ok

TODO 



## gbaya

TODO 

