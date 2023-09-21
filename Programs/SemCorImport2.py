import xml.etree.ElementTree as ET

#tree = ET.ElementTree(file='Z:\BE Project\Training Data\WSD_Training_Corpora\SemCor\semcor\brown2\tagfiles\br-n12.xml')

files=open("Z:\\BE Project\\Training Data\\WSD_Training_Corpora\\SemCor\\semcor\\brown2\\tagfiles\\br-n12.xml","r")

tree = ET.parse(files)

root = tree.getroot()
p=0
s=0

for i in root[0][p][s].iter('wf'):
    print(i.text)
    
result=root[0][p][s].iterfind('wf')
print("\n",result)

for i in root[0][p][s].iterfind('wf'):
    print(i)
