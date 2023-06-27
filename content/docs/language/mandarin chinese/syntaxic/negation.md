# Negation in Chinese

There are several ways to express negation in Mandarin Chinese depending on the context. Two ways are syntactic while the other are morphological.


## Syntactical negation

### 1) 不 (bù)
This is the most common way to express general negation. It's typically used before a verb or an adjective. For example, "我们 不 喝 酒。" (Wǒmen bù hējiǔ) means "We don't drink alcohol.".

Negation of a verb :

{{< conll_interactive >}}
# text = 我们 不 喝 酒。
# pinyin = Wǒmen bù hējiǔ.
# text_en = We don't drink alcohol.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGIPYFV
1	我	我	PRON	_	Number=Plur|Person=1	4	subj	_	_
2	们	们	PART	_	Number=Plur|Person=1	1	@m	_	_
3	不	不	ADV	_	Polarity=Neg	4	mod	_	highlight=red
4	喝	喝	VERB	_	_	0	root	_	_
5	酒	酒	NOUN	_	_	4	comp:obj	_	_
6	。	。	PUNCT	_	_	4	punct	_	_
{{< /conll_interactive >}}

Negation of an adjective :
 
{{< conll_interactive >}}
# sent_id = 17
# text = 这 个 不 贵。
# pinyin = Zhège bù guì.
# text_en = This is not expensive.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGIPYFV
1	这	这	DET	_	_	2	det	_	_
2	个	个	NOUN	_	_	4	subj	_	_
3	不	不	ADV	_	Polarity=Neg	4	mod	_	highlight=red
4	贵	贵	ADJ	_	_	0	root	_	_
5	。	。	PUNCT	_	_	4	punct	_	_
{{< /conll_interactive >}}


Negation of the copula 是 :

{{< conll_interactive >}}
# text = 他们 不 是 坏 孩子。
# pinyin = Tāmen bù shì  huài háizi.
# text_en = They are not bad kids.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGIPYFV
1	他	他	PRON	_	Number=Plur|Person=3	4	subj	_	_
2	们	们	PART	_	Number=Plur|Person=3	1	@m	_	_
3	不	不	ADV	_	Polarity=Neg	4	mod	_	highlight=red
4	是	是	VERB	_	_	0	root	_	_
5	坏	坏	ADJ	_	_	6	mod	_	_
6	孩	孩	NOUN	_	_	4	comp:pred	_	_
7	子	子	NOUN	_	_	6	@m	_	_
8	。	。	PUNCT	_	_	4	punct	_	_
{{< /conll_interactive >}}

Negation of an auxiliary :

{{< conll_interactive >}}
# sent_id = 969
# text = 我 不 想 吃 了 。
# pinyin = Wǒ bù xiǎng chī le.
# text_en = I don't want to eat anymore.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGFR96B
1	我	我	PRON	_	Person=1	3	subj	_	_
2	不	不	ADV	_	Polarity=Neg	3	mod	_	highlight=red
3	想	想	AUX	_	_	0	root	_	_
4	吃	吃	VERB	_	_	3	comp:aux	_	_
5	了	了	PART	_	_	3	discourse	_	_
6	。	。	PUNCT	_	_	3	punct	_	_
{{< /conll_interactive >}}

### 2) 没 (méi) 
This is often used to negate past actions or to express the absence of something. For example, "我没去" (Wǒ méi qù) means "I didn't go." Note that 没 is also used in the negative form of the verb 有 (to have), as in "我没有书" (Wǒ méiyǒu shū) meaning "I don't have a book."

Negation of the existence VERB 有 (yǒu - to have) : 
{{< conll_interactive >}}
# sent_id = 1
# text = 我 没有 问题。
# pinyin = Wǒ méiyǒu wèntí.
# text_en = I don't have any questions.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGPNV3Q
1	我	我	PRON	_	Person=1	3	subj	_	_
2	没	没	ADV	_	_	3	mod	_	highlight=red
3	有	有	VERB	_	_	0	root	_	_
4	问	问	NOUN	_	_	3	comp:obj	_	_
5	题	题	NOUN	_	_	4	@m	_	_
6	。	。	PUNCT	_	_	3	punct	_	_
{{< /conll_interactive >}}


Negation of the perfective AUX 有 (yǒu - perfective) : 
{{< conll_interactive >}}
# sent_id = 284
# text = 她 没有 看到 你。
# pinyin = Tā méiyǒu kàndào nǐ.
# text_en = She didn't see you.
# url = https://resources.allsetlearning.com/chinese/grammar/ASGAUCXK
1	她	她	PRON	_	Person=3	3	subj	_	_
2	没	没	ADV	_	_	3	mod	_	highlight=red
3	有	有	AUX	_	_	0	root	_	_
4	看	看	VERB	_	_	3	comp:aux	_	_
5	到	到	VERB	_	_	4	comp:res	_	_
6	你	你	PRON	_	Person=2	4	comp:obj	_	_
7	。	。	PUNCT	_	_	3	punct	_	_
{{< /conll_interactive >}}

When negating the perfective 有, this last one can be ommitted and the 没 will directly direct the verb : 
{{< conll_interactive >}}
# user_id = kiriangui
# text = 你 昨天 没 回家 吗？
# pinyin = Nǐ zuótiān méi huíjiā ma?
# text_en = You didn't go back home yesterday?
# url = https://resources.allsetlearning.com/chinese/grammar/ASGAUCXK
1	你	你	PRON	_	Person=2	5	subj	_	_
2	昨	昨	NOUN	_	_	5	mod	_	_
3	天	天	NOUN	_	_	2	@m	_	_
4	没	没	ADV	_	Polarity=Neg	5	mod	_	highlight=red
5	回	回	VERB	_	_	0	root	_	_
6	家	家	NOUN	_	_	5	comp:obj	_	_
7	吗	吗	PART	_	Mood=Inter	5	discourse	_	_
8	？	？	PUNCT	_	_	5	punct	_	_
{{< /conll_interactive >}}


## Morphological negation
1) 非 (fēi): This prefix negates nouns, making them the opposite of what they originally mean, similar to the English "un-" or "non-". For example, "非法" (fēifǎ) means "illegal."

2) 未 (wèi): This prefix is often used in formal or literary contexts to mean "not yet." For example, "未完成" (wèi wánchéng) means "not yet completed."

3) 否 (fǒu): This is more formal and often used in written language, it means "no" or "not". For example, "否定" (fǒudìng) means "to deny."

4) 勿 (wù): This is a classical or literary way to express a negative imperative, similar to "别" (bié). For example, "勿忘我" (Wù wàng wǒ) means "Don't forget me."

5) 无 (wú): This is a more formal or literary way to express the absence of something, similar to "没有" (méiyǒu). For example, "无聊" (Wúliáo) means "boring" or literally "without chat."

6) 禁 (jìn): Often used in the sense of "prohibit" or "ban," implying a strong negation. For example, "禁烟" (Jìn yān) means "No Smoking."

7) 决 (jué): This is used to express a strong negative determination, such as "决不" (jué bù) means "never."

8) 免 (miǎn): This means to exempt or to avoid, and it is often used to politely turn down something. For example, "免谢" (Miǎn xiè) means "No need to thank."