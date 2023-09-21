from nltk.corpus import senseval
i=0;

for inst in senseval.instances('interest.pos')[2150:2170]:
    p = inst.position
    i=i+1
    left = ' '.join(w for (w,t) in inst.context[p-1:p])
    word = ' '.join(w for (w,t) in inst.context[p:p+1])
    right = ' '.join(w for (w,t) in inst.context[p+1:p+2])
    senses = ' '.join(inst.senses)
    print(i,'%20s |%10s | %-15s -> %s' % (left, word, right, senses))

print(i)