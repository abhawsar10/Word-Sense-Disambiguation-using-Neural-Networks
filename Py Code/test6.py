from nltk.tokenize import sent_tokenize, word_tokenize 
import warnings 

warnings.filterwarnings(action = 'ignore') 
  
import gensim
from gensim.models import Word2Vec 
  
#  Reads ‘alice.txt’ file 
sample = open("C:\\Users\\Admin\\Desktop\\alice.txt", "r", encoding="utf8") 
s = sample.read() 
  
# Replaces escape character with space 
f = s.replace("\n", " ") 
data = [] 
  
# iterate through each sentence in the file 
for i in sent_tokenize(f): 
    temp = [] 
      
    # tokenize the sentence into words 
    for j in word_tokenize(i): 
        temp.append(j.lower()) 
  
    data.append(temp) 
  
# Create CBOW model 
model1 = gensim.models.Word2Vec(data, min_count = 1,  
                              size = 100, window = 5,hs=1, negative=0) 
  
# Print results 
print("Cosine similarity between 'alice' " + 
               "and 'wonderland' - CBOW : ", 
    model1.similarity('alice','wonderland')) 
      
print("Cosine similarity between 'alice' " + 
               "and 'porpoise' - CBOW : ", 
    model1.similarity('alice', 'porpoise')) 
  
print("Cosine similarity between 'alice' " + 
               "and 'porpoise' - CBOW : ", 
    model1.similarity('alice', 'hat')) 


alic=model1.wv.most_similar('alice',topn=5000)

for i in range(100):
    print(i,alic[i][0])

#print(model1)
#help(model1.wv.most_similar_cosmul)
# Create Skip Gram model 
#model2 = gensim.models.Word2Vec(data, min_count = 1, size = 100,window = 5, sg = 1) 
  
# Print results 
#print("Cosine similarity between 'alice' " +"and 'wonderland' - Skip Gram : ",     model2.similarity('alice', 'wonderland')) 
      
#print("Cosine similarity between 'alice' " +"and 'machines' - Skip Gram : ",       model2.similarity('alice', 'machines')) 








