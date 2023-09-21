from nltk.corpus import brown
import gensim
from gensim.models import KeyedVectors
from nltk.corpus import senseval


print(brown.categories())
data=brown.sents(categories="government")
print(data)

model1 = gensim.models.Word2Vec(data, min_count = 1,  
                              size = 100, window = 5,hs=1, negative=0) 
  
# Print results 

model1.save("word2vec.model")

alic=model1.wv.most_similar('interest',topn=5000)

for i in range(4990,5000):
    print(i,alic[i])
    
