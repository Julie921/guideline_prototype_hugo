---
title: "Reflex"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# Reflex


## Universal

*Definition from de [UD website](https://universaldependencies.org/u/feat/Person.html)*
Boolean feature, typically of pronouns or determiners. It tells whether the word is reflexive, i.e. refers to the subject of its clause.

While many tagsets would have “reflexive” as one of the various pronoun types, this feature is intentionally separate from PronType. When used with pronouns and determiners, it should be combined with PronType=Prs, regardless whether they really distinguish the Person feature (in some languages they do, in others they do not).

Note that forms that are canonically reflexive sometimes have other functions in the language, too. The feature Reflex=Yes denotes the word type, not its actual function in context (which can be distinguished by dependency relation types). Hence the feature is not restricted to situations where the word is used truly reflexively.

For example, reflexive clitics in European languages often have a wide array of possible functions (middle, passive, inchoative, impersonal, or even as a lexical morpheme). Besides that, reflexives in some languages are also used for emphasis (while other languages have separate emphatic pronouns), and in some languages they signal reciprocity (while other languages have separate reciprocal pronouns). Using Reflex=Yes with all of them has the benefit that they can be easily identified (however, if it is possible for the annotators to distinguish contexts where a reflexive pronoun is used reciprocally or emphatically, it is possible to combine Reflex=Yes with PronType=Rcp or PronType=Emp, instead of PronType=Prs).

Note that while some languages also have reflexive verbs, these are in fact fused verbs with reflexive pronouns, as in Spanish despertarse or Russian проснуться (both meaning “to wake up”). Thus in these cases the fused token will be split to two syntactic words, one of them being a reflexive pronoun. In languages where the reflexive pronoun is not split, it may be more appropriate to mark the verb as the middle Voice than using Reflex=Yes with the verb.

### Values

[Yes](https://universaldependencies.org/u/feat/Reflex.html#Yes).



## french

TODO
### Overview

### Specific Pattern



