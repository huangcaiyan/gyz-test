# -*- encoding:utf-8 -*-

from xml.dom import minidom

# 获得标签信息
# open xml file
file_dir = '/Users/doghome/work/guanplus-test/test/read_xml/info.xml'
dom = minidom.parse(file_dir)

# get xml file parameter
root = dom.documentElement

print 'nodename=>',root.nodeName
print 'nodeValue=>',root.nodeValue
print 'nodeType=>',root.nodeType
print 'ELEMENT_NODE=>',root.ELEMENT_NODE
