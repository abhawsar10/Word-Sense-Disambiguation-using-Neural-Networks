import xml.etree.ElementTree as ET

#tree = ET.ElementTree(file='Z:\BE Project\Training Data\WSD_Training_Corpora\SemCor\semcor\brown2\tagfiles\br-n12.xml')

files=open("Z:\\BE Project\\Training Data\\WSD_Training_Corpora\\SemCor\\semcor\\brown2\\tagfiles\\br-n12.xml","r")

tree = ET.parse(files)

#print(help(open))

# for child in root:
#     root2=child
#     for child2 in root2:
#         root3=child2
#         for child3 in root3:
#             root4=child3
#             for child4 in root4:
#                 print(child4.tag)
         
root = tree.getroot()
p=0
s=0

for i in root[0][p][s]:
    print(i.text)