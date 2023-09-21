from nltk.corpus import wordnet as wn
import numpy as np
import re
from nltk.corpus import wordnet as wn

sense_key_regex = r"(.*)\%(.*):(.*):(.*):(.*):(.*)"
synset_types = {1:'n', 2:'v', 3:'a', 4:'r', 5:'s'}

def synset_from_sense_key(sense_key):
    lemma, ss_type, lex_num, lex_id, head_word, head_id = re.match(sense_key_regex, sense_key).groups()
    
    for syn in wn.synsets(lemma):
        #print(syn.lemmas())
        for syn2 in syn.lemmas():
            #print(syn2.key())
            if sense_key == syn2.key():
                return lemma,syn

x = "crown%1:06:00::"

word,wordidx= synset_from_sense_key(x)

print(wx)

wx=wn.synsets(word);

print("Synset             :",wordidx)
print("Synset Name        :",wordidx.name())
print("Synset Definition  :",wordidx.definition())
print("Number of Senses :",len(wx))
print("---------------------------")
#print("Synsets  :",wx)

mat=np.zeros(shape=(len(wx),1), dtype='int')


i=0
for s in wx:
    if wordidx == s:
        mat[i]=1
    i=i+1

print(mat)













 