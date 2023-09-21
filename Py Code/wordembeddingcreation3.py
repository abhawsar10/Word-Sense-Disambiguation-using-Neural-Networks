from nltk.corpus import brown
import gensim
from gensim.models import KeyedVectors
from nltk.corpus import senseval

data=[]

k=0
for inst in senseval.instances('interest.pos')[0:2368]:
    p = inst.position
    
    left = ' '.join(w for (w,t) in inst.context[0:p])
    word = ' '.join(w for (w,t) in inst.context[p:p+1])
    right = ' '.join(w for (w,t) in inst.context[p+1:])
    senses = ' '.join(inst.senses)
    #print('%20s |%10s | %-15s -> %s' % (left, word, right, senses))

    lchar=senses[len(senses)-1:len(senses)]
    sens=int(lchar,10)-1
    
    sent1=left+" "+word+" "+right
    sent=sent1.split()
    #print(sent)
    data.append(sent)
    k=k+1
    
print()
#print(brown.categories())
#data=brown.sents(categories="government")
#print(data) 
    

model1 = gensim.models.Word2Vec(data, min_count = 1,  
                              size = 100, window = 5,hs=1, negative=0) 
  
# Print results 

model1.save("word2vec.model")

alic=model1.wv.most_similar('interest',topn=5000)

for i in range(100):
    print(i,alic[i])
    














    