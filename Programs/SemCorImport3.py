from lxml import etree

data=[]

with open("Z:\\BE Project\\Training Data\\WSD_Training_Corpora\\SemCor\\semcor\\brown2\\tagfiles\\br-n12.xml","r") as f:
#with open("fruits.xml","r") as f:
  file_content = f.read()
  tree = etree.fromstring(file_content)
  
aword="have"
p_ids =    tree.xpath('//p[s/wf/@lemma="'+aword+'"]/@pnum')
s_ids =    tree.xpath('//s[wf/@lemma="'+aword+'"]/@snum')
wnsn_ids = tree.xpath('//wf[@lemma="'+aword+'"]/@wnsn')

for sid in s_ids:
    sent = tree.xpath('//s[@snum="'+str(sid)+'"]/wf/text()')
    print("\n",sent)
    data.append(sent)

print("Occurences of the word ",aword,":")
print("-----------------------------------")
print("p\ts\twnsn")
for i in range(len(s_ids)):
    print(p_ids[i],"\t",s_ids[i],"\t",wnsn_ids[i])
    
print("\n")

print(data)
