"""
Protocole pour vérifier la relation subj en français.  J'ai décomposé la relation subj dans tous les différents pattern qu'elle peut prendre :
- nominal 
- adverbial dans le cas des déterminants composés
- symbole
- x (disfluence et foreign)
- numéral

Pour le moment, le script repère ces patterns et associe une grammaire GRS quand la correction peut se faire automatiquement. Le lien n'est pas encore fonctionnel. 
Le script repère les relations `subj`qui sont hors pattern. 

TODO : 
- faire un rapport des relations extraites avec les patterns
- 
"""
import sys, os, json
import pandas as pd 
import protocolemodule
import grewpy


sys.path.insert(0, os.path.abspath(os.path.join( os.path.dirname(__file__), "."))) # Use local grew lib

from grewpy import Corpus, CorpusDraft, Request, grew_web
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))) 

import grewpy
from grewpy import Corpus, CorpusDraft, Request, grew_web
from grewpy.grew_web import Grew_web

from grewpy import Graph, CorpusDraft, Request, Corpus, request_counter

from grewpy import Graph

from grewpy import Corpus, GRSDraft, Rule, Request, Commands, GRS, set_config

set_config("sud")

# Charger un corpus 

pud_file = "corpora/SUD_French-ParisStories/ParisStories_2022_hamacTahiti.conllu"
pud = Corpus(pud_file)


with open("french/output/output_french_subj.json") as file:
   content = json.load(file)

get_upos_and_feat = {}
get_pattern = []
construct_request = []
for element in content:
  for key,value in element.items():
    if key == "upos_and_value_feats":
       get_upos_and_feat= value
    if key == "specific_pattern":
       for kk,vv in value.items():
          for kkk,vvv in vv.items():
             if kkk == "pattern":
                get_pattern.append(vvv)

for gov,dep in get_upos_and_feat.items():
   i = 0 
   while i < len(dep):
      request = Request(f"DEP[ExtPos={dep[i]}/upos={dep[i]}] ; GOV [upos={gov}]; GOV-[1=subj]->DEP")
      print(f"DEP[ExtPos={dep[i]}/upos={dep[i]}] ; GOV [upos={gov}]; GOV-[1=subj]->DEP")
      i = i +1
      construct_request.append(request)



print(get_pattern)


exit()
# Extraire la relation subj en fonction des différentes règles 

deprel = "subj"
good_result = []
false_result = []



exit()

## sujet nominal : upos =  NOUN, PROPN ou PRON
"""
La relation sujet peut-être entre un NOM, un PRONOM ou un NOM PROPRE et un AUXILIAIRE ou un VERBE
"""

req_gov_noun = Request(f"DEP[upos=NOUN|PROPN|PRON] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP")
print(f"nombre de {deprel} nominaux dans {pud_file} : ", pud.count(req_gov_noun))
result_nom = pud.search(req_gov_noun)

for element in pud.search(req_gov_noun):
    good_result.append(element)

df_noun = pd.DataFrame(result_nom)
df_noun = df_noun.assign(name=True)
df_noun = df_noun.rename(columns={'name': f'DEP[upos=NOUN|PROPN|PRON] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP'})

## sujet adverbiale avec ExtPos = NOUN o           u PRON
"""
Le sujet peut être de la forme suivante : ADVERBE de NOM VERBE ou AUXILIAIRE. Dans ce cas, la tête est l'adverbe, qui a une ExtPos = PRON.
"""

req_gov_adv = Request(f"DEP[upos=ADV, ExtPos = PRON] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP")
print(f"nombre de {deprel} adverbiaux avec extpo dans {pud_file} : ", pud.count(req_gov_adv))
result_adv = (pud.search(req_gov_adv))

for element in pud.search(req_gov_adv):
    good_result.append(element)

df_adv = pd.DataFrame(result_adv)
name = "DEP = ADV , ExtPos = PRON"
df_adv = df_adv.assign(name=True)
df_adv = df_adv.rename(columns={'name': f'DEP[upos=ADV, ExtPos = PRON] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP'})

### repérer les sujet adv sans ExtPos  

req_gov_adv_false = Request(f"DEP[upos=ADV, !ExtPos] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP")
print(f"nombre de {deprel} adverbiaux sans extpo dans {pud_file} : ", pud.count(req_gov_adv))
result_adv_false = (pud.search(req_gov_adv_false))

for element in pud.search(req_gov_adv_false):
    false_result.append(element)

string_grs = """
rule add_extpos_adv {
  pattern { DEP[upos=ADV, !ExtPos] ; GOV [upos=AUX|VERB] ; GOV-[1=subj]->DEP }
  commands { DEP.ExtPos = PRON}
}
strat s2 { Onf (det) }
"""

