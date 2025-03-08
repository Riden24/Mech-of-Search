import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('Mech-of-Search\cran.qry.xml')  # Replace 'input.xml' with your file name



root = tree.getroot()

# Iterate through each <top> element and update <num>
for index, top in enumerate(root.findall('top'), start=1):
    num = top.find('num')
    num.text = str(index)  # Update <num> to the current index

# Save the updated XML to a new file
tree.write('cran_updated.qry.xml', encoding='utf-8', xml_declaration=True)

print("XML file has been updated and saved as 'output.xml'.")
