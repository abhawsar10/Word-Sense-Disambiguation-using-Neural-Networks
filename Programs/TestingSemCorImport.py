import xml.etree.ElementTree as ET


tree = ET.parse('fruits.xml')
root = tree.getroot()

for child in root:
     print(child.tag, child.attrib)
     
print(root[0][2].text)

#for Ns in root.iter('rank'):
 #   print(Ns.text)
    
    