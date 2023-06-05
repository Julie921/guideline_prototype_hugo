The Beja treebank contains 684 words if we count both stems and clitics; 39% of words are clitics. The  
treebank contains 244 affixes for 418 stems, or a proportion of 58%. 59% of them are suffixes and 41%  
prefixes. 88% of the affixes are on verbs, 7% on nouns, and 5% on auxiliaries. All affixes on nouns are  
suffixes. Not all inflectional morphemes are affixes: 44% of the stems are in fact inflected forms,  
containing an inseparable inflectional morpheme, which increases the proportion of inflectional  
morphemes to 102% (102 inflectional morphemes for 100 stems).  
Beja is a head-final language: only 11% of the dependencies between two stems have the governor  
before the dependent in the SUD version of the treebank. Among the 31 dependencies concerned, 11  
are for modifiers, 6 for discourse markers, 4 for dislocated objects, 2 for objects in canonical position,  
and 2 for determiners. Clitics occur on both sides: 47% are proclitics and 53% are enclitics. Clitics are  
mainly on verbs (56%) and nouns (38%). Clitics on nouns are determiners (70%), possessives (15%),  
postpositions (11%), and coordinating conjunctions (3%). Clitics on verbs are subordinating  
conjunctions (35%), object pronouns (25%), coordinating conjunctions (14%), an optative particle (2%),  
and, on nominalized forms, determiners (15%) and copulas (8%).  
Beja adpositions are postpositions, either as independent words (Figure 10) or as enclitics  
(Figure 11)

