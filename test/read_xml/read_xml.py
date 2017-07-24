from xml.dom import minidom

# open xml file
file_dir = '/Users/doghome/work/guanplus-test/test/read_xml/info.xml'
dom = minidom.parse(file_dir)

# get xml file parameter
root = dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)
