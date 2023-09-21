import pickle

aword="crown"



with open("Z:\\BE Project\\Data Storage\\"+aword+"_data_y.txt", "rb") as fp:   
    datay = pickle.load(fp)
print(datay)


dataysensekeys=[]
    
linno=0    
fil = open('Z:\\BE Project\\Training Data\\WSD_Training_Corpora\\SemCor\\semcor.gold.key.txt', "rt")

for f in fil:
    linno=linno+1
    for i in range(len(datay)):
        if datay[i][0] in f:
            print(linno,"---",f)
            dataysensekeys.append(f[15:-1])
fil.close()

print(dataysensekeys)
















