# Directional Complement in Mandarin Chinese (comp:dir)

A "directional complement" (known as "directional verb compound” in UD) consists of a series of at least two verbs where the second verb is one of the directional or deitic motion verbs (or a combination of the two) in the below exhaustive list : 

## VERB + A : Directional motion
Eight verbs expressing directional motion:
- 上 (shàng) - "我爬上山" (wǒ pá shàng shān) - "I climb up the mountain"
- 下 (xià) - "他跑下楼" (tā pǎo xià lóu) - "He runs down the stairs"
- 出 (chū) - "我走出房间" (wǒ zǒu chū fángjiān) - "I walk out of the room"
- 进 (jìn) - "我们走进电影院" (wǒmen zǒu jìn diànyǐngyuàn) - "We walk into the movie theater"
- 回 (huí) - "他跑回家" (tā pǎo huí jiā) - "He runs back home"
- 过 (guò) - "他跳过河" (tā tiào guò hé) - "He jumps over the river"
- 开 (kāi) - "她拉开门" (tā lā kāi mén) - "She pulls open the door"
- 起 (qǐ) - "他拿起书" (tā ná qǐ shū) - "He picks up the book"

The main verb is the head of it's directional complement : 
VERB<-[comp:dir]- A

## VERB + B : Diectic motion 
Two verbs expressing deictic motion:
- 来 (lái) - "他走过来" (tā zǒu guò lái) - "He walks over here"
- 去 (qù) - "我走过去" (wǒ zǒu guò qù) - "I walk over there"

The main verb is the head of it's directional complement : 
VERB<-[comp:dir]- B


## VERB + AB : Directional and diectic motion
The combination of directional verbs (上/下/进/出/回/过/开/起) with deictic motion verbs (来/去) can result in more specific expressions of motion or direction. Here are the combinations:
- 上来 (shànglái) - "他把箱子提上来" (tā bǎ xiāngzi tí shànglái) - "He lifts the box up"
- 上去 (shàngqù) - "他爬上去" (tā pá shàngqù) - "He climbs up"
- 下来 (xiàlái) - "他滑下来" (tā huá xiàlái) - "He slides down"
- 下去 (xiàqù) - "我跳下去" (wǒ tiào xiàqù) - "I jump down"
- 进来 (jìnlái) - "请进来" (qǐng jìnlái) - "Please come in"
- 进去 (jìnqù) - "我走进去" (wǒ zǒu jìnqù) - "I walk in"
- 出来 (chūlái) - "他走出来" (tā zǒu chūlái) - "He walks out"
- 出去 (chūqù) - ""我带他们出去" (Wǒ dài tāmen chūqù) - "I take them out"
- 回来 (huílái) - "他会回来" (tā huì huílái) - "He will come back"
- 回去 (huíqù) - "我要回去" (wǒ yào huíqù) - "I need to go back"
- 过来 (guòlái) - "请过来" (qǐng guòlái) - "Please come over"
- 过去 (guòqù) - "我走过去" (wǒ zǒu guòqù) - "I walk over there"
- 开来 (kāilái) - "花儿开来了" (huā er kāilái le) - "The flowers have blossomed" (Note: 开来 in this sense is less common and has a more metaphorical usage)
- 开去 (kāiqù) - Not commonly used, as it doesn't make much sense in most contexts
- 起来 (qǐlái) - "他站起来" (tā zhàn qǐlái) - "He stands up"
- 起去 (qǐqù) - Not commonly used, as it doesn't make much sense in most contexts

This construction is annotated as a comp:dir relation both between the main verb and the directional complement group, and between each element of the directional complement group :
VERB <-[comp:dir]- A <-[comp:dir]- B


## Remarks
- You can find a SVC (see SVC in mandarin) construction at the end of directional complement verbs chain (我出去玩). The head of this word is the last verb of the directional complement verb chain (here 去) and the label is `comp:svc`.

## Other schemas and litterature
### UD : 
See page about compound:dir for mandarin in UD : https://universaldependencies.org/zh/dep/compound-dir.html

### Chinese grammar wiki :
For a more didactic explanation towards language learners, this ressource is really helpful : https://resources.allsetlearning.com/chinese/grammar/Direction_complement