enclitics : 
# sent_id = BEJ_MV_NARR_01_shelter_065-070
# text = bak ʔabk -i -n i- ni =oː =hoːb / hoːj sallam -am -an =t // ontʔa / doːr =ka toː= ʃa kitʔ -a =t tam -a =t ni- ki /
# text_wb = bak ʔabkin ini =oː =hoːb / hoːj sallamaman =t // ontʔa / doːr =ka toː= ʃa kitʔa =t tama =t niki /
# text_en = when he told me: "So take it like that!", I took it from him, and  then, we would cut and eat the meat in turn [and]
# phonetic_text = bak ʔabkin ijoːhoːb / hoːj sallamamant // ontʔa / doːrka toːʃa kitʔat tamat niki /
# sound_url = https://api.nakala.fr/data/10.34847/nkl.d67a57yq/883c5f613e52b14063d6c2a5541417cab054595c
1	bak	_	PART	DEICT	_	2	mod	_	AlignBegin=58718|AlignEnd=58986|GE=thus|Gloss=thus|RX=[DEICT].[MNR]|TokenType=Stem
2	ʔabk	_	VERB	V1	VerbClass=1	4	comp:aff	_	AlignBegin=58986|AlignEnd=59075|GE=take|Gloss=take|ReportedSpeech=Yes|RX=[V1]|TokenType=Stem
3	-i	_	PRON	TAM, PNG	Gender=Fem|Mood=Imp|Number=Sing	4	subj:aff	_	AlignBegin=59075|AlignEnd=59164|GE=-[IMP].[SG].[F]|RX=-[TAM].[PNG]|TokenType=InflAff
4	-n	_	AUX	SUFX	_	6	parataxis:obj	_	AlignBegin=59164|AlignEnd=59254|GE=-[EMPH]|RX=-[SUFX]|TokenType=InflAff
5	i-	_	PRON	PNG	Gender=Masc|Number=Sing|Person=3	6	subj:aff	_	AlignBegin=59254|AlignEnd=59321|GE=[3SG].[M]-|RX=[PNG]-|TokenType=InflAff
6	ni	_	VERB	V1, IRG	Aspect=Perf|VerbClass=1	8	comp:obj	_	AlignBegin=59321|AlignEnd=59388|GE=say\[PFV]|Gloss=say|RX=[V1].[IRG]|TokenType=Stem
7	=oː	_	PRON	PRO	Number=Sing|Person=1	6	comp:obj	_	AlignBegin=59388|AlignEnd=59455|GE==[OBJ].[1SG]|RX==[PRO]|TokenType=Clit
8	=hoːb	_	SCONJ	CONJ	_	12	mod	_	AlignBegin=59455|AlignEnd=59522|GE==when|Gloss==when|RX==[CONJ]|TokenType=Clit
9	/	_	PUNCT	PUNCT	_	8	punct	_	AlignBegin=59522|AlignEnd=59790|TokenType=Break
10	hoːj	_	PRON	PRO	Case=Abl	12	comp:obl	_	AlignBegin=59790|AlignEnd=60157|GE=[ABL].[3]|RX=[PRO]|TokenType=Stem
11	sallam	_	VERB	V2	VerbClass=2	12	comp:aff	_	AlignBegin=60157|AlignEnd=60248|GE=give|Gloss=give|RX=[V2]|TokenType=Stem
12	-am	_	AUX	V2	VerbClass=2|Voice=Mid	23	conj:coord	_	AlignBegin=60248|AlignEnd=60340|DerPos=VERB|GE=-[MID]|RX=-[V2].[DER]|TokenType=DerAff
13	-an	_	PRON	TAM, PNG	Aspect=Pfv|Number=Sing|Person=1	12	subj:aff	_	AlignBegin=60340|AlignEnd=60432|GE=-[PFV].[1SG]|RX=-[TAM].[PNG]|TokenType=InflAff
14	=t	_	CCONJ	CCONJ	_	12	cc	_	AlignBegin=60432|AlignEnd=60524|GE==[COORD]|RX==[CONJ]|TokenType=Clit
15	//	_	PUNCT	PUNCT	_	12	punct	_	AlignBegin=60524|AlignEnd=61267|TokenType=Break
16	ontʔa	_	PART	PTCL	_	4	discourse	_	AlignBegin=61267|AlignEnd=61443|GE=now|Gloss=now|RX=[PTCL]|TokenType=Stem
17	/	_	PUNCT	PUNCT	_	16	punct	_	AlignBegin=61443|AlignEnd=61620|TokenType=Break
18	doːr	_	NOUN	N	Gender=Masc	19	comp:obj	_	AlignBegin=61620|AlignEnd=61844|GE=time|Gloss=time|RX=[N].[M]|TokenType=Stem
19	=ka	_	ADP	POSTP	Case=Dis	22	mod	_	AlignBegin=61844|AlignEnd=62068|GE==[DISTR]|RX==[POSTP]|TokenType=Clit
20	toː=	_	DET	DET	Case=Acc|Definite=Def|Gender=Fem|Number=Sing	21	det	_	AlignBegin=62068|AlignEnd=62292|GE=[DEF].[SG].[F].[ACC]=|RX=[DET]=|TokenType=Clit
21	ʃa	_	NOUN	N	Gender=Fem	22	comp:obj	_	AlignBegin=62292|AlignEnd=62517|GE=meat|Gloss=meat|RX=[N].[F]|TokenType=Stem
22	kitʔ	_	VERB	V1	VerbClass=1	23	comp:aff	_	AlignBegin=62517|AlignEnd=62666|GE=cut|Gloss=cut|RX=[V1]|TokenType=Stem
23	-a	_	SCONJ	CVB	Aspect=Perf|VerbForm=Conv	26	conj:coord	_	AlignBegin=62666|AlignEnd=62816|GE=-[CVB].[MNR]|RX=-[PRF]|TokenType=InflAff
24	=t	_	DET	DET	Definite=Ind|Gender=Fem	23	det	_	AlignBegin=62816|AlignEnd=62966|GE==[INDF].[F]|RX==[DET]|TokenType=Clit
25	tam	_	VERB	V2	VerbClass=2	26	comp:aff	_	AlignBegin=62966|AlignEnd=63115|GE=eat|Gloss=eat|RX=[V2]|TokenType=Stem
26	-a	_	SCONJ	CVB	Aspect=Perf|VerbForm=Conv	29	comp:pred	_	AlignBegin=63115|AlignEnd=63264|GE=-[CVB].[MNR]|RX=-[PRF]|TokenType=InflAff
27	=t	_	DET	DET	Definite=Ind|Gender=Fem	26	det	_	AlignBegin=63264|AlignEnd=63414|GE==[INDF].[F]|RX==[DET]|TokenType=Clit
28	ni-	_	PRON	PNG	Number=Plur|Person=1	29	subj:aff	_	AlignBegin=63414|AlignEnd=63638|GE=[1PL]-|RX=[PNG]-|TokenType=InflAff
29	ki	_	AUX	AUX	Aspect=Perf	0	root	_	AlignBegin=63638|AlignEnd=63863|GE=become\[PFV]|Gloss=become|RX=[AUX].[PRF]|TokenType=Stem
30	/	_	PUNCT	PUNCT	_	29	punct	_	AlignBegin=63863|AlignEnd=65384|TokenType=Break


