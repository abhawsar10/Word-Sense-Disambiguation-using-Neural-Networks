from lxml import etree
import os

datax=[]
datay=[]
entries = os.listdir('Z:\\BE Project\\Training Data\\WSD_Training_Corpora\\SemCor\\semcor\\brown2\\tagfiles\\')


for entry in entries:
    with open("Z:\\BE Project\\Training Data\\WSD_Training_Corpora\\SemCor\\semcor\\brown2\\tagfiles\\"+entry,"r") as f:
        file_content = f.read()
        tree = etree.fromstring(file_content)
  
   
   
    aword="interest"
    s_ids =    tree.xpath('//s[wf/@lemma="'+aword+'"]/@snum')
    wnsn_ids = tree.xpath('//wf[@lemma="'+aword+'"]/@wnsn')
    context_file_id= tree.xpath('//context/@filename')
    numambi=len(wnsn_ids)


    for sid in s_ids:
        sent = tree.xpath('//s[@snum="'+str(sid)+'"]/wf/text()')
        sentlemma = tree.xpath('//s[@snum="'+str(sid)+'"]/wf/@lemma')
        #print("\n",sent)
        datax.append(sentlemma)
    
    print("-----------------------------------+++")
    print(entry)
    print("Filename: "+str(context_file_id))
    print("Occurences of the word ",aword,":")
    print("---------------")


    for i in s_ids:
        wx=tree.xpath('//wf[@lemma="'+aword+'" and ../@snum="'+i+'"]/@wnsn')
        print("s:"+str(i)+" ; wnsn:"+str(wx))
        datay.append(wx)


print("-----------------------------------+++")
print("-----------------------------------+++")
print("Number of files processed: ",len(entries))
print("\n")
#print(datax)
print(datay)
print("len of datax=",len(datax))