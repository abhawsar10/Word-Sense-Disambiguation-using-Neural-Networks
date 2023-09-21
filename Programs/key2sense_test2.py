from nltk.corpus import wordnet as wn
import numpy as np
import re
from nltk.corpus import wordnet as wn


sense_key_regex = r"(.*)\%(.*):(.*):(.*):(.*):(.*)"
synset_types = {1:'n', 2:'v', 3:'a', 4:'r', 5:'s'}

x = "review%1:09:00::"


def synset_from_sense_key(sense_key):
    lemma, ss_type, lex_num, lex_id, head_word, head_id = re.match(sense_key_regex, sense_key).groups()
    
    for syn in wn.synsets(lemma):
        #print(syn.lemmas())
        for syn2 in syn.lemmas():
            #print(syn2.key())
            if sense_key == syn2.key():
                return syn

word=synset_from_sense_key(x)

print(word)
print(word.definition())
#syns=wn.synsets(word)
#print(syns[0].lemmas()[0].key())








 