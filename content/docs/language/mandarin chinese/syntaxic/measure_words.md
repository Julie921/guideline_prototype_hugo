# Measure words in Mandarin Chinese


"Measure words", commonly referred to as "classifiers" in linguistics, are utilized in conjunction with numbers to denote the quantity of a noun or, on occasion, an action. These terms, measure words, essentially classify or categorize the noun or action under consideration for counting.

## How to annotate
The head of the measure head will be the noun it qualify.   
The dependant will be the quantity and/or the determinant

## Structures

### - NUM + CLF + NOUN

{{< conll_interactive >}}
# sent_id = 216
# text = 我 能 吃 四 十 个 饺子。
# pinyin = Wǒ néng chī sìshí gè jiǎozi.
# text_en = I can eat 40 dumplings.
# url = https://resources.allsetlearning.com/chinese/grammar/ASG9PQ40
1	我	我	PRON	_	Person=1	2	subj	_	_
2	能	能	AUX	_	_	0	root	_	_
3	吃	吃	VERB	_	_	2	comp:aux	_	_
4	四	四	NUM	_	NumType=Card	6	mod	_	_
5	十	十	NUM	_	NumType=Card	4	flat	_	_
6	个	个	NOUN	_	_	7	clf	_	highlight=red
7	饺	饺	NOUN	_	_	3	comp:obj	_	highlight=#3eaa0c
8	子	子	NOUN	_	_	7	@m	_	highlight=#3eaa0c
9	。	。	PUNCT	_	_	2	punct	_	_
{{< /conll_interactive >}}

{{< conll_interactive >}}
# sent_id = 526
# text = 我 只 能 说 两 句 中文。
# text_en = I can only say two sentences in Chinese.
# pinyin = Wǒ zhǐ néng shuō liǎng jù Zhōngwén.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGN8C8R
1	我	我	PRON	_	Person=1	3	subj	_	_
2	只	只	ADV	_	_	3	mod	_	_
3	能	能	AUX	_	_	0	root	_	_
4	说	说	VERB	_	_	3	comp:aux	_	_
5	两	两	NUM	_	NumType=Card	6	mod	_	_
6	句	句	NOUN	_	_	7	clf	_	highlight=red
7	中	中	NOUN	_	_	4	comp:obj	_	highlight=#3eaa0c
8	文	文	NOUN	_	_	7	@m	_	highlight=#3eaa0c
9	。	。	PUNCT	_	_	3	punct	_	_
{{< /conll_interactive >}}

### - DET + CLF + NOUN
When a classifier is used without a finite number but with a determinant, it act like in english when we use an indefinite quantifier (some, many, few)


{{< conll_interactive >}}
# sent_id = 673
# text = 这些 菜多 好吃 啊！
# pinyin = Zhèxiē cài duō hǎochī a!
# text_en = These dishes are so delicious!
# url = https://resources.allsetlearning.com/chinese/grammar/ASGGH7RR
1	这	这	DET	_	_	2	det	_	highlight=#0C94AA
2	些	些	NOUN	_	_	3	clf	_	highlight=red
3	菜	菜	NOUN	_	_	5	subj	_	highlight=#3eaa0c
4	多	多	ADV	_	_	5	mod	_	_
5	好	好	ADJ	_	_	0	root	_	_
6	吃	吃	VERB	_	_	5	mod@m	_	_
7	啊	啊	PART	_	_	5	discourse	_	_
8	！	！	PUNCT	_	_	5	punct	_	_
{{< /conll_interactive >}}


{{< conll_interactive >}}
# sent_id = 717
# text = 这 种 事 最 麻烦 。
# pinyin = Zhè zhǒng shì zuì máfan.
# text_en = These kind of things are the most troublesome.
# url = https://resources.allsetlearning.com/chinese/grammar/ASG3544U
1	这	这	DET	_	_	2	det	_	highlight=#0C94AA
2	种	种	NOUN	_	_	3	clf	_	highlight=red
3	事	事	NOUN	_	_	5	subj	_	highlight=#3eaa0c
4	最	最	ADV	_	_	5	mod	_	_
5	麻	麻	ADJ	_	_	0	root	_	_
6	烦	烦	ADJ	_	_	5	@m	_	_
7	。	。	PUNCT	_	_	5	punct	_	_
{{< /conll_interactive >}}