import xml.etree.ElementTree as ET
doc = ET.parse("RGPOST.xml")
root = doc.getroot() # <--- this is the new line
print root.attrib
for elem in range(len(root)):
    print root[elem].attrib
    print root[elem][0].attrib
    for subelem in root[elem]:
        print(subelem.text)
    print(root[elem].text)

