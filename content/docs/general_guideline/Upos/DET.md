---
title: "DET"
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

#  Determinant  

##  Universal  

*Definition from de [UD website](https://universaldependencies.org/u/pos/DET.html)*

Determiners are words that modify nouns or noun phrases and express the reference of the noun phrase in context. That is, a determiner may indicate whether the noun is referring to a definite or indefinite element of a class, to a closer or more distant element, to an element belonging to a specified person or thing, to a particular number or quantity, etc.

Determiners under this definition include both articles and pro-adjectives (pronominal adjectives), which is a slightly broader sense than what is usually regarded as determiners in English. In particular, there is no general requirement that a nominal can be modified by at most one determiner, although some languages may show a strong tendency towards such a constraint. (For example, an English nominal usually allows only one DET modifier, but there are occasional cases of addeterminers, which appear outside the usual determiner, such as [en] all in all the children survived. In such cases, both all and the are given the POS DET.)

Note that the DET tag includes (pronominal) quantifiers (words like many, few, several), which are included among determiners in some languages but may belong to numerals in others. However, cardinal numerals in the narrow sense (one, five, hundred) are not tagged DET even though some authors would include them in quantifiers. Cardinal numbers have their own tag NUM.

Also note that the notion of determiners is unknown in traditional grammar of some languages (e.g. Czech); words equivalent to English determiners may be traditionally classified as pronouns and/or numerals in these languages. In order to annotate the same thing the same way across languages, the words satisfying our definition of determiners should be tagged DET in these languages as well.

It is not always crystal clear where pronouns end and determiners start. Unlike in UD v1 it is no longer required that they are told apart solely on the base of the context. The words can be pre-classified in the dictionary as either PRON or DET, based on their typical syntactic distribution (and morphology, when applicable). Language-specific documentation should list all determiners (it is a closed class) and point out ambiguities, if any.

See also general principles on pronominal words for more tips on how to define determiners. In particular:

- Articles (the, a, an) are always tagged DET; their PronType is Art.
- Pronominal numerals (quantifiers) are tagged DET; besides PronType, they also use the NumType feature.
- Words that behave similar to adjectives are DET. Similar behavior means:
    - They are more likely to be used attributively (modifying a noun phrase) than substantively (replacing a noun phrase). They may occur alone, though. If they do, it is either because of ellipsis, or because the hypothetical modified noun is something unspecified and general, as in All [visitors] must pay.
    - Their inflection (if applicable) is similar to that of adjectives, and distinct from nouns. They agree with the nouns they modify. Especially the ability to inflect for gender is typical for adjectives and determiners. (Gender of nouns is determined lexically and determiners may be required by the grammar to agree with their nouns in gender; therefore they need to inflect for gender.)
- Possessives vary across languages. In some languages the above tests put them in the DET category. In others, they are more like a normal personal pronoun in a specific case (often the genitive), or a personal pronoun with an adposition; they are tagged PRON.

Examples
- articles (a closed class indicating definiteness, specificity or givenness): a, an, the
possessive determiners (which modify a nominal) (note that some languages use PRON for similar words): [cs] můj, tvůj, jeho, její, náš, váš, jejich
- demonstrative determiners: this as in I saw this car yesterday.
- interrogative determiners: which as in “Which car do you like?”
- relative determiners: which as in “I wonder which car you like.”
- quantity determiners (quantifiers): indefinite any, universal: all, and negative no as in “We have no cars available.”


## french

TODO
### Overview

### Specific Pattern


