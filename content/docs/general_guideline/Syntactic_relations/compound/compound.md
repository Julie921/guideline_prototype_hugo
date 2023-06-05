# Compound

SUD shares with with UD its `compound` relation, though the exact usage of this relationship is determined on a language-by-language basis. SUD annotations for some languages, such as French, do not use the `compound` relation at all.

>[!tip]
> pattern { GOV-[compound]->DEP } 

Naija in particular makes heavy use of this relation, which is used to link nouns to virtually any other nouns which play a modifying role. However, it is also used to annotate phrasal verbs as well as a more limited subset of relations between nouns and adjectives, such as *dry cleaner*, which are considered fixed expressions whose meaning cannot be directly understood from its constituent parts. For more information about use of this relation in Naija, please consult the language's [dedicated page](../../../language/Naija/syntaxic/compound_phrasal_verbs.md).

  

In many cases, the existence of a `compound` relation can be determined with a series of linguistic tests. For example, it might be impossible to insert an adjective between two elements of a compound. In English, compounds are phonologically distinct, pronounced with an intonation similar to that of a single word. Consider the difference in pronunciation between *real estate*, a bona fide compound, and *real property*, an adjective and a noun connected with a simple `mod` relation.

  


