
from nltk.corpus import semcor

for i in [15]:
    
    sent = semcor.xml('brown2/tagfiles/br-n12.xml').findall('context/p/s')[i]
    
    for wordform in sent.getchildren():
        print(wordform.text, end=' ')
        for key in sorted(wordform.keys()):
            print(key + '=' + wordform.get(key), end=' ')
        print()