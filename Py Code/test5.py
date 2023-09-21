from nltk.corpus import wordnet as wn

syns=wn.synsets('interest')

definitions=['readiness to give attention','quality of causing attention to be given to','activity, etc. that one gives attention to','advantage, advancement or favor','a share in a company or business','money paid for the use of money']

from nltk.corpus import senseval
i=0
for inst in senseval.instances('interest.pos')[0:1]:
    p = inst.position

    left = ' '.join(w for (w,t) in inst.context[0:p])
    word = ' '.join(w for (w,t) in inst.context[p:p+1])
    right = ' '.join(w for (w,t) in inst.context[p+1:])
    senses = ' '.join(inst.senses)
    print('%20s |%10s | %-15s -> %s' % (left, word, right, senses))
    i=i+1
    
print(i)
lchar=senses[len(senses)-1:len(senses)]
sens=int(lchar,10)-1
print("Definition:=",definitions[sens],"\n")
