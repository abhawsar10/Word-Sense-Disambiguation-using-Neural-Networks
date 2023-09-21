from nltk.corpus import senseval
import pickle

data=[]
for inst in senseval.instances('interest.pos')[:]:
    p = inst.position
    left = ' '.join(w for (w,t) in inst.context[0:p])
    word = ' '.join(w for (w,t) in inst.context[p:p+1])
    right = ' '.join(w for (w,t) in inst.context[p+1:])
    senses = ' '.join(inst.senses)

    lchar=senses[len(senses)-1:len(senses)]
    sens=int(lchar,10)-1

    sent1=left+" "+word+" "+right
    sent=sent1.split()

    print("Sense=",sens)
    data.append(sent)
    
print(data)

with open("data.txt", "wb") as fp:   #Pickling
    pickle.dump(data, fp)

