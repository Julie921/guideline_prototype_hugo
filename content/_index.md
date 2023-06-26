---
title: "Docs"
weight: 1
bookFlatSection: False
bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
bookSearch: true
---
# Welcome to Syntactic Universal Dependencies Guidelines (SUD)


## About Syntactic Universal Dependenciers (SUD)
![Surface Syntactic Universal Dependencies (SUD)](images/sud.svg) 
SUD is an annotation scheme for syntactic dependency treebanks, and has a nearly perfect degree of two-way convertibility with the Universal Dependencies scheme (UD). Contrary to UD, it is based on syntactic criteria (favoring functional heads) and the relations are defined on distributional and functional bases. This web site centralizes the information necessary to understand the annotation in SUD and to annotate from sratch. You can found the guidelines [here](./docs/_index.md)


## An Example of SUD annotation 

{{< conll_interactive >}}
# sent_id = email-enronsent19_01-0071
# text = I'm happy about this.
1	I	I	PRON	PRP	Case=Nom|Number=Sing|Person=1|PronType=Prs	2	subj	_	SpaceAfter=No
2	'm	be	AUX	VBP	Mood=Ind|Tense=Pres|VerbForm=Fin	0	root	_	_
3	happy	happy	ADJ	JJ	Degree=Pos	2	comp:pred	_	_
4	about	about	ADP	IN	_	3	mod	_	_
5	SUD	SUD	PROPN	DT	Number=Sing	4	comp:obj	_	SpaceAfter=No
6	.	.	PUNCT	.	_	2	punct	_	_
{{< /conll_interactive >}}


To see more examples, head over to the [universal SUD guidelines](./docs/_index.md). 

  

## Data
### Descriptions
In version 2.11 of SUD data, released in November 2022:
 * 7 corpora are built in the SUD format (called **Native SUD**)
 * 234 corpora are automatically converted to SUD from the corresponding UD data (version 2.11)

