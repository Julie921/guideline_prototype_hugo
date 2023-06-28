# Filler words in Mandarin Chinese
In Mandarin Chinese, there are several filler words (also known as "filler sounds" or "hesitation sounds") that are used, much like "um", "uh", "like", "you know", etc. in English. Here are some of the most common ones:

1) 那个 (nèi ge / nà ge) - Similar to "uh", "um", or "like" in English.
2) 这个 (zhè ge) - Used similarly to 那个 (nèi ge / nà ge). It can also mean "this one" in other contexts.
3) 嗯 (ń / ň / ǹg) - Used to show agreement or acknowledgment, similar to "uh-huh" in English.
4) 就是 (jiù shì) - Similar to "it's just like", "you know", or "so" in English.
5) 对 (duì) - Means "correct", but it can also be used as a filler word similar to "right" in English.
6) 然后 (ránhòu) - Similar to "and then" or "so then" in English.

As in other languages, filler words in Mandarin should be used sparingly in formal speech or writing but can make informal speech sound more natural.

## How to annotate
The filler word is annotated as an interjection (INTJ) and with a discourse relation to the head of the phrase. If there is punctuation related to the filler word, the punctuation will be governed by the filler word.

## Structures

### - 那个
As there is no syntactic relation between 那 and 个, we annotate with a det@m relation.

{{< conll_interactive >}}
# sent_id = 761
# text = 那个 ⋯⋯ 这样 做 不 好 吧？
# pinyin = Nèige... zhèyàng zuò bù hǎo ba?
# text_en = Ummm, it's not good to do it this way?
# url = https://resources.allsetlearning.com/chinese/grammar/ASG8VJM8
1	那	那	DET	_	_	2	det@m	_	highlight=red
2	个	个	NOUN	INTJ	_	9	discourse	_	highlight=red
3	⋯	⋯	PUNCT	_	_	2	punct	_	_
4	⋯	⋯	PUNCT	_	_	2	punct	_	_
5	这	这	DET	_	_	6	det	_	_
6	样	样	NOUN	_	_	7	clf	_	_
7	做	做	VERB	_	_	9	subj	_	_
8	不	不	ADV	_	Polarity=Neg	9	mod	_	_
9	好	好	ADJ	_	_	0	root	_	_
10	吧	吧	PART	_	Mood=Inter	9	discourse	_	_
11	？	？	PUNCT	_	_	9	punct	_	_
{{< /conll_interactive >}}