grs_adv = GRS(string_grs)
# graph = sent_id
# print ("nb of output with strat s2 (should be 1) ---> ", end='')
# print (len (grs_adv.run(graph, strat="s2")))

## sujet inconnu : upos = X
"""
Le sujet peut avoir comme POS = X, trois cas sont possibles :
- Foreign = Yes
- cas des disfluences. Quand c'est possible, il y a une ExtPos qui renseigne la POS qu'aurait ou avoir l'amorce.
"""

req_gov_x = Request(f"DEP[upos=X] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP")
print(f"nombre de {deprel} X dans {pud_file} : ", pud.count(req_gov_x))
result_x = pud.search(req_gov_x)

for element in pud.search(req_gov_x):
    good_result.append(element)

df_x = pd.DataFrame(result_x)
df_x = df_x.assign(name=True)
df_x = df_x.rename(columns={'name': f'DEP[upos=X] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP'})
### repérer les sujet X sans ExtPos et sans Foreign -> pour les vérifier (trouver un moyen de les valider (tagger))

req_gov_x_false = Request(f"DEP[upos=X, !ExtPos, !Foreign] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP")
print(f"nombre de {deprel} adverbiaux sans extpo dans {pud_file} : ", pud.count(req_gov_adv))
result_x_false = (pud.search(req_gov_x_false))

for element in pud.search(req_gov_x_false):
    false_result.append(element)

df_x_false = pd.DataFrame(result_x_false)
df_x_false = df_x_false.assign(name=False)
df_x_false = df_x_false.rename(columns={'name': f"DEP[upos=X, !ExtPos, !Foreign] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP"})

## sujet numéral
"""
Le sujet peut être de la catégorie NUM 
"""

req_gov_num = Request(f"DEP[upos=NUM] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP")
print(f"nombre de {deprel} X dans {pud_file} : ", pud.count(req_gov_num))
result_num = pud.search(req_gov_num)

for element in pud.search(req_gov_num):
    good_result.append(element)

df_num = pd.DataFrame(result_num)
df_num = df_num.assign(name=True)
df_num = df_num.rename(columns={'name': f'DEP[upos=NUM] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP'})

## sujet symbole : upos = SYM 
"""
Autre cas possibles : le sujet est de type SYM (exemple : %). Dans ce cas, il y a normalement une ExtPos = NOUN 
"""

req_gov_sym = Request(f"DEP[upos=SYM, ExtPos = NOUN|PRON] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP")
print(f"nombre de {deprel} X dans {pud_file} : ", pud.count(req_gov_sym))
result_sym = pud.search(req_gov_sym)

for element in pud.search(req_gov_sym):
    good_result.append(element)

df_sym = pd.DataFrame(result_num)
df_sym = df_sym.assign(name=True)
df_sym = df_sym.rename(columns={'name': f'DEP[upos=SYM, ExtPos = NOUN|PRON] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP'})

### repérer les sujet SYM sans ExtPos 

req_gov_sym_false = Request(f"DEP[upos=SYM, !ExtPos] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP")
print(f"nombre de {deprel} adverbiaux sans extpo dans {pud_file} : ", pud.count(req_gov_adv))
result_sym_false = (pud.search(req_gov_sym_false))

for element in pud.search(req_gov_sym_false):
    false_result.append(element)

string_grs = """
rule add_extpos_adv {
  pattern { DEP[upos=ADV, !ExtPos] ; GOV [upos=AUX|VERB] ; GOV-[1=subj]->DEP }
  commands { DEP.ExtPos = NOUN}
}
strat s2 { Onf (det) }
"""

grs_sym = GRS(string_grs)

df_sym_false = pd.DataFrame(result_sym_false)
df_sym_false = df_sym_false.assign(name=False)
df_sym_false = df_sym_false.rename(columns={'name': f"DEP[upos=SYM, !ExtPos] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP"})

## le reste des sujets -> à corriger ou ajouter dans le validateur des règles
"""
Comment trouver le reste des sujets ? 
- On garde les informations récupérer, et on fait un search de tous les sujets restants ? 
"""

# fonctionnement des listes de dictionnaires de résultats 
# for element in result_adv:
#     for key,value in element.items():
#         print(key,value)

request = Request(f"GOV[]; DEP []; GOV-[1={deprel}]->DEP")
all_subject = pud.search(request) #clustering_parameter=[], clustering_keys=[], flat=None)
#print(all_subject)
print(good_result)


print("Element : ",protocolemodule.compare_two_listes(all_subject,good_result))


print("Elements : ",protocolemodule.compare_three_listes(all_subject,good_result,false_result))

error = protocolemodule.compare_three_listes(all_subject,good_result,false_result)

df_err = pd.DataFrame(error)
df_err = df_err.assign(name=False)
df_err = df_err.rename(columns={'name': 'ERROR'})