The full release SUD 2.11 contains 241 corpora.
Note that UD 2.11 has 243 corpora but two corpora cannot be released in the SUD version, because of their CC license which contain the **ND** (NoDerivative) flags:
 * [UD_Japanese-Modern](https://github.com/UniversalDependencies/UD_Japanese-Modern) &rarr; `License: CC BY-NC-ND 3.0`
 * [UD_Portuguese-CINTIL](https://github.com/UniversalDependencies/UD_Portuguese-CINTIL) &rarr; `License: CC BY-NC-ND 4.0`

### Download all corpora
Download the full set of 241 SUD corpora: [sud-treebanks-v2.11.tgz](https://grew.fr/download/sud-treebanks-v2.11.tgz).

### Native SUD corpora

In the table below, the 7 native SUD corpora are given.
Note that each corresponding UD version is obtained by automatic conversion.

| Corpus | Files | Grew-match |
|--------|------------|-------|
| [`SUD_Beja-NSC`](https://github.com/surfacesyntacticud/SUD_Beja-NSC) | [2.11](https://github.com/surfacesyntacticud/SUD_Beja-NSC/archive/refs/tags/r2.11.tar.gz) -- [latest](https://github.com/surfacesyntacticud/SUD_Beja-NSC/archive/master.zip) | [2.11](http://universal.grew.fr/?corpus=SUD_Beja-NSC@2.11) -- [latest](http://universal.grew.fr/?corpus=SUD_Beja-NSC@latest) |
| 🆕 [`SUD_Chinese-PatentChar`](https://github.com/surfacesyntacticud/SUD_Chinese-PatentChar) | [2.11](https://github.com/surfacesyntacticud/SUD_Chinese-PatentChar/archive/refs/tags/r2.11.tar.gz) -- [latest](https://github.com/surfacesyntacticud/SUD_Chinese-PatentChar/archive/master.zip) | [2.11](http://universal.grew.fr/?corpus=SUD_Chinese-PatentChar@2.11) -- [latest](http://universal.grew.fr/?corpus=SUD_Chinese-PatentChar@latest) |
| [`SUD_French-GSD`](https://github.com/surfacesyntacticud/SUD_French-GSD) | [2.11](https://github.com/surfacesyntacticud/SUD_French-GSD/archive/refs/tags/r2.11.tar.gz) -- [latest](https://github.com/surfacesyntacticud/SUD_French-GSD/archive/master.zip) | [2.11](http://universal.grew.fr/?corpus=SUD_French-GSD@2.11) -- [latest](http://universal.grew.fr/?corpus=SUD_French-GSD@latest) |
| [`SUD_French-ParisStories`](https://github.com/surfacesyntacticud/SUD_French-ParisStories) | [2.11](https://github.com/surfacesyntacticud/SUD_French-ParisStories/archive/refs/tags/r2.11.tar.gz) -- [latest](https://github.com/surfacesyntacticud/SUD_French-ParisStories/archive/master.zip) | [2.11](http://universal.grew.fr/?corpus=SUD_French-ParisStories@2.11) -- [latest](http://universal.grew.fr/?corpus=SUD_French-ParisStories@latest) |
| [`SUD_French-Rhapsodie`](https://github.com/surfacesyntacticud/SUD_French-Rhapsodie) | [2.11](https://github.com/surfacesyntacticud/SUD_French-Rhapsodie/archive/refs/tags/r2.11.tar.gz) -- [latest](https://github.com/surfacesyntacticud/SUD_French-Rhapsodie/archive/master.zip) | [2.11](http://universal.grew.fr/?corpus=SUD_French-Rhapsodie@2.11) -- [latest](http://universal.grew.fr/?corpus=SUD_French-Rhapsodie@latest) |
| [`SUD_Naija-NSC`](https://github.com/surfacesyntacticud/SUD_Naija-NSC) | [2.11](https://github.com/surfacesyntacticud/SUD_Naija-NSC/archive/refs/tags/r2.11.tar.gz) -- [latest](https://github.com/surfacesyntacticud/SUD_Naija-NSC/archive/master.zip) | [2.11](http://universal.grew.fr/?corpus=SUD_Naija-NSC@2.11) -- [latest](http://universal.grew.fr/?corpus=SUD_Naija-NSC@latest) |
| 🆕 [`SUD_Zaar-Autogramm`](https://github.com/surfacesyntacticud/SUD_Zaar-Autogramm) | [2.11](https://github.com/surfacesyntacticud/SUD_Zaar-Autogramm/archive/refs/tags/r2.11.tar.gz) -- [latest](https://github.com/surfacesyntacticud/SUD_Zaar-Autogramm/archive/master.zip) | [2.11](http://universal.grew.fr/?corpus=SUD_Zaar-Autogramm@2.11) -- [latest](http://universal.grew.fr/?corpus=SUD_Zaar-Autogramm@latest) |

### Conversion from UD

  * 234 corpora of SUD 2.11 are converted from UD. The version of the data and tools used:
    * input data: [version 2.11 of UD corpora](http://hdl.handle.net/11234/1-4923)
    * **Grew** conversion rules system: [tag `v2.11` of the conversion system](https://github.com/surfacesyntacticud/tools/tree/v2.11/converter)
    * tools: **Grew** version 1.10.0, **libcaml-grew** version 1.10.0 and **libcaml-conll** version 1.13.2


### Access to each corpus

In the table below, for each corpus you can access to the [Grew-match](http://universal.grew.fr/?corpus=SUD_English-ParTUT@2.11) query system.


| Corpus | Grew-match |
|--------|------------|
| 🆕 `Abaza-ATB` | [[Query](http://universal.grew.fr/?corpus=SUD_Abaza-ATB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Abaza-ATB@2.11_table.html)] |
| `Afrikaans-AfriBooms` | [[Query](http://universal.grew.fr/?corpus=SUD_Afrikaans-AfriBooms@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Afrikaans-AfriBooms@2.11_table.html)] |
| `Akkadian-PISANDUB` | [[Query](http://universal.grew.fr/?corpus=SUD_Akkadian-PISANDUB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Akkadian-PISANDUB@2.11_table.html)] |
| `Akkadian-RIAO` | [[Query](http://universal.grew.fr/?corpus=SUD_Akkadian-RIAO@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Akkadian-RIAO@2.11_table.html)] |
| `Akuntsu-TuDeT` | [[Query](http://universal.grew.fr/?corpus=SUD_Akuntsu-TuDeT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Akuntsu-TuDeT@2.11_table.html)] |
| `Albanian-TSA` | [[Query](http://universal.grew.fr/?corpus=SUD_Albanian-TSA@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Albanian-TSA@2.11_table.html)] |
| `Amharic-ATT` | [[Query](http://universal.grew.fr/?corpus=SUD_Amharic-ATT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Amharic-ATT@2.11_table.html)] |
| `Ancient_Greek-Perseus` | [[Query](http://universal.grew.fr/?corpus=SUD_Ancient_Greek-Perseus@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Ancient_Greek-Perseus@2.11_table.html)] |
| `Ancient_Greek-PROIEL` | [[Query](http://universal.grew.fr/?corpus=SUD_Ancient_Greek-PROIEL@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Ancient_Greek-PROIEL@2.11_table.html)] |
| `Ancient_Hebrew-PTNK` | [[Query](http://universal.grew.fr/?corpus=SUD_Ancient_Hebrew-PTNK@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Ancient_Hebrew-PTNK@2.11_table.html)] |
| `Apurina-UFPA` | [[Query](http://universal.grew.fr/?corpus=SUD_Apurina-UFPA@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Apurina-UFPA@2.11_table.html)] |
| `Arabic-NYUAD` | [[Query](http://universal.grew.fr/?corpus=SUD_Arabic-NYUAD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Arabic-NYUAD@2.11_table.html)] |
| `Arabic-PADT` | [[Query](http://universal.grew.fr/?corpus=SUD_Arabic-PADT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Arabic-PADT@2.11_table.html)] |
| `Arabic-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Arabic-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Arabic-PUD@2.11_table.html)] |
| `Armenian-ArmTDP` | [[Query](http://universal.grew.fr/?corpus=SUD_Armenian-ArmTDP@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Armenian-ArmTDP@2.11_table.html)] |
| `Armenian-BSUT` | [[Query](http://universal.grew.fr/?corpus=SUD_Armenian-BSUT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Armenian-BSUT@2.11_table.html)] |
| `Assyrian-AS` | [[Query](http://universal.grew.fr/?corpus=SUD_Assyrian-AS@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Assyrian-AS@2.11_table.html)] |
| `Bambara-CRB` | [[Query](http://universal.grew.fr/?corpus=SUD_Bambara-CRB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Bambara-CRB@2.11_table.html)] |
| `Basque-BDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Basque-BDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Basque-BDT@2.11_table.html)] |
| `Beja-NSC` (Native) | [[Query](http://universal.grew.fr/?corpus=SUD_Beja-NSC@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Beja-NSC@2.11_table.html)] |
| `Belarusian-HSE` | [[Query](http://universal.grew.fr/?corpus=SUD_Belarusian-HSE@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Belarusian-HSE@2.11_table.html)] |
| `Bengali-BRU` | [[Query](http://universal.grew.fr/?corpus=SUD_Bengali-BRU@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Bengali-BRU@2.11_table.html)] |
| `Bhojpuri-BHTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Bhojpuri-BHTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Bhojpuri-BHTB@2.11_table.html)] |
| `Breton-KEB` | [[Query](http://universal.grew.fr/?corpus=SUD_Breton-KEB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Breton-KEB@2.11_table.html)] |
| `Bulgarian-BTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Bulgarian-BTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Bulgarian-BTB@2.11_table.html)] |
| `Buryat-BDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Buryat-BDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Buryat-BDT@2.11_table.html)] |
| `Cantonese-HK` | [[Query](http://universal.grew.fr/?corpus=SUD_Cantonese-HK@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Cantonese-HK@2.11_table.html)] |
| `Catalan-AnCora` | [[Query](http://universal.grew.fr/?corpus=SUD_Catalan-AnCora@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Catalan-AnCora@2.11_table.html)] |
| `Cebuano-GJA` | [[Query](http://universal.grew.fr/?corpus=SUD_Cebuano-GJA@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Cebuano-GJA@2.11_table.html)] |
| `Chinese-CFL` | [[Query](http://universal.grew.fr/?corpus=SUD_Chinese-CFL@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Chinese-CFL@2.11_table.html)] |
| `Chinese-GSD` | [[Query](http://universal.grew.fr/?corpus=SUD_Chinese-GSD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Chinese-GSD@2.11_table.html)] |
| `Chinese-GSDSimp` | [[Query](http://universal.grew.fr/?corpus=SUD_Chinese-GSDSimp@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Chinese-GSDSimp@2.11_table.html)] |
| `Chinese-HK` | [[Query](http://universal.grew.fr/?corpus=SUD_Chinese-HK@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Chinese-HK@2.11_table.html)] |
| 🆕 `Chinese-PatentChar` | [[Query](http://universal.grew.fr/?corpus=SUD_Chinese-PatentChar@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Chinese-PatentChar@2.11_table.html)] |
| `Chinese-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Chinese-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Chinese-PUD@2.11_table.html)] |
| `Chukchi-HSE` | [[Query](http://universal.grew.fr/?corpus=SUD_Chukchi-HSE@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Chukchi-HSE@2.11_table.html)] |
| `Classical_Chinese-Kyoto` | [[Query](http://universal.grew.fr/?corpus=SUD_Classical_Chinese-Kyoto@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Classical_Chinese-Kyoto@2.11_table.html)] |
| `Coptic-Scriptorium` | [[Query](http://universal.grew.fr/?corpus=SUD_Coptic-Scriptorium@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Coptic-Scriptorium@2.11_table.html)] |
| `Croatian-SET` | [[Query](http://universal.grew.fr/?corpus=SUD_Croatian-SET@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Croatian-SET@2.11_table.html)] |
| `Czech-CAC` | [[Query](http://universal.grew.fr/?corpus=SUD_Czech-CAC@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Czech-CAC@2.11_table.html)] |
| `Czech-CLTT` | [[Query](http://universal.grew.fr/?corpus=SUD_Czech-CLTT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Czech-CLTT@2.11_table.html)] |
| `Czech-FicTree` | [[Query](http://universal.grew.fr/?corpus=SUD_Czech-FicTree@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Czech-FicTree@2.11_table.html)] |
| `Czech-PDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Czech-PDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Czech-PDT@2.11_table.html)] |
| `Czech-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Czech-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Czech-PUD@2.11_table.html)] |
| `Danish-DDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Danish-DDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Danish-DDT@2.11_table.html)] |
| `Dutch-Alpino` | [[Query](http://universal.grew.fr/?corpus=SUD_Dutch-Alpino@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Dutch-Alpino@2.11_table.html)] |
| `Dutch-LassySmall` | [[Query](http://universal.grew.fr/?corpus=SUD_Dutch-LassySmall@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Dutch-LassySmall@2.11_table.html)] |
| `English-Atis` | [[Query](http://universal.grew.fr/?corpus=SUD_English-Atis@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_English-Atis@2.11_table.html)] |
| `English-ESL` | [[Query](http://universal.grew.fr/?corpus=SUD_English-ESL@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_English-ESL@2.11_table.html)] |
| `English-EWT` | [[Query](http://universal.grew.fr/?corpus=SUD_English-EWT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_English-EWT@2.11_table.html)] |
| `English-GUM` | [[Query](http://universal.grew.fr/?corpus=SUD_English-GUM@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_English-GUM@2.11_table.html)] |
| `English-GUMReddit` | [[Query](http://universal.grew.fr/?corpus=SUD_English-GUMReddit@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_English-GUMReddit@2.11_table.html)] |
| `English-LinES` | [[Query](http://universal.grew.fr/?corpus=SUD_English-LinES@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_English-LinES@2.11_table.html)] |
| `English-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_English-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_English-PUD@2.11_table.html)] |
| `English-Pronouns` | [[Query](http://universal.grew.fr/?corpus=SUD_English-Pronouns@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_English-Pronouns@2.11_table.html)] |
| `Erzya-JR` | [[Query](http://universal.grew.fr/?corpus=SUD_Erzya-JR@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Erzya-JR@2.11_table.html)] |
| `Estonian-EDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Estonian-EDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Estonian-EDT@2.11_table.html)] |
| `Estonian-EWT` | [[Query](http://universal.grew.fr/?corpus=SUD_Estonian-EWT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Estonian-EWT@2.11_table.html)] |
| `Faroese-OFT` | [[Query](http://universal.grew.fr/?corpus=SUD_Faroese-OFT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Faroese-OFT@2.11_table.html)] |
| `Faroese-FarPaHC` | [[Query](http://universal.grew.fr/?corpus=SUD_Faroese-FarPaHC@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Faroese-FarPaHC@2.11_table.html)] |
| `Finnish-FTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Finnish-FTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Finnish-FTB@2.11_table.html)] |
| `Finnish-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Finnish-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Finnish-PUD@2.11_table.html)] |
| `Finnish-TDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Finnish-TDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Finnish-TDT@2.11_table.html)] |
| `Finnish-OOD` | [[Query](http://universal.grew.fr/?corpus=SUD_Finnish-OOD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Finnish-OOD@2.11_table.html)] |
| `French-FQB` | [[Query](http://universal.grew.fr/?corpus=SUD_French-FQB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_French-FQB@2.11_table.html)] |
| `French-FTB` | [[Query](http://universal.grew.fr/?corpus=SUD_French-FTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_French-FTB@2.11_table.html)] |
| `French-GSD` (Native) | [[Query](http://universal.grew.fr/?corpus=SUD_French-GSD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_French-GSD@2.11_table.html)] |
| `French-ParTUT` | [[Query](http://universal.grew.fr/?corpus=SUD_French-ParTUT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_French-ParTUT@2.11_table.html)] |
| `French-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_French-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_French-PUD@2.11_table.html)] |
| `French-Sequoia` | [[Query](http://universal.grew.fr/?corpus=SUD_French-Sequoia@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_French-Sequoia@2.11_table.html)] |
| `French-ParisStories` (Native)  | [[Query](http://universal.grew.fr/?corpus=SUD_French-ParisStories@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_French-ParisStories@2.11_table.html)] |
| `French-Rhapsodie` (Native)  | [[Query](http://universal.grew.fr/?corpus=SUD_French-Rhapsodie@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_French-Rhapsodie@2.11_table.html)] |
| `Frisian_Dutch-Fame` | [[Query](http://universal.grew.fr/?corpus=SUD_Frisian_Dutch-Fame@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Frisian_Dutch-Fame@2.11_table.html)] |
| `Galician-CTG` | [[Query](http://universal.grew.fr/?corpus=SUD_Galician-CTG@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Galician-CTG@2.11_table.html)] |
| `Galician-TreeGal` | [[Query](http://universal.grew.fr/?corpus=SUD_Galician-TreeGal@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Galician-TreeGal@2.11_table.html)] |
| `German-GSD` | [[Query](http://universal.grew.fr/?corpus=SUD_German-GSD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_German-GSD@2.11_table.html)] |
| `German-HDT` | [[Query](http://universal.grew.fr/?corpus=SUD_German-HDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_German-HDT@2.11_table.html)] |
| `German-LIT` | [[Query](http://universal.grew.fr/?corpus=SUD_German-LIT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_German-LIT@2.11_table.html)] |
| `German-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_German-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_German-PUD@2.11_table.html)] |
| `Gothic-PROIEL` | [[Query](http://universal.grew.fr/?corpus=SUD_Gothic-PROIEL@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Gothic-PROIEL@2.11_table.html)] |
| `Greek-GDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Greek-GDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Greek-GDT@2.11_table.html)] |
| `Guajajara-TuDeT` | [[Query](http://universal.grew.fr/?corpus=SUD_Guajajara-TuDeT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Guajajara-TuDeT@2.11_table.html)] |
| `Guarani-OldTuDeT` | [[Query](http://universal.grew.fr/?corpus=SUD_Guarani-OldTuDeT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Guarani-OldTuDeT@2.11_table.html)] |
| `Hebrew-HTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Hebrew-HTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Hebrew-HTB@2.11_table.html)] |
| `Hebrew-IAHLTwiki` | [[Query](http://universal.grew.fr/?corpus=SUD_Hebrew-IAHLTwiki@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Hebrew-IAHLTwiki@2.11_table.html)] |
| `Hindi_English-HIENCS` | [[Query](http://universal.grew.fr/?corpus=SUD_Hindi_English-HIENCS@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Hindi_English-HIENCS@2.11_table.html)] |
| `Hindi-HDTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Hindi-HDTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Hindi-HDTB@2.11_table.html)] |
| `Hindi-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Hindi-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Hindi-PUD@2.11_table.html)] |
| `Hittite-HitTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Hittite-HitTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Hittite-HitTB@2.11_table.html)] |
| `Hungarian-Szeged` | [[Query](http://universal.grew.fr/?corpus=SUD_Hungarian-Szeged@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Hungarian-Szeged@2.11_table.html)] |
| `Icelandic-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Icelandic-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Icelandic-PUD@2.11_table.html)] |
| `Icelandic-Modern` | [[Query](http://universal.grew.fr/?corpus=SUD_Icelandic-Modern@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Icelandic-Modern@2.11_table.html)] |
| `Icelandic-IcePaHC` | [[Query](http://universal.grew.fr/?corpus=SUD_Icelandic-IcePaHC@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Icelandic-IcePaHC@2.11_table.html)] |
| `Indonesian-GSD` | [[Query](http://universal.grew.fr/?corpus=SUD_Indonesian-GSD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Indonesian-GSD@2.11_table.html)] |
| `Indonesian-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Indonesian-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Indonesian-PUD@2.11_table.html)] |
| `Indonesian-CSUI` | [[Query](http://universal.grew.fr/?corpus=SUD_Indonesian-CSUI@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Indonesian-CSUI@2.11_table.html)] |
| 🆕 `Irish-Cadhan` | [[Query](http://universal.grew.fr/?corpus=SUD_Irish-Cadhan@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Irish-Cadhan@2.11_table.html)] |
| `Irish-IDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Irish-IDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Irish-IDT@2.11_table.html)] |
| `Irish-TwittIrish` | [[Query](http://universal.grew.fr/?corpus=SUD_Irish-TwittIrish@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Irish-TwittIrish@2.11_table.html)] |
| `Italian-ISDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Italian-ISDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Italian-ISDT@2.11_table.html)] |
| `Italian-MarkIT` | [[Query](http://universal.grew.fr/?corpus=SUD_Italian-MarkIT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Italian-MarkIT@2.11_table.html)] |
| `Italian-ParTUT` | [[Query](http://universal.grew.fr/?corpus=SUD_Italian-ParTUT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Italian-ParTUT@2.11_table.html)] |
| `Italian-PoSTWITA` | [[Query](http://universal.grew.fr/?corpus=SUD_Italian-PoSTWITA@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Italian-PoSTWITA@2.11_table.html)] |
| `Italian-TWITTIRO` | [[Query](http://universal.grew.fr/?corpus=SUD_Italian-TWITTIRO@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Italian-TWITTIRO@2.11_table.html)] |
| 🆕 `Italian-ParlaMint` | [[Query](http://universal.grew.fr/?corpus=SUD_Italian-ParlaMint@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Italian-ParlaMint@2.11_table.html)] |
| `Italian-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Italian-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Italian-PUD@2.11_table.html)] |
| `Italian-Valico` | [[Query](http://universal.grew.fr/?corpus=SUD_Italian-Valico@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Italian-Valico@2.11_table.html)] |
| `Italian-VIT` | [[Query](http://universal.grew.fr/?corpus=SUD_Italian-VIT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Italian-VIT@2.11_table.html)] |
| `Japanese-BCCWJ` | [[Query](http://universal.grew.fr/?corpus=SUD_Japanese-BCCWJ@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Japanese-BCCWJ@2.11_table.html)] |
| `Japanese-BCCWJLUW` | [[Query](http://universal.grew.fr/?corpus=SUD_Japanese-BCCWJLUW@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Japanese-BCCWJLUW@2.11_table.html)] |
| `Japanese-GSD` | [[Query](http://universal.grew.fr/?corpus=SUD_Japanese-GSD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Japanese-GSD@2.11_table.html)] |
| `Japanese-GSDLUW` | [[Query](http://universal.grew.fr/?corpus=SUD_Japanese-GSDLUW@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Japanese-GSDLUW@2.11_table.html)] |
| `Japanese-Modern` | [[Query](http://universal.grew.fr/?corpus=SUD_Japanese-Modern@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Japanese-Modern@2.11_table.html)] |
| `Japanese-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Japanese-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Japanese-PUD@2.11_table.html)] |
| `Japanese-PUDLUW` | [[Query](http://universal.grew.fr/?corpus=SUD_Japanese-PUDLUW@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Japanese-PUDLUW@2.11_table.html)] |
| `Javanese-CSUI` | [[Query](http://universal.grew.fr/?corpus=SUD_Javanese-CSUI@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Javanese-CSUI@2.11_table.html)] |
| `Kaapor-TuDeT` | [[Query](http://universal.grew.fr/?corpus=SUD_Kaapor-TuDeT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Kaapor-TuDeT@2.11_table.html)] |
| `Kangri-KDTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Kangri-KDTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Kangri-KDTB@2.11_table.html)] |
| `Karelian-KKPP` | [[Query](http://universal.grew.fr/?corpus=SUD_Karelian-KKPP@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Karelian-KKPP@2.11_table.html)] |
| `Karo-TuDeT` | [[Query](http://universal.grew.fr/?corpus=SUD_Karo-TuDeT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Karo-TuDeT@2.11_table.html)] |
| `Kazakh-KTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Kazakh-KTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Kazakh-KTB@2.11_table.html)] |
| `Khunsari-AHA` | [[Query](http://universal.grew.fr/?corpus=SUD_Khunsari-AHA@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Khunsari-AHA@2.11_table.html)] |
| `Kiche-IU` | [[Query](http://universal.grew.fr/?corpus=SUD_Kiche-IU@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Kiche-IU@2.11_table.html)] |
| `Komi_Permyak-UH` | [[Query](http://universal.grew.fr/?corpus=SUD_Komi_Permyak-UH@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Komi_Permyak-UH@2.11_table.html)] |
| `Komi_Zyrian-IKDP` | [[Query](http://universal.grew.fr/?corpus=SUD_Komi_Zyrian-IKDP@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Komi_Zyrian-IKDP@2.11_table.html)] |
| `Komi_Zyrian-Lattice` | [[Query](http://universal.grew.fr/?corpus=SUD_Komi_Zyrian-Lattice@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Komi_Zyrian-Lattice@2.11_table.html)] |
| `Korean-GSD` | [[Query](http://universal.grew.fr/?corpus=SUD_Korean-GSD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Korean-GSD@2.11_table.html)] |
| `Korean-Kaist` | [[Query](http://universal.grew.fr/?corpus=SUD_Korean-Kaist@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Korean-Kaist@2.11_table.html)] |
| `Korean-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Korean-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Korean-PUD@2.11_table.html)] |
| `Kurmanji-MG` | [[Query](http://universal.grew.fr/?corpus=SUD_Kurmanji-MG@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Kurmanji-MG@2.11_table.html)] |
| `Latin-ITTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Latin-ITTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Latin-ITTB@2.11_table.html)] |
| `Latin-LLCT` | [[Query](http://universal.grew.fr/?corpus=SUD_Latin-LLCT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Latin-LLCT@2.11_table.html)] |
| `Latin-Perseus` | [[Query](http://universal.grew.fr/?corpus=SUD_Latin-Perseus@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Latin-Perseus@2.11_table.html)] |
| `Latin-PROIEL` | [[Query](http://universal.grew.fr/?corpus=SUD_Latin-PROIEL@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Latin-PROIEL@2.11_table.html)] |
| `Latin-UDante` | [[Query](http://universal.grew.fr/?corpus=SUD_Latin-UDante@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Latin-UDante@2.11_table.html)] |
| `Latvian-LVTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Latvian-LVTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Latvian-LVTB@2.11_table.html)] |
| `Ligurian-GLT` | [[Query](http://universal.grew.fr/?corpus=SUD_Ligurian-GLT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Ligurian-GLT@2.11_table.html)] |
| `Lithuanian-ALKSNIS` | [[Query](http://universal.grew.fr/?corpus=SUD_Lithuanian-ALKSNIS@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Lithuanian-ALKSNIS@2.11_table.html)] |
| `Lithuanian-HSE` | [[Query](http://universal.grew.fr/?corpus=SUD_Lithuanian-HSE@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Lithuanian-HSE@2.11_table.html)] |
| `Livvi-KKPP` | [[Query](http://universal.grew.fr/?corpus=SUD_Livvi-KKPP@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Livvi-KKPP@2.11_table.html)] |
| `Low_Saxon-LSDC` | [[Query](http://universal.grew.fr/?corpus=SUD_Low_Saxon-LSDC@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Low_Saxon-LSDC@2.11_table.html)] |
| `Madi-Jarawara` | [[Query](http://universal.grew.fr/?corpus=SUD_Madi-Jarawara@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Madi-Jarawara@2.11_table.html)] |
| `Makurap-TuDeT` | [[Query](http://universal.grew.fr/?corpus=SUD_Makurap-TuDeT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Makurap-TuDeT@2.11_table.html)] |
| 🆕 `Malayalam-UFA` | [[Query](http://universal.grew.fr/?corpus=SUD_Malayalam-UFA@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Malayalam-UFA@2.11_table.html)] |
| `Maltese-MUDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Maltese-MUDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Maltese-MUDT@2.11_table.html)] |
| `Manx-Cadhan` | [[Query](http://universal.grew.fr/?corpus=SUD_Manx-Cadhan@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Manx-Cadhan@2.11_table.html)] |
| `Marathi-UFAL` | [[Query](http://universal.grew.fr/?corpus=SUD_Marathi-UFAL@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Marathi-UFAL@2.11_table.html)] |
| `Mbya_Guarani-Dooley` | [[Query](http://universal.grew.fr/?corpus=SUD_Mbya_Guarani-Dooley@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Mbya_Guarani-Dooley@2.11_table.html)] |
| `Mbya_Guarani-Thomas` | [[Query](http://universal.grew.fr/?corpus=SUD_Mbya_Guarani-Thomas@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Mbya_Guarani-Thomas@2.11_table.html)] |
| `Moksha-JR` | [[Query](http://universal.grew.fr/?corpus=SUD_Moksha-JR@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Moksha-JR@2.11_table.html)] |
| `Munduruku-TuDeT` | [[Query](http://universal.grew.fr/?corpus=SUD_Munduruku-TuDeT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Munduruku-TuDeT@2.11_table.html)] |
| `Naija-NSC` (Native) | [[Query](http://universal.grew.fr/?corpus=SUD_Naija-NSC@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Naija-NSC@2.11_table.html)] |
| `Nayini-AHA` | [[Query](http://universal.grew.fr/?corpus=SUD_Nayini-AHA@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Nayini-AHA@2.11_table.html)] |
| `Neapolitan-RB` | [[Query](http://universal.grew.fr/?corpus=SUD_Neapolitan-RB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Neapolitan-RB@2.11_table.html)] |
| 🆕 `Nheengatu-CompLin` | [[Query](http://universal.grew.fr/?corpus=SUD_Nheengatu-CompLin@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Nheengatu-CompLin@2.11_table.html)] |
| `North_Sami-Giella` | [[Query](http://universal.grew.fr/?corpus=SUD_North_Sami-Giella@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_North_Sami-Giella@2.11_table.html)] |
| `Norwegian-Bokmaal` | [[Query](http://universal.grew.fr/?corpus=SUD_Norwegian-Bokmaal@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Norwegian-Bokmaal@2.11_table.html)] |
| `Norwegian-Nynorsk` | [[Query](http://universal.grew.fr/?corpus=SUD_Norwegian-Nynorsk@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Norwegian-Nynorsk@2.11_table.html)] |
| `Norwegian-NynorskLIA` | [[Query](http://universal.grew.fr/?corpus=SUD_Norwegian-NynorskLIA@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Norwegian-NynorskLIA@2.11_table.html)] |
| `Old_Church_Slavonic-PROIEL` | [[Query](http://universal.grew.fr/?corpus=SUD_Old_Church_Slavonic-PROIEL@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Old_Church_Slavonic-PROIEL@2.11_table.html)] |
| `Old_East_Slavic-Birchbark` | [[Query](http://universal.grew.fr/?corpus=SUD_Old_East_Slavic-Birchbark@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Old_East_Slavic-Birchbark@2.11_table.html)] |
| `Old_East_Slavic-RNC` | [[Query](http://universal.grew.fr/?corpus=SUD_Old_East_Slavic-RNC@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Old_East_Slavic-RNC@2.11_table.html)] |
| 🆕 `Old_East_Slavic-Ruthenian` | [[Query](http://universal.grew.fr/?corpus=SUD_Old_East_Slavic-Ruthenian@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Old_East_Slavic-Ruthenian@2.11_table.html)] |
| `Old_East_Slavic-TOROT` | [[Query](http://universal.grew.fr/?corpus=SUD_Old_East_Slavic-TOROT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Old_East_Slavic-TOROT@2.11_table.html)] |
| `Old_French-SRCMF` | [[Query](http://universal.grew.fr/?corpus=SUD_Old_French-SRCMF@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Old_French-SRCMF@2.11_table.html)] |
| `Old_Russian-RNC` | [[Query](http://universal.grew.fr/?corpus=SUD_Old_Russian-RNC@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Old_Russian-RNC@2.11_table.html)] |
| `Old_Russian-TOROT` | [[Query](http://universal.grew.fr/?corpus=SUD_Old_Russian-TOROT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Old_Russian-TOROT@2.11_table.html)] |
| `Old_Turkish-Tonqq` | [[Query](http://universal.grew.fr/?corpus=SUD_Old_Turkish-Tonqq@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Old_Turkish-Tonqq@2.11_table.html)] |
| `Persian-Seraji` | [[Query](http://universal.grew.fr/?corpus=SUD_Persian-Seraji@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Persian-Seraji@2.11_table.html)] |
| `Persian-PerDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Persian-PerDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Persian-PerDT@2.11_table.html)] |
| `Pomak-Philotis` | [[Query](http://universal.grew.fr/?corpus=SUD_Pomak-Philotis@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Pomak-Philotis@2.11_table.html)] |
| `Polish-LFG` | [[Query](http://universal.grew.fr/?corpus=SUD_Polish-LFG@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Polish-LFG@2.11_table.html)] |
| `Polish-PDB` | [[Query](http://universal.grew.fr/?corpus=SUD_Polish-PDB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Polish-PDB@2.11_table.html)] |
| `Polish-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Polish-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Polish-PUD@2.11_table.html)] |
| `Portuguese-Bosque` | [[Query](http://universal.grew.fr/?corpus=SUD_Portuguese-Bosque@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Portuguese-Bosque@2.11_table.html)] |
| `Portuguese-GSD` | [[Query](http://universal.grew.fr/?corpus=SUD_Portuguese-GSD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Portuguese-GSD@2.11_table.html)] |
| 🆕 `Portuguese-PetroGold` | [[Query](http://universal.grew.fr/?corpus=SUD_Portuguese-PetroGold@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Portuguese-PetroGold@2.11_table.html)] |
| `Portuguese-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Portuguese-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Portuguese-PUD@2.11_table.html)] |
| `Romanian-ArT` | [[Query](http://universal.grew.fr/?corpus=SUD_Romanian-ArT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Romanian-ArT@2.11_table.html)] |
| `Romanian-Nonstandard` | [[Query](http://universal.grew.fr/?corpus=SUD_Romanian-Nonstandard@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Romanian-Nonstandard@2.11_table.html)] |
| `Romanian-RRT` | [[Query](http://universal.grew.fr/?corpus=SUD_Romanian-RRT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Romanian-RRT@2.11_table.html)] |
| `Romanian-SiMoNERo` | [[Query](http://universal.grew.fr/?corpus=SUD_Romanian-SiMoNERo@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Romanian-SiMoNERo@2.11_table.html)] |
| `Russian-GSD` | [[Query](http://universal.grew.fr/?corpus=SUD_Russian-GSD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Russian-GSD@2.11_table.html)] |
| `Russian-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Russian-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Russian-PUD@2.11_table.html)] |
| `Russian-SynTagRus` | [[Query](http://universal.grew.fr/?corpus=SUD_Russian-SynTagRus@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Russian-SynTagRus@2.11_table.html)] |
| `Russian-Taiga` | [[Query](http://universal.grew.fr/?corpus=SUD_Russian-Taiga@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Russian-Taiga@2.11_table.html)] |
| `Sanskrit-UFAL` | [[Query](http://universal.grew.fr/?corpus=SUD_Sanskrit-UFAL@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Sanskrit-UFAL@2.11_table.html)] |
| `Sanskrit-Vedic` | [[Query](http://universal.grew.fr/?corpus=SUD_Sanskrit-Vedic@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Sanskrit-Vedic@2.11_table.html)] |
| `Scottish_Gaelic-ARCOSG` | [[Query](http://universal.grew.fr/?corpus=SUD_Scottish_Gaelic-ARCOSG@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Scottish_Gaelic-ARCOSG@2.11_table.html)] |
| `Serbian-SET` | [[Query](http://universal.grew.fr/?corpus=SUD_Serbian-SET@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Serbian-SET@2.11_table.html)] |
| 🆕 `Sinhala-STB` | [[Query](http://universal.grew.fr/?corpus=SUD_Sinhala-STB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Sinhala-STB@2.11_table.html)] |
| `Skolt_Sami-Giellagas` | [[Query](http://universal.grew.fr/?corpus=SUD_Skolt_Sami-Giellagas@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Skolt_Sami-Giellagas@2.11_table.html)] |
| `Slovak-SNK` | [[Query](http://universal.grew.fr/?corpus=SUD_Slovak-SNK@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Slovak-SNK@2.11_table.html)] |
| `Slovenian-SSJ` | [[Query](http://universal.grew.fr/?corpus=SUD_Slovenian-SSJ@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Slovenian-SSJ@2.11_table.html)] |
| `Slovenian-SST` | [[Query](http://universal.grew.fr/?corpus=SUD_Slovenian-SST@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Slovenian-SST@2.11_table.html)] |
| `Soi-AHA` | [[Query](http://universal.grew.fr/?corpus=SUD_Soi-AHA@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Soi-AHA@2.11_table.html)] |
| `South_Levantine_Arabic-MADAR` | [[Query](http://universal.grew.fr/?corpus=SUD_South_Levantine_Arabic-MADAR@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_South_Levantine_Arabic-MADAR@2.11_table.html)] |
| `Spanish-AnCora` | [[Query](http://universal.grew.fr/?corpus=SUD_Spanish-AnCora@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Spanish-AnCora@2.11_table.html)] |
| `Spanish-GSD` | [[Query](http://universal.grew.fr/?corpus=SUD_Spanish-GSD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Spanish-GSD@2.11_table.html)] |
| `Spanish-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Spanish-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Spanish-PUD@2.11_table.html)] |
| `Swedish-LinES` | [[Query](http://universal.grew.fr/?corpus=SUD_Swedish-LinES@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Swedish-LinES@2.11_table.html)] |
| `Swedish-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Swedish-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Swedish-PUD@2.11_table.html)] |
| `Swedish_Sign_Language-SSLC` | [[Query](http://universal.grew.fr/?corpus=SUD_Swedish_Sign_Language-SSLC@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Swedish_Sign_Language-SSLC@2.11_table.html)] |
| `Swedish-Talbanken` | [[Query](http://universal.grew.fr/?corpus=SUD_Swedish-Talbanken@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Swedish-Talbanken@2.11_table.html)] |
| `Swiss_German-UZH` | [[Query](http://universal.grew.fr/?corpus=SUD_Swiss_German-UZH@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Swiss_German-UZH@2.11_table.html)] |
| `Tagalog-TRG` | [[Query](http://universal.grew.fr/?corpus=SUD_Tagalog-TRG@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Tagalog-TRG@2.11_table.html)] |
| `Tagalog-Ugnayan` | [[Query](http://universal.grew.fr/?corpus=SUD_Tagalog-Ugnayan@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Tagalog-Ugnayan@2.11_table.html)] |
| `Tamil-TTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Tamil-TTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Tamil-TTB@2.11_table.html)] |
| `Tamil-MWTT` | [[Query](http://universal.grew.fr/?corpus=SUD_Tamil-MWTT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Tamil-MWTT@2.11_table.html)] |
| `Tatar-NMCTT` | [[Query](http://universal.grew.fr/?corpus=SUD_Tatar-NMCTT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Tatar-NMCTT@2.11_table.html)] |
| `Teko-TuDeT` | [[Query](http://universal.grew.fr/?corpus=SUD_Teko-TuDeT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Teko-TuDeT@2.11_table.html)] |
| `Telugu-MTG` | [[Query](http://universal.grew.fr/?corpus=SUD_Telugu-MTG@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Telugu-MTG@2.11_table.html)] |
| `Thai-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Thai-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Thai-PUD@2.11_table.html)] |
| `Tupinamba-TuDeT` | [[Query](http://universal.grew.fr/?corpus=SUD_Tupinamba-TuDeT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Tupinamba-TuDeT@2.11_table.html)] |
| `Turkish-Atis` | [[Query](http://universal.grew.fr/?corpus=SUD_Turkish-Atis@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Turkish-Atis@2.11_table.html)] |
| `Turkish-BOUN` | [[Query](http://universal.grew.fr/?corpus=SUD_Turkish-BOUN@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Turkish-BOUN@2.11_table.html)] |
| `Turkish-FrameNet` | [[Query](http://universal.grew.fr/?corpus=SUD_Turkish-FrameNet@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Turkish-FrameNet@2.11_table.html)] |
| `Turkish-GB` | [[Query](http://universal.grew.fr/?corpus=SUD_Turkish-GB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Turkish-GB@2.11_table.html)] |
| `Turkish-IMST` | [[Query](http://universal.grew.fr/?corpus=SUD_Turkish-IMST@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Turkish-IMST@2.11_table.html)] |
| `Turkish-Kenet` | [[Query](http://universal.grew.fr/?corpus=SUD_Turkish-Kenet@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Turkish-Kenet@2.11_table.html)] |
| `Turkish-PUD` | [[Query](http://universal.grew.fr/?corpus=SUD_Turkish-PUD@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Turkish-PUD@2.11_table.html)] |
| `Turkish-Penn` | [[Query](http://universal.grew.fr/?corpus=SUD_Turkish-Penn@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Turkish-Penn@2.11_table.html)] |
| `Turkish-Tourism` | [[Query](http://universal.grew.fr/?corpus=SUD_Turkish-Tourism@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Turkish-Tourism@2.11_table.html)] |
| `Turkish_German-SAGT` | [[Query](http://universal.grew.fr/?corpus=SUD_Turkish_German-SAGT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Turkish_German-SAGT@2.11_table.html)] |
| `Ukrainian-IU` | [[Query](http://universal.grew.fr/?corpus=SUD_Ukrainian-IU@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Ukrainian-IU@2.11_table.html)] |
| `Umbrian-IKUVINA` | [[Query](http://universal.grew.fr/?corpus=SUD_Umbrian-IKUVINA@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Umbrian-IKUVINA@2.11_table.html)] |
| `Upper_Sorbian-UFAL` | [[Query](http://universal.grew.fr/?corpus=SUD_Upper_Sorbian-UFAL@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Upper_Sorbian-UFAL@2.11_table.html)] |
| `Urdu-UDTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Urdu-UDTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Urdu-UDTB@2.11_table.html)] |
| `Uyghur-UDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Uyghur-UDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Uyghur-UDT@2.11_table.html)] |
| `Vietnamese-VTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Vietnamese-VTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Vietnamese-VTB@2.11_table.html)] |
| `Warlpiri-UFAL` | [[Query](http://universal.grew.fr/?corpus=SUD_Warlpiri-UFAL@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Warlpiri-UFAL@2.11_table.html)] |
| `Welsh-CCG` | [[Query](http://universal.grew.fr/?corpus=SUD_Welsh-CCG@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Welsh-CCG@2.11_table.html)] |
| `Western_Armenian-ArmTDP` | [[Query](http://universal.grew.fr/?corpus=SUD_Western_Armenian-ArmTDP@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Western_Armenian-ArmTDP@2.11_table.html)] |
| 🆕 `Western_Sierra_Puebla_Nahuatl-ITML` | [[Query](http://universal.grew.fr/?corpus=SUD_Western_Sierra_Puebla_Nahuatl-ITML@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Western_Sierra_Puebla_Nahuatl-ITML@2.11_table.html)] |
| `Wolof-WTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Wolof-WTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Wolof-WTB@2.11_table.html)] |
| 🆕 `Xavante-XDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Xavante-XDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Xavante-XDT@2.11_table.html)] |
| `Xibe-XDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Xibe-XDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Xibe-XDT@2.11_table.html)] |
| `Yakut-YKTDT` | [[Query](http://universal.grew.fr/?corpus=SUD_Yakut-YKTDT@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Yakut-YKTDT@2.11_table.html)] |
| `Yoruba-YTB` | [[Query](http://universal.grew.fr/?corpus=SUD_Yoruba-YTB@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Yoruba-YTB@2.11_table.html)] |
| `Yupik-SLI` | [[Query](http://universal.grew.fr/?corpus=SUD_Yupik-SLI@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Yupik-SLI@2.11_table.html)] |
| 🆕 `Zaar-Autogramm` | [[Query](http://universal.grew.fr/?corpus=SUD_Zaar-Autogramm@2.11)] [[Relations](http://universal.grew.fr/meta/SUD_Zaar-Autogramm@2.11_table.html)] |


### Conversion from UD to SUD
This page describes the process used in the conversion from UD to SUD. It also explains how this can be adapted to languages specificities.

#### The main sequence

 * `Onf (eud_to_ud)`: Remove all enhanced annotation; the conversion supposes that the input is in basic UD format. Note that it can be safely applied to basic UD, the annotations are left unchanged.
 * `Onf (idioms)`: Add the features encoding of idioms in SUD; namely, features `ExtPos`, `PhraseType`, `InTitle` and `InIdiom` (see [Idioms and titles](./docs/general_guideline/Misc/Idiom_Titles.md)). Note that relations are not changed here.
 * `specific_expr_init`: Add an explicit node for each `ExtPos`. TODO: give detail and an example.
 
 * `Onf (sub_relations)`: Transform UD relations with subtypes into the SUD equivalent.
 * `Onf (rel_extensions)`: Transform remaining UD subtypes (not handled in `sub_relations`) into `deep` SUD feature. For instance, the Polish `cop:locat` is transformed into `cop@locat`.
 * `Onf (relations)`: Transform main UD relation into the SUD equivalent (except `case`, `aux`, `mark` and `cop`, see next step).
 * `reverse_relations.main`: Reverse relations `case`, `aux`, `mark` and `cop`. See below for detail about reversing relations.
 * Move the dependents of a conjunction from the left conjunct to the right conjunct. Dependencies `conj`, `discourse`, `parataxis` and `punct` are not moved. 
    * `Onf (shared_left_conj-dep)`
    * `Onf (unshared_left_conj-dep)`
    * `Onf (minimize_right_conj-dep)`
 * `Onf (add_conj_emb)`: Mark embedded `conj` relations with the extension `emb`.
 * `Onf (chained_relations)`: Dependencies of type `conj`,  and `flat:*` grouped into a bouquet are reorganised into a chain.
 * `specific_expr_close`: Remove specific nodes and edges introduced by the dual package `specific_expr_init`.
 * `Onf (unk_rel)`: Rename all non-SUD relations to `unk` (backoff package).
  
Defining rules for reversing relations is tricky mainly for two reasons:
  * When more than one relations to be reversed have the same head, the order of the reverse operations produced different output. Some mechanism to describe the wanted order is necessary.
  * When reversing a relation from `N` to `M` into a relation from `M` to `N`, we have to decide for each dependent of `N` if it should be lifted up to `M` or if it should stay on `N`.

#### Choosing the order when reversing relations

To constraint the order, a numeric level is given to each edge to be reversed and then:
  1. edge with the smallest level have higher priority
  2. if two edges have the same level and are on the same side of the head, the closest one has higher priority
  3. if two edges have the same level and are on both sides of the head, the one after the head has higher priority.

By default, the 4 relations `case`, `cop`, `aux` and `mark` (and their subtypes) are given the level 10.

We give below examples of conversions with multiple reversing of relations.
In Japanese or in German, the default rules are applied.
The order can be changed by adding different levels to specific relations before calling the strategy `reverse_relations.main` (see examples below for French and Wolof).

##### Japanese
In Japanese all UD relations `case`, `cop`, `aux` and `mark` are left-headed. The constraint 2 applies.

| ![ud_logo](/images/ud.svg) | ![sud_logo](/images/sud.svg) |
|:---------:|:---------:|
| ![japanese_ud_ex](/images/ud_to_sud/ja/3_rel.svg) | ![japanese_ud_ex](/images/ud_to_sud/ja/3_rel__sud_u.svg) |

##### German
In German, there are many cases with edges on both sides. Contraint 3 applies here:

| ![ud_logo](/images/ud.svg) | ![sud_logo](/images/sud.svg) |
|:---------:|:---------:|
| ![german_ud_ex](/images/ud_to_sud/de/bilat.svg) | ![german_sud_ex](/images/ud_to_sud/de/bilat__sud_u.svg) |

##### French

In French, levels are set to:
 * `case` or `case:*` &rarr; 10
 * `cop` or `cop:*` &rarr; 20
 * `aux:caus` or `aux:pass` &rarr; 30
 * `aux` or `aux:*` (≠ `aux:caus` or `aux:pass`) &rarr; 40
 * `mark` or `mark:*` &rarr; 50

From the UD annotation:

![french_example_ud](/images/ud_to_sud/fr/post.svg)

The universal conversion produces:

![french_example_ud_default](/images/ud_to_sud/fr/post__sud_u.svg)

And the conversion with the French specific levels (see [GitHub](https://github.com/surfacesyntacticud/tools/blob/master/converter/grs/fr_UD_to_SUD.grs)):

![french_example_ud_specif](/images/ud_to_sud/fr/post__sud_fr.svg)


##### Wolof

In Wolof, the lemma *na* must always be the head of the whole structure, so it must be the last relation to be reversed. This can be specified with a rule: 

```grew
rule na {
  pattern { e: V -[aux]-> A; A[lemma="na"] }
  commands { e.level = 100 }
}
```

From the UD annotation:

![wolof_example_ud](/images/ud_to_sud/wo/na.svg)

The universal conversion produces:

![wolof_example_ud_default](/images/ud_to_sud/wo/na__sud_u.svg)

And the conversion with the new `na` rule produces (see [GitHub](https://github.com/surfacesyntacticud/tools/blob/master/converter/grs/wo_UD_to_SUD.grs)):

![wolof_example_ud_specif](/images/ud_to_sud/wo/na__sud_wo.svg)

More examples of *na* as the head of a double `aux` construction: [Grew-match](http://universal.grew.fr/?corpus=SUD_Wolof-WTB@conv&custom=6226075687afb).


#### Lifting dependencies

TODO


  

## Publications
### Papers about the SUD annotation scheme and SUD annotated corpora
- Sylvain Kahane, Bernard Caron, Emmett Strickland, Kim Gerdes [Annotation guidelines of UD and SUD treebanks for spoken corpora: a proposal](https://aclanthology.org/2021.tlt-1.4.pdf) in [TLT 2021](https://tlt2021.phil.hhu.de/).

- Sylvain Kahane, Martine Vanhove, Rayan Ziane, Bruno Guillaume. [A morph-based and a word-based treebank for Beja](https://aclanthology.org/2021.tlt-1.5.pdf) in [TLT 2021](https://tlt2021.phil.hhu.de/).

- Kim Gerdes, Bruno Guillaume, Sylvain Kahane, Guy Perrier. [Starting a new treebank? Go SUD! Theoretical and practical benefits of the Surface-Syntactic distributional approach](https://hal.inria.fr/hal-03509136v1) in [DepLing 2021](http://depling.org/depling2021/).

- Kim Gerdes, Bruno Guillaume, Sylvain Kahane, Guy Perrier. [Improving Surface-syntactic Universal Dependencies (SUD): surface-syntactic relations and deep syntactic features](https://hal.inria.fr/hal-02266003v1) in [TLT 2019](https://syntaxfest.github.io/syntaxfest19/tlt2019/tlt2019.html).

- Kim Gerdes, Bruno Guillaume, Sylvain Kahane, Guy Perrier. [SUD or Surface-Syntactic Universal Dependencies: An annotation scheme near-isomorphic to UD](https://hal.inria.fr/hal-01930614v1) in [UDW 2018](https://universaldependencies.org/udw18/).

  

### Other publications related to SUD
Some linguistic arguments in favor of SUD can be found in the Glossa article:

- Timothy Osborne, Kim Gerdes [The status of function words in dependency grammar: A critique of Universal Dependencies (UD)](https://www.glossa-journal.org/article/10.5334/gjgl.537/)

  

Comparing syntactic complexity and cognitive constraint of SUD and UD:

- Yan, Jianwei, and Haitao Liu. [Which annotation scheme is more expedient to measure syntactic difficulty and cognitive demand?.](https://www.aclweb.org/anthology/W19-7903.pdf) Presented at [Quasy](https://quasy-2019.webnode.com/), SyntaxFest 2019.

  

## SUD principles 

SUD is a Surface-syntax Universal Dependencies scheme. SUD follows the Surface syntax criteria (favoring functional heads) and can be automatically converted to the UD scheme. This page describes the universal principles used in SUD and the tagset. Some annotations are shared with UD. See details below.

### SUD relations overview


The picture below describes:
* :blue_square: in blue: the hierarchy of relations specific to SUD
* :green_square: in green: the relations shared with UD
* :orange_square: in orange: the UD relations not used in SUD
* :white_large_square: The light-blue boxes at the bottom correspond to the deep syntactic features.
![taxonomy](/images/taxo.svg)

### Common principles between UD and SUD
Please refer to UD for these aspects:
- [Tokenization and word segmentation](https://universaldependencies.org/u/overview/tokenization.html)
- [Morphology](https://universaldependencies.org/u/overview/morphology.html)
- [POS tags](https://universaldependencies.org/u/pos) ([single document](https://universaldependencies.org/u/pos/all.html))
- [Features](https://universaldependencies.org/u/feat) ([single document](https://universaldependencies.org/u/feat/all.html))
  - [Layered features](https://universaldependencies.org/u/overview/feat-layers.html)
  - [Language-specific features](https://universaldependencies.org/ext-feat-index.html)

The tagset for the **Part Of Speech** follows the UD one. SUD shares a number of syntactic relations with UD too, the list of which is given below (links to UD related page are given):
  [`vocative`](https://universaldependencies.org/u/dep/vocative.html),
  [`compound`](https://universaldependencies.org/u/dep/compound.html),
  [`dislocated`](https://universaldependencies.org/u/dep/dislocated.html),
  [`discourse`](https://universaldependencies.org/u/dep/discourse.html),
  [`appos`](https://universaldependencies.org/u/dep/appos.html),
  [`det`](https://universaldependencies.org/u/dep/det.html),
  [`clf`](https://universaldependencies.org/u/dep/clf.html),
  [`conj`](https://universaldependencies.org/u/dep/conj.html),
  [`cc`](https://universaldependencies.org/u/dep/cc.html),
  [`flat`](https://universaldependencies.org/u/dep/flat.html),
  [`parataxis`](https://universaldependencies.org/u/dep/parataxis.html),
  [`orphan`](https://universaldependencies.org/u/dep/orphan.html),
  [`goeswith`](https://universaldependencies.org/u/dep/goeswith.html),
  [`reparandum`](https://universaldependencies.org/u/dep/reparandum.html),
  [`punct`](https://universaldependencies.org/u/dep/punct.html).

However, we must stress that there are some differences between the usage of some of these relations in UD and SUD. Namely, the relations `appos`, `conj` and `reparandum` are only used when analysing written texts. When analysing oral texts, we use instead the relations `conj:appos`, `conj:coord` and `conj:dicto` respectively (which are specific to SUD). We will explain the details in the section below.

#### Correspondences between UD and SUD

SUD is a dependency-based annotation scheme. Annotation choices rely on surface-syntactic distributional criteria, while at the same time attempting to maintain convertibility with the UD annotation scheme as much as possible.

SUD represents an alternative rather than a competitor to UD, and was designed in such a way that the two can convey the same informational content. The two schemes enjoy a nearly perfect degree of two-way convertibility, meaning that conversions between the two schemes can take place without informational loss in most cases. Because of this, correspondences between the two are most often regular and predictable.

Correspondences between SUD and UD relationships are impacted by several key properties. Firstly, SUD annotations are less redundant and more economical than UD annotations. For example, we can see in the table below that SUD uses a single `subj` relation which comprises both the `nsubj` (nominal subject) and `csubj` (clausal subject) relationships in UD. However, the information provided by UD's distinction between nominal and clausal subjects is not lost in under the simpler SUD scheme: the differentiation can be recovered automatically from the POS of the subject and its context, though how this context is taken into account depends on the language. In total, a subset of 17 UD relations (`nsubj`, `csubj`, `obj`, `iobj`, `obl`, `xcomp`, `ccomp`, `amod`, `nmod`, `nummod`, `advmod`, `acl`, `advcl`, `aux`, `cop`, `case`, `mark`) is replaced by three major relations in SUD: `subj`, `comp`, `mod`, as well as `udep` to a marginal extent.

In addition to its more economical set of labels, SUD also diverges from UD in the sense that it does not systematically label content words as heads. Instead, SUD treats adpositions, subordinating conjunctions, auxiliaries, and copulas as heads. This is because SUD identifies surface syntactic heads using the main criterion that they determine the distribution of the syntactic unit in question. For example, the SUD scheme would identify the preposition *to* in the sentence *Peter talked to Mary* as a head, since it determines the distribution of *Mary*. The UD scheme would label *Mary* as a head based on the fact that it is a content word. Because of this difference, **the direction of certain syntactic relationships is reversed between SUD and UD**. This namely applies to the SUD relationships `aux`, `cop`, `case`, and `mark`, which are also highlighted in **bold** in the correspondence table below. You may also find more information about this aspect of SUD relations on the [general principles](./_index.md#general-sud-principles) section.

##### Table of correspondences between UD and SUD

{{<rawhtml>}}
<table class="center">
    <thead>
        <tr>
            <th><img src="/images/ud.svg" alt="Universal Dependencies (UD)"></th>
            <th><img src="/images/sud.svg" alt="Surface Syntactic Universal Dependencies (SUD)"></th>
        </tr>
    </thead>
    <tbody>
        <tr>
          <td>nsubj</td>
          <td rowspan=2>subj</td>
        </tr>
        <tr>
          <td>csubj</td>
        </tr>
        <tr>
          <td><b>aux</b></td>
          <td>comp:aux</td>
        </tr>
        <tr>
          <td><b>cop</b></td>
          <td>comp:pred</td>
        </tr>
        <tr>
          <td>xcomp</td>
          <td rowspan=5>comp:obj</td>
        <tr>
          <td><b>case</b></td>
        </tr>
        <tr><td><b>mark</b></td></tr>
        <tr><td>obj</td></tr>
        <tr><td>ccomp</td></tr>
        <tr>
          <td>ccomp</td>
          <td rowspan=3>comp:obl</td>
        </tr>
        <tr><td>obl</td></tr>
        <tr>
          <td>iobj</td>
        </tr>
        <tr><td>nmod</td><td>udep</td></tr>
        <tr>
          <td rowspan>obl, acl</td>
          <td rowspan=5>mod</td>
        </tr>
        <tr><td>advcl</td></tr>
        <tr><td>advmod</td></tr>
        <tr><td>amod</td></tr>
        <tr><td>nummod</td></tr>
        <tr>
          <td>fixed</td>
          <td>encoded in node features (see <a href="./docs/general_guideline/Misc/Idiom_Titles.md">here</a>)</td>
        </tr>
        <tr>
          <td>det</td>
          <td rowspan=2>det</td>
        </tr>
        <tr>
          <td>nummod</td>
        </tr>

    </tbody>
</table>
{{</rawhtml>}}



##### Example of a sentence annotated in SUD (above) and UD (below).
![Surface Syntactic Universal Dependencies (SUD)](/images/sud.svg)
{{< conll >}}
\# text = I am out of the office today but will be back tomorrow.
1	I	_	PRON	_	_	2	subj	_	_
2	am	_	AUX	_	_	0	root	_	_
3	out	_	ADP	_	_	2	comp:pred	_	_
4	of	_	ADP	_	_	3	comp:obj	_	_
5	the	_	DET	_	_	6	det	_	_
6	office	_	NOUN	_	_	4	comp:obj	_	_
7	today	_	NOUN	_	_	2	mod	_	_
8	but	_	CCONJ	_	_	9	cc	_	_
9	will	_	AUX	_	_	2	conj	_	_
10	be	_	AUX	_	_	9	comp:aux	_	_
11	back	_	ADV	_	_	10	comp:pred	_	_
12	tomorrow	_	NOUN	_	_	9	mod	_	_
13	.	_	PUNCT	.	_	2	punct	_	_
{{< /conll >}}

![Universal Dependencies (UD)](/images/ud.svg)
{{< conll >}}
\# text = I am out of the office today but will be back tomorrow.
1	I	_	PRON	_	_	6	nsubj	_	_
2	am	_	AUX	_	_	6	cop	_	_
3	out	_	ADP	_	_	6	case	_	_
4	of	_	ADP	_	_	6	case	_	_
5	the	_	DET	_	_	6	det	_	_
6	office	_	NOUN	_	_	0	root	_	_
7	today	_	NOUN	_	_	6	obl:tmod	_	_
8	but	_	CCONJ	_	_	11	cc	_	_
9	will	_	AUX	_	_	11	aux	_	_
10	be	_	AUX	_	_	11	cop	_	_
11	back	_	ADV	_	_	6	conj	_	_
12	tomorrow	_	NOUN	_	_	11	obl:tmod	_	_
13	.	_	PUNCT	.	_	6	punct	_	_
{{< /conll >}}
 
### General SUD principles 

SUD differs from UD in several general principles. The main differences with respect to UD are the following:
- The definition of relations is based on the **syntactic position** and not on semantic relations or the category of the dependents. In other words, two units that commute and exclude each other occupy the same position and must have the same function.

- **Functional heads** (instead of lexical heads): The head of a unit is the distributional head, that is, the element that control the distribution of the unit. This points out the functional head in most cases. For instance, the adposition *to* is the head of *to Mary* because *Mary* and *to Mary* do not have the same distribution (at all).

- In some cases, this criterion does not give a clear situation because two words have head features. In this case, a second gradual criterion comes into play where we prefer to give the status of dependent to the one that changes less the distribution of the unit. According to this principle, a coordinative conjunction such as *and* does not govern the conjunct following it, because *and Mary*, *and red*, or *and is sleeping* occupy completely different positions. In the same way, the determiner is analyzed as a dependent of the noun because nouns partly control the distribution of a combination determiner-noun (*this morning* can work as a modifier of a verb contrary to *this boy*).

- SUD relations are organized in a **taxonomic hierarchy**: A relation that is the daughter of another one inherits its syntactic properties with the addition of specific properties. Indeed, sometimes, we cannot take into account all possible distinctions, either because of the conversion from different treebanks not containing enough information, or because a sentence does not allow to make a clear decision. A way of naming a daughter of a relation `R` is to add an extension `EXT` to `R`, calling this new relation `R:EXT`.

- It is possible to distinguish between **arguments** and **modifiers**: Although this distinction involves semantic criteria (an argument of a lexical unit L is an obligatory participant in the semantic description of L), we consider that it is hard to avoid, because especially for verb dependents, most language have special functions.

- A **multiple coordination**, such as *John, Mary and Peter*, is analyzed as a chain instead of a bouquet: One of the main argument for the chain-analysis is that it reduces the dependency length. See the [page](./docs/general_guideline/Particular_construction/coordination.md) dedicated to coordination.

- There is a strict distinction between surface-syntactic relations and deep-syntactic features expressed as extensions of syntactic relation names using the `@` symbol.


UD relations that are not used in **SUD**:
[`nsubj`](https://universaldependencies.org/u/dep/nsubj.html),
[`csubj`](https://universaldependencies.org/u/dep/csubj.html),
[`obj`](https://universaldependencies.org/u/dep/obj.html),
[`iobj`](https://universaldependencies.org/u/dep/iobj.html),
[`obl`](https://universaldependencies.org/u/dep/obl.html),
[`xcomp`](https://universaldependencies.org/u/dep/xcomp.html),
[`ccomp`](https://universaldependencies.org/u/dep/ccomp.html),
[`amod`](https://universaldependencies.org/u/dep/amod.html),
[`nmod`](https://universaldependencies.org/u/dep/nmod.html),
[`nummod`](https://universaldependencies.org/u/dep/nummod.html),
[`advmod`](https://universaldependencies.org/u/dep/advmod.html),
[`acl`](https://universaldependencies.org/u/dep/acl.html),
[`advcl`](https://universaldependencies.org/u/dep/advcl.html),
[`aux`](https://universaldependencies.org/u/dep/aux.html),
[`cop`](https://universaldependencies.org/u/dep/cop.html),
[`case`](https://universaldependencies.org/u/dep/case.html),
[`mark`](https://universaldependencies.org/u/dep/mark.html).

These 17 relations are replaced by three major relations in SUD --
[`subj`](./docs/general_guideline/Syntactic_relations/subj/subj.md),
[`comp`](./docs/general_guideline/Syntactic_relations/comp/_index.md),
[`mod`](./docs/general_guideline/Syntactic_relations/mod/mod.md)
(subject, complement, modifier) -- with possible sub-relations, in addition to the general [`udep`](./docs/general_guideline/Syntactic_relations/udep/udep.md) (underspecified dependency) to a more marginal extent. The key differences between SUD and UD as well as a table summarizing the most frequent correspondences may be consulted [here](#conversion-from-ud-to-sud).
SUD has 4 specific syntactic relations and a few extended relations:
- [`subj`](./docs/general_guideline/Syntactic_relations/subj/subj.md)
- [`udep`](./docs/general_guideline/Syntactic_relations/udep/udep.md)
- [`comp`](./docs/general_guideline/Syntactic_relations/comp/_index.md)
  - [`comp:aux`](./docs/general_guideline/Syntactic_relations/comp/comp_aux.md)
  - [`comp:cleft`](./docs/general_guideline/Syntactic_relations/comp/comp_cleft.md)
  - [`comp:obj`](./docs/general_guideline/Syntactic_relations/comp/comp_obj.md)
  - [`comp:obl`](./docs/general_guideline/Syntactic_relations/comp/comp_obj.md)
  - [`comp:pred`](./docs/general_guideline/Syntactic_relations/comp/comp_pred.md)
- [`mod`](./docs/general_guideline/Syntactic_relations/mod/mod.md)

#### SUD deep features

In SUD, dependency relations are designed to describe syntactic surface relations. Information related to deep syntax or semantics is given on dependencies with *deep features* which are extensions to dependency label introduced by the `@` symbol.
The main deep features are:
[`@agent`](./docs/general_guideline/Deep/agent.md),
[`@caus`](./docs/general_guideline/Deep/caus.md),
[`@expl`](./docs/general_guideline/Deep/expletiv.md),
[`@lvc`](./docs/general_guideline/Deep/lvc.md),
[`name`](./docs/general_guideline/Deep/name.md),
[`@pass`](./docs/general_guideline/Deep/pass.md),
[`@relcl`](./docs/general_guideline/Deep/relcl.md),
[`@tense`](./docs/general_guideline/Deep/tense.md),
[@scrap](./docs/general_guideline/Deep/scrap.md)
[`@x`](./docs/general_guideline/Deep/x.md).

## Tutorials 

You can find some exercices to practice the SUD annotations [here](). 

We recommand you to use the platform [Arborator Grew](https://arboratorgrew.elizia.net/#/) for your annotation. You can find the documentation [here](https://arborator.github.io/arborator-documentation/#/). 

We then encourage you to use [Grew-Match](http://universal.grew.fr/?corpus=SUD_English-GUM@2.11#) to visualise your annotations and to analyse your corpus. 

## Authors and contributors 