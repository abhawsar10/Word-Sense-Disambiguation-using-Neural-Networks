from nltk.stem import PorterStemmer
import nltk
ps = PorterStemmer() 

#str=input("Enter String\n")

str1="Eating in bed is easier said than done, as it is heavily dependant on the bedding clothing"
tokenAux=""
textAux=""

tokens = nltk.word_tokenize(str1)
for token in tokens:
    tokenAux = ps.stem(token)    
    textAux = textAux + " "+ tokenAux
print("Stemmer Output:",textAux,"\n")


from nltk.stem import WordNetLemmatizer 

lem = WordNetLemmatizer() 

print("cacti :", lem.lemmatize("cacti")) 
print("rocks :", lem.lemmatize("rocks"))  
print("corpora :", lem.lemmatize("corpora")) 
  
# a denotes adjective in "pos" 
print("better :", lem.lemmatize("better", pos ="a")) 