# créer dataframe pour report 
df = pd.concat([df_adv, df_noun, df_x, df_sym, df_num, df_sym_false, df_x_false, df_err], join='outer', sort=False)

# Afficher le résultat
df.to_csv('test_dataframe.csv', sep=',', quotechar='"')

exit(0)
pud_file = "ParisStories_2023_afterFashionWeek.conllu"
pud = Corpus(pud_file)
print(pud)

corpus = CorpusDraft(pud)
print("\n=============== Iteration on graphs of a corpus ===============")
acc = 0
for sent_id in corpus:
  acc += len(corpus[sent_id])
print(f"nb of nodes in {pud_file} = ", acc)
print (request_counter())

def clear_edges(graph):
    for n in graph:
        graph.sucs[n] = []

for sid in corpus:
  clear_edges(corpus[sid])

noedge_corpus = Corpus(corpus)
print(" ----- counting subj within corpus -----")
dep = "subj"
req = Request(f"X[];Y[];X -[{dep}]-> Y")
print(f"nb of {dep} in {pud_file} = ", pud.count(req))
print(f"nb of {dep} in noedge_corpus = ", noedge_corpus.count(req))

deprel = "subj"
# '/' ne foncitonne pas 
#req_gov_noun = Request(f"DEP[upos=NOUN|PROPN|PRON/ExtPos=NOUN|PROPN|PRON] ; GOV [upos=AUX|VERB] ; GOV-[1={deprel}]->DEP")
#print(f"nombre de {deprel} nominaux dans {pud_file} : ", pud.count(req_gov_noun))
dict_with_graph = pud.get_all()
for key,value in dict_with_graph.items():
    #print(value.to_conll()) -> ne fonctionne pas : pourquoi ? 
    print(json.dumps(value.json_data(), indent=4))


exit(0)

print ("\n=============== len ===============")
print(f"nb of graph in {pud_file} = {len(pud)}")
print (request_counter())

print ("\n=============== Get one graph ===============")
sent_id="ParisStories_2023_afterFashionWeek_afterFashionWeek__1"
graph = pud[sent_id]
print(f"nb of nodes of {sent_id} = ", len(graph))
print (request_counter())

print(f"len(pud[0]) = {len(pud[0])}")
print(f"len(pud[-1]) = {len(pud[-1])}")
print(f"[len(g) for g in pud[-3:]] = {[len(g) for g in pud[-3:]]}")
#other forms pud[-3:-1], pud[1:7:2], ...


print ("\n=============== Iteration on graphs of a corpus ===============")
print ("⚠️  generate one request to Grew backend for each graph")
acc = 0
for sent_id in pud.get_sent_ids():
  acc += len(pud[sent_id])
print(f"nb of nodes in {pud_file} = ", acc)
print (request_counter())

print ("\n=============== Count request in a corpus ===============")
upos="ADV"
req = Request(f"X[upos={upos}]")

print(" ----- basic count -----")
print(f"nb of {upos} in {pud_file} = ", pud.count(req))

print (" ----- count with clustering -----")
print(f"nb of {upos} in {pud_file}, clustered by lemma:")
print (json.dumps(pud.count(req, ["X.lemma"]), indent=2))
print (request_counter())


corpus = CorpusDraft(pud)
print("\n=============== Iteration on graphs of a corpus ===============")
acc = 0
for sent_id in corpus:
  acc += len(corpus[sent_id])
print(f"nb of nodes in {pud_file} = ", acc)
print (request_counter())

def clear_edges(graph):
    for n in graph:
        graph.sucs[n] = []

for sid in corpus:
  clear_edges(corpus[sid])

noedge_corpus = Corpus(corpus)
print(" ----- counting subj within corpus -----")
dep = "subj"
req = Request(f"X[];Y[];X -[{dep}]-> Y")
print(f"nb of {dep} in {pud_file} = ", pud.count(req))
print(f"nb of {dep} in noedge_corpus = ", noedge_corpus.count(req))


req = Request(f"X -[udep]-> Y")
print (" ----- count with clustering -----")
print(f"nb of udep in {pud_file}, clustered by head.lemma:")
print (json.dumps(pud.count(req, ["X.lemma"]), indent=2))


g = pud[sent_id]
print(g)
for n in g:
  print(n)

exit(0)
#   for (s,e) in g.sucs(n):
#     if e  == {'1' : 'udep'}:
#       print(f"\n{n} : {g[n]} -[{e}]-> {s} : {g[s]}\n")

# clear_edges(g)
#pud[sent_id] = g
# NOTE: the next line does not work properly (not __set_item__ called), have a look to https://stackoverflow.com/questions/26189090/how-to-detect-if-any-element-in-a-dictionary-changes
# clear_edges(pud[sent_id]) ==> WARNING: does not change pud!