independant words : # sent_id = BEJ_MV_NARR_01_shelter_015-024
# text = mhiːn / i- muːki =eːb oː= biri hariw -eː / liːlaːw -i geːb // kirra -jaː =b iː- ktiː -na i= bʔaɖ i- sini =joː =hoːb / i= mbʔaɖ -i whiː / a- sʔa i- ni //
# text_wb = mhiːn / imuːki =eːb oː= biri hariweː / liːlaːwi geːb // kirrajaː =b iːktiːna i= bʔaɖ isini =joː =hoːb / i= mbʔaɖi whiː / asʔa ini //
# text_en = Looking for a place where to take refuge from the rain,  when I found the wrapped straw mats (a straw tent) next to a rock, I sat down under the tent", he said.
# phonetic_text = mhiːn / imuːkjeːb oːbiri harweː / liːlaːwi geːb // kirrajaːb iːktiːna ibʔaɖ isinijoːhoːb / imbʔaɖi whiː / asʔa ini //
# sound_url = https://api.nakala.fr/data/10.34847/nkl.d67a57yq/883c5f613e52b14063d6c2a5541417cab054595c
1	mhiːn	_	NOUN	N	Gender=Masc	8	comp:obj	_	AlignBegin=9063|AlignEnd=9336|GE=place|Gloss=place|RX=[N].[M]|TokenType=Stem
2	/	_	PUNCT	PUNCT	_	1	punct	_	AlignBegin=9336|AlignEnd=9609|TokenType=Break
3	i-	_	PRON	PNG	Gender=Masc|Number=Sing|Person=3	4	subj:aff	_	AlignBegin=9609|AlignEnd=9744|GE=[3SG].[M]-|RX=[PNG]-|TokenType=InflAff
4	muːki	_	VERB	V1	Aspect=Aor|VerbClass=1	5	comp:obj	_	AlignBegin=9744|AlignEnd=9880|GE=take_shelter\[INT].[AOR]|Gloss=take_shelter|RX=[V1].[DER]|TokenType=Stem
5	=eːb	_	SCONJ	CONJ	Gender=Masc|Number=Sing	1	mod@relcl	_	AlignBegin=9880|AlignEnd=10016|GE==[REL].[SG].[M]|RX==[CONJ]|TokenType=Clit
6	oː=	_	DET	DET	Case=Acc|Definite=Def|Gender=Masc|Number=Sing	7	det	_	AlignBegin=10016|AlignEnd=10220|GE=[DEF].[SG].[M].[ACC]=|RX=[DET]=|TokenType=Clit
7	biri	_	NOUN	N	Gender=Masc	4	comp:obj	_	AlignBegin=10220|AlignEnd=10424|GE=rain|Gloss=rain|RX=[N].[M]|TokenType=Stem
8	hariw	_	VERB	V1	VerbClass=1	9	comp:aff	_	AlignBegin=10424|AlignEnd=10627|GE=seek|Gloss=seek|RX=[V1]|TokenType=Stem
9	-eː	_	SCONJ	CVB	VerbForm=Conv	24	mod	_	AlignBegin=10627|AlignEnd=10831|GE=-[CVB].[SMLT]|TokenType=InflAff
10	/	_	PUNCT	PUNCT	_	9	punct	_	AlignBegin=10831|AlignEnd=12268|TokenType=Break
11	liːlaːw	_	NOUN	N	Gender=Masc	12	comp:aff	_	AlignBegin=12268|AlignEnd=12410|GE=rock|Gloss=rock|RX=[N].[M]|TokenType=Stem
12	-i	_	ADP	CASE	Case=Gen	13	comp:obj	_	AlignBegin=12410|AlignEnd=12552|GE=-[GEN]|RX=-[CASE]|TokenType=InflAff
13	geːb	_	ADP	POSTP	_	24	mod	_	AlignBegin=12552|AlignEnd=12836|GE=beside|Gloss=beside|RX=[POSTP]|TokenType=Stem
14	//	_	PUNCT	PUNCT	_	13	punct	_	AlignBegin=12836|AlignEnd=13350|TokenType=Break
15	kirra	_	VERB	V1	VerbClass=1	16	comp:aff	_	AlignBegin=13350|AlignEnd=13477|GE=cover|Gloss=cover|RX=[V1]|TokenType=Stem
16	-jaː	_	SCONJ	CVB	Aspect=Perf|VerbForm=Conv	19	comp:aux	_	AlignBegin=13477|AlignEnd=13604|GE=-[CVB].[MNR]|RX=-[PRF]|TokenType=InflAff
17	=b	_	DET	DET	Case=Acc|Definite=Ind|Gender=Masc	16	det	_	AlignBegin=13604|AlignEnd=13732|GE==[INDF].[M].[ACC]|RX==[DET]|TokenType=Clit
18	iː-	_	PRON	PNG	_	19	subj:aff	_	AlignBegin=13732|AlignEnd=13859|GE=[3]-|RX=[PNG]-|TokenType=InflAff
19	ktiː	_	AUX	AUX	Aspect=Perf	22	mod@relcl	_	AlignBegin=13859|AlignEnd=13987|GE=become\[AOR]|Gloss=become|RX=[AUX].[PRF]|TokenType=Stem
20	-na	_	PRON	PNG	Number=Plur	19	subj:aff	_	AlignBegin=13987|AlignEnd=14115|GE=-[PL]|RX=-[PNG]|TokenType=InflAff
21	i=	_	DET	DET	Definite=Def|Gender=Masc	22	det	_	AlignBegin=14115|AlignEnd=14306|GE=[DEF].[M]=|RX=[DET]=|TokenType=Clit
22	bʔaɖ	_	NOUN	N	Gender=Masc	24	subj	_	AlignBegin=14306|AlignEnd=14497|GE=mat|Gloss=mat|RX=[N].[M]|TokenType=Stem
23	i-	_	PRON	PNG	Gender=Masc|Number=Sing|Person=3	24	subj:aff	_	AlignBegin=14497|AlignEnd=14592|GE=[3SG].[M]-|RX=[PNG]-|TokenType=InflAff
24	sini	_	VERB	V1	Aspect=Perf|VerbClass=1	26	comp:obj	_	AlignBegin=14592|AlignEnd=14688|GE=wait\[PFV]|Gloss=wait|RX=[V1]|TokenType=Stem
25	=joː	_	PRON	PRO	Number=Sing|Person=1	24	comp:obj	_	AlignBegin=14688|AlignEnd=14784|GE==[OBJ].[1SG]|RX==[PRO]|TokenType=Clit
26	=hoːb	_	SCONJ	CONJ	_	34	mod	_	AlignBegin=14784|AlignEnd=14880|GE==when|Gloss==when|RX==[CONJ]|TokenType=Clit
27	/	_	PUNCT	PUNCT	_	26	punct	_	AlignBegin=14880|AlignEnd=16106|TokenType=Break
28	i=	_	DET	DET	Definite=Def|Gender=Masc	30	det	_	AlignBegin=16106|AlignEnd=16214|GE=[DEF].[M]=|RX=[DET]=|TokenType=Clit
29	mbʔaɖ	_	NOUN	N	Gender=Masc	30	comp:aff	_	AlignBegin=16214|AlignEnd=16322|GE=mat|Gloss=mat|RX=[N].[M]|TokenType=Stem
30	-i	_	ADP	CASE	Case=Gen	31	comp:obj	_	AlignBegin=16322|AlignEnd=16431|GE=-[GEN]|RX=-[CASE]|TokenType=InflAff
31	whiː	_	ADP	POSTP	_	34	comp:obl	_	AlignBegin=16431|AlignEnd=16756|GE=under|Gloss=under|RX=[POSTP]|TokenType=Stem
32	/	_	PUNCT	PUNCT	_	31	punct	_	AlignBegin=16756|AlignEnd=17082|TokenType=Break
33	a-	_	PRON	PNG	Number=Sing|Person=1	34	subj:aff	_	AlignBegin=17082|AlignEnd=17217|GE=[1SG]-|RX=[PNG]-|TokenType=InflAff
34	sʔa	_	VERB	V1	Aspect=Perf|VerbClass=1|Voice=Mid	36	parataxis:obj	_	AlignBegin=17217|AlignEnd=17352|GE=sit\[MID].[PFV]|Gloss=sit|ReportedSpeech=Yes|RX=[V1].[DER]|TokenType=Stem
35	i-	_	PRON	PNG	Gender=Masc|Number=Sing|Person=3	36	subj:aff	_	AlignBegin=17352|AlignEnd=17487|GE=[3SG].[M]-|RX=[PNG]-|TokenType=InflAff
36	ni	_	VERB	V1, IRG	Aspect=Perf|VerbClass=1	0	root	_	AlignBegin=17487|AlignEnd=17623|GE=say\[PFV]|Gloss=say|RX=[V1].[IRG]|TokenType=Stem
37	//	_	PUNCT	PUNCT	_	36	punct	_	AlignBegin=17623|AlignEnd=18153|TokenType=Break
