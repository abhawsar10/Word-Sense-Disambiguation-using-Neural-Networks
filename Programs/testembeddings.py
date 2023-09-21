from nltk.corpus import brown
import gensim
from gensim.models import Word2Vec

model = Word2Vec.load("word2vec.model")

alic=model1.wv.most_similar('crown',topn=5000)

for i in range(10):
    print(i,alic[i][0])
    

p="the interest rate on this assets is killing development"#input("enter sentence\n")
ip=p.split()
print('\n',ip)
l=len(ip)

featurevec=alic

for i in range(11):
    flag=0
    for j in range(l):
        if alic[i][0].lower()==ip[j].lower():
            flag=1
    featurevec[i]=flag
        

print(featurevec[0:10